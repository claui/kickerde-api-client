"""Mapping and transformation logic for :py:class:`~.model.LeagueSeason`
objects.
"""

from typing import Any, cast

import datetype
import xmltodict

from ..model import Gameday, GamedayId, LeagueSeason, Team, TeamId
from . import map_default, Submapper, SubmapperKey, XmlMappingHelper
from .team import map_team_properties


def league_season_info_to_dict(xml: str) -> LeagueSeason:
    """Transforms an API response to a :py:class:`~.model.LeagueSeason`
    object.

    :param xml:
        a response to a `LeagueSeasonInfo/3/ligid/{leagueId}/saison/{season}` query.
    """
    submappers: dict[SubmapperKey, Submapper] = {
        'league': _map_league_properties,
        'teams': _map_teams,
        'team': map_team_properties,
        'stadium': map_default,
        'gameday': _map_gameday_properties,
        'gamedays': _map_gamedays,
    }

    return cast(
        LeagueSeason,
        xmltodict.parse(
            xml, postprocessor=XmlMappingHelper(submappers).map
        )['league'],
    )


def _map_league_properties(
    key: str, value: Any
) -> tuple[str, str | int | bool]:
    if key in {
        'currentRoundId',
        'displayKey',
        'displayKey2',
        'id',
        'ressortId',
        'ressortIdHome',
        'table',
        'tblcalc',
    }:
        return key, int(value)
    if key in {
        'goalgetters',
        'socialmedia',
        'syncMeinKicker',
    }:
        return key, bool(int(value))
    return key, value


def _map_teams(key: str, value: Any) -> tuple[str, dict[TeamId, Team]]:
    # Remove extraneous `team` key below `teams`
    teams = value['team']
    return key, {team['id']: team for team in teams}


def _map_gamedays(
    key: str, value: Any
) -> tuple[str, dict[GamedayId, Gameday]]:
    # Remove extraneous `gameday` key below `gamedays`
    gamedays = value['gameday']
    return key, {day['id']: day for day in gamedays}


def _map_gameday_properties(
    key: str, value: Any
) -> tuple[str, str | int | datetype.NaiveDateTime]:
    if key in {
        'id',
    }:
        return key, int(value)
    if key in {
        'hideForTable',
    }:
        return key, bool(int(value))
    if key in {
        'dateFrom',
        'dateTo',
    }:
        timestamp: datetype.NaiveDateTime = datetype.fromisoformat(  # pylint: disable=duplicate-code
            value
        ).replace(tzinfo=None)
        return (key, timestamp)
    return key, value
