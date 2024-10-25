"""Mapping and transformation logic for seasons of a given league."""

from typing import Any, cast

import xmltodict

from ..model import Season, SeasonId
from . import Submapper, SubmapperKey, XmlMappingHelper


def league_season_list_to_dict(
    xml: str,
) -> dict[SeasonId, Season]:
    """Transforms an API response to a dictionary of `Season` objects,
    indexed by season ID.

    :param xml:
        a response to a `LeagueSeasonList/3/ligid/{leagueId}` query.
    """
    submappers: dict[SubmapperKey, Submapper] = {
        'seasons': _map_seasons_dict,
        'season': _map_season,
    }

    return cast(
        dict[SeasonId, Season],
        xmltodict.parse(
            xml, postprocessor=XmlMappingHelper(submappers).map
        )['seasons'],
    )


def _map_seasons_dict(
    key: str, value: Any
) -> tuple[str, dict[SeasonId, Season]]:
    # Remove extraneous `season` key below `seasons`
    seasons = value['season']
    return key, {season['id']: season for season in seasons}


def _map_season(key: str, value: Any) -> tuple[str, str | int]:
    if key in {
        'currentRoundId',
        'displayKey',
        'displayKey2',
        'table',
        'winnerId',
    }:
        return key, int(value)
    return key, value
