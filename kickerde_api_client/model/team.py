"""Upstream model for sports teams."""

from typing import NotRequired, TypedDict

from .core import CountryId, LeagueId, Stadium


type TeamId = int


class Team(TypedDict):
    """Upstream model for a sports team."""

    id: TeamId
    defaultLeagueId: LeagueId
    shortName: str
    longName: str
    countryId: NotRequired[CountryId]
    stadium: NotRequired[Stadium]
