"""Mapping and transformation logic for leagues and tournaments."""

from typing import Any, cast

import xmltodict

from ..model import League, LeagueId
from . import Submapper, SubmapperKey, XmlMappingHelper
from .league import map_league_properties


def league_list_home_to_dict(
    xml: str,
) -> dict[LeagueId, League]:
    """Transforms an API response to a dictionary of
    :py:class:`~.model.League` objects, indexed by league ID.

    :param xml:
        a response to a `LeagueListHome/3` query.
    """
    submappers: dict[SubmapperKey, Submapper] = {
        'leagues': _map_leagues_dict,
        'league': map_league_properties,
    }

    return cast(
        dict[LeagueId, League],
        xmltodict.parse(
            xml, postprocessor=XmlMappingHelper(submappers).map
        )['leagues'],
    )


def _map_leagues_dict(
    key: str, value: Any
) -> tuple[str, dict[LeagueId, League]]:
    # Remove extraneous `league` key below `leagues`
    leagues = value['league']
    return key, {league['id']: league for league in leagues}
