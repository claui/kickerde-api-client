"""Upstream model for leagues, tournaments, and seasons."""

from collections.abc import Mapping
from typing import Literal, NotRequired, TypedDict

from datetype import NaiveDateTime

from .association import Association
from .core import (
    Country,
    CountryId,
    SportId,
    StateId,
    RessortId,
    RessortIdHome,
    TrackRessortId,
)
from .league_id import LeagueId as LeagueId
from .team import TeamId, Team


type ConferenceId = int
"""Upstream ID with unknown semantics."""

type DivisionId = int
"""Upstream ID with unknown semantics."""

type GamedayId = int
"""Upstream ID for a match day within a league or tournament."""

type GroupId = int
"""Upstream ID with unknown semantics."""

type LeagueTableId = int
"""Upstream ID for a (partial or complete) league table."""

type SeasonId = str
"""Upstream ID for a season of a league or tournament."""


class League(TypedDict):
    """Upstream model for a league or tournament."""

    id: LeagueId
    shortName: str
    longName: str
    currentSeasonId: SeasonId
    currentRoundId: int
    currentRoundName: NotRequired[str]
    iconSmall: NotRequired[str]
    iconBig: NotRequired[str]
    displayKey: int
    displayKey2: int
    table: NotRequired[int]
    stateId: NotRequired[StateId]
    countryId: CountryId
    associationId: NotRequired[Association]
    sportId: SportId
    teamOrigin: NotRequired[bool]
    imId: int
    urlName: str
    uShortName: str
    friendlyName: NotRequired[str]
    ressortId: NotRequired[RessortId]
    ressortIdHome: NotRequired[RessortIdHome]
    trackRessortId: NotRequired[TrackRessortId]
    trackRessortName: NotRequired[str]
    priority: NotRequired[int]
    tblcalc: NotRequired[bool]
    tickerQuoteAd: NotRequired[bool]
    gamedayQuoteAd: NotRequired[bool]
    gamedayButtonTitle: NotRequired[str]
    socialmedia: NotRequired[bool]
    goalgetters: NotRequired[bool]
    history: NotRequired[bool]
    hasTransfers: NotRequired[bool]
    adKeywords: NotRequired[str]


class Season(TypedDict):
    """Upstream model for the season of a league or tournament."""

    id: SeasonId
    currentRoundId: int
    displayKey: int
    displayKey2: int
    table: NotRequired[int]
    winnerId: TeamId | Literal[0]
    winnerLongName: NotRequired[str]
    points: NotRequired[str]
    goals: NotRequired[str]


class Gameday(TypedDict):
    """Upstream model for a match day."""

    id: GamedayId
    title: str
    dateFrom: NotRequired[NaiveDateTime]
    dateTo: NotRequired[NaiveDateTime]
    hideForTable: NotRequired[bool]


class LeagueSeason(TypedDict):
    """Upstream model for a hierarchical view on a league in a season.
    Contains teams and match days (dubbed  :py:attr:`.gamedays`) as
    submappings.

    Submappings are indexed by team ID or gameday ID, respectively.
    """

    id: LeagueId
    shortName: str
    longName: str
    country: NotRequired[Country]
    teamType: str
    teams: Mapping[TeamId, Team]
    gamedays: Mapping[GamedayId, Gameday]
    iconSmall: str
    iconBig: str
    currentSeasonId: SeasonId
    currentRoundId: int
    displayKey: int
    displayKey2: int
    table: NotRequired[int]
    ressortId: NotRequired[RessortId]
    ressortIdHome: NotRequired[RessortId]
    tblcalc: NotRequired[bool]
    socialmedia: NotRequired[bool]
    syncMeinKicker: NotRequired[bool]
    goalgetters: bool


class LeagueTableEntry(TypedDict):
    """Upstream model for an entry in a league table."""

    id: TeamId

    rank: int
    """The numeric rank of the table entry.

    Note that in the context of the league table that contains this
    entry, the values of `rank` may be non-unique (due to ties) and
    sparse (also due to ties, or because the league table might
    represent a focused subwindow of an actual league table).
    """

    shortName: str
    longName: str
    sortName: str
    defaultLeagueId: LeagueId
    games: int
    goalsFor: int
    goalsAgainst: int
    wins: int
    ties: int
    lost: int
    points: int
    direction: Literal['up', 'down'] | None
    winsOvertime: int
    winsPenalty: int
    lostOvertime: int
    lostPenalty: int
    groupId: GroupId | None
    groupName: str | None
    divisionId: DivisionId | None
    divisionName: str | None
    conferenceId: ConferenceId | None
    conferenceName: str | None
    iconSmall: str
    iconBig: str


class LeagueTable(TypedDict):
    """Upstream model for a league table."""

    id: LeagueTableId
    leagueId: LeagueId
    name: str
    seasonId: SeasonId
    roundId: int

    entries: dict[TeamId, LeagueTableEntry]
    """Dictionary containing :py:class:`.LeagueTableEntry` objects,
    ordered by :py:attr:`~.LeagueTableEntry.rank` but indexed by
    team ID.

    See :py:attr:`.LeagueTableEntry.rank` for details on why this
    dictionary is indexed by team rather than by rank.
    """
