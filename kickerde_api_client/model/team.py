"""Upstream model for sports teams."""

from typing import NotRequired, TypedDict

from .core import CountryId, Stadium
from .league_id import LeagueId

type TeamId = int
"""Upstream ID for a sports team."""


class Team(TypedDict):
    """Upstream model for a sports team."""

    id: TeamId
    defaultLeagueId: LeagueId
    shortName: str
    longName: str
    countryId: NotRequired[CountryId]
    stadium: NotRequired[Stadium]
