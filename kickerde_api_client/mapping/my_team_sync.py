"""Mapping and transformation logic for :py:class:`~.model.LeagueSeason`
objects.
"""

from typing import Any, cast

import datetype
import xmltodict

from ..model import (
    LeagueTableEntry,
    MatchId,
    Match,
    MediaObject,
    MyTeamSync,
    ObjectId,
    TeamId,
)
from . import Submapper, SubmapperKey, XmlMappingHelper
from .league import map_league_properties
from .team import map_team_properties


def my_team_sync_to_dict(xml: str) -> MyTeamSync:
    """Transforms an API response to a :py:class:`~.model.MyTeamSync`
    object.

    :param xml:
        a response to a `MyTeamSync/3/vrnid/{teamId}` query.
    """
    submappers: dict[SubmapperKey, Submapper] = {
        ('team',): _map_root_properties,
        'match': _map_match_properties,
        'matches': _map_matches,
        'homeTeam': map_team_properties,
        'guestTeam': map_team_properties,
        'results': _map_match_result_properties,
        'objects': _map_media_objects,
        'video': _map_media_object_properties,
        'document': _map_media_object_properties,
        'teams': _map_league_table_entries,
        (
            'team',
            'table',
            'teams',
            'team',
        ): _map_league_table_entry_properties,
        'league': map_league_properties,
    }

    return cast(
        MyTeamSync,
        xmltodict.parse(
            xml,
            postprocessor=XmlMappingHelper(submappers).map,
            force_list=(
                'document',
                'video',
            ),
        )['team'],
    )


def _map_root_properties(
    key: str, value: Any
) -> tuple[str, str | int | bool]:
    if key in {
        'id',
        'defaultLeagueId',
    }:
        return key, int(value)
    if key in {
        'changeMeinKicker',
        'syncMeinKicker',
    }:
        return key, bool(int(value))
    return key, value


def _map_matches(
    key: str, value: Any
) -> tuple[str, dict[MatchId, Match]]:
    # Remove extraneous `match` key below `matches`
    matches = value['match']
    return key, {match['id']: match for match in matches}


def _map_match_properties(
    key: str, value: Any
) -> tuple[str, str | int | bool | datetype.NaiveDateTime]:
    if key in {
        'id',
        'leagueId',
        'roundId',
        'currentMinute',
        'currentPeriod',
        'approvalId',
        'sportId',
        'displayKey',
        'leaguePriority',
    }:
        return key, int(value)
    if key in {
        'completed',
        'timeConfirmed',
    }:
        return key, bool(int(value))
    if key in {
        'date',
        'modifiedAt',
        'currentDateTime',
    }:
        timestamp: datetype.NaiveDateTime = datetype.fromisoformat(  # pylint: disable=duplicate-code
            value
        ).replace(tzinfo=None)
        return (key, timestamp)
    return key, value


def _map_match_result_properties(
    key: str, value: Any
) -> tuple[str, int]:
    if isinstance(value, str):
        return key, int(value)
    return key, value


def _map_media_objects(
    key: str, value: Any
) -> tuple[
    str,
    dict[str, dict[ObjectId, MediaObject]],
]:
    # Fix property names; also index items by media object ID
    return key, {
        'documents': {
            media['id']: media for media in value.get('document', ())
        },
        'videos': {
            media['id']: media for media in value.get('video', ())
        },
    } | {
        media_type: value
        for media_type, value in value.items()
        if media_type not in {'document', 'video'}
    }


def _map_media_object_properties(
    key: str, value: Any
) -> tuple[str, str | int | datetype.NaiveDateTime]:
    if key in {
        'id',
        'ressortId',
        'typId',
        'duration',
    }:
        return key, int(value)
    if key in {'date'}:
        timestamp: datetype.NaiveDateTime = datetype.fromisoformat(  # pylint: disable=duplicate-code
            value
        ).replace(tzinfo=None)
        return (key, timestamp)
    return key, value


def _map_league_table_entries(
    _: str, value: Any
) -> tuple[
    str,
    dict[str, dict[TeamId, LeagueTableEntry]],
]:
    # Remove extraneous `team` key below `teams`;
    # also rename `teams` to `entries`
    entries = value['team']
    return 'entries', {entry['id']: entry for entry in entries}


def _map_league_table_entry_properties(
    key: str, value: Any
) -> tuple[str, str | int]:
    if key in {
        'id',
        'rank',
        'defaultLeagueId',
        'goalsFor',
        'goalsAgainst',
        'wins',
        'lost',
        'points',
        'winsOvertime',
        'winsPenalty',
        'lostOvertime',
        'lostPenalty',
    }:
        return key, int(value)
    return key, value
