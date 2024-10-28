"""Upstream model for sports matches and their state."""

from enum import IntEnum
from typing import NotRequired, TypedDict

from datetype import NaiveDateTime

from .core import CountryId, LeagueId, SportId
from .league import SeasonId
from .team import TeamId

type MatchId = int
type TeamToken = str


class MatchTeam(TypedDict):
    """Upstream model for a sports team that takes part in a match."""

    id: TeamId
    defaultLeagueId: LeagueId
    shortName: str
    longName: str
    urlName: str
    iconSmall: str
    iconBig: str
    token: TeamToken


class MatchResults(TypedDict):
    """Upstream model for the results of a sports match."""

    hergAktuell: int
    """Current standings for the home team."""

    aergAktuell: int
    """Current standings for the away team."""

    hergHz: NotRequired[int]
    """Standings for the home team by the end of the first half."""

    aergHz: NotRequired[int]
    """Standings for the away team by the end of the first half."""

    hergEnde: NotRequired[int]
    """Standings for the home team by the end of the match."""

    aergEnde: NotRequired[int]
    """Standings for the away team by the end of the match."""


class ApprovalId(IntEnum):
    """Degree of certainty with which a match is scheduled."""

    SCHEDULED = 0
    """The match is tentatively scheduled (`Angesetzt`)."""

    CONFIRMED = 1
    """The match schedule is confirmed (`Vorschau`)."""

    LIVE = 12
    """The match is currently being played (`Live`)."""

    UNKNOWN_13 = 13
    """This value has not been observed in the wild yet."""

    FINISHED = 14
    """The match is over and a report (`Spielbericht`) has been
    published.
    """


class Period(IntEnum):
    """The degree of progress in a match."""

    BEFORE = 0
    """The match has not started."""

    FIRST_HALF = 1
    """The first half is underway."""

    HALF_TIME = 2
    """The first half has completed. The second half has not started."""

    SECOND_HALF = 3
    """The second half is underway."""

    FINISHED = 4
    """The match is over."""


class Match(TypedDict):
    """Upstream model for a sports match."""

    id: MatchId
    leagueId: LeagueId
    leagueShortName: str
    leagueLongName: str
    seasonId: SeasonId
    roundId: int
    homeTeam: MatchTeam
    guestTeam: MatchTeam
    results: NotRequired[MatchResults]
    date: NaiveDateTime
    completed: bool
    currentMinute: int

    currentPeriod: Period
    """The phase into which the match has progressed."""

    approvalId: ApprovalId
    """Degree of certainty with which this match is scheduled."""

    approvalName: str
    """German-language description of the degree of certainty."""

    timeConfirmed: bool
    sportId: SportId
    displayKey: int
    round: str
    leaguePriority: int
    countryId: CountryId
    country: str
    leagueUrlName: str
    state: str
    modifiedAt: NaiveDateTime
    currentDateTime: NaiveDateTime
