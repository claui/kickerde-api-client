"""Python types for the upstream API."""

from collections.abc import Mapping
from typing import Any, Literal, NotRequired, TypedDict

from datetype import NaiveDateTime


type ApprovalId = int
type AssociationId = int
type ConferenceId = int
type CountryId = str
type DivisionId = int
type GamedayId = int
type GroupId = int
type LeagueId = int
type LeagueTableId = int
type MatchId = int
type ObjectId = int
type RessortId = int
type SeasonId = str
type SportId = int
type StadiumId = int
type StateId = int
type TeamId = int
type TeamToken = str


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
    associationId: NotRequired[AssociationId]
    sportId: SportId
    teamOrigin: NotRequired[bool]
    imId: int
    urlName: str
    uShortName: str
    friendlyName: NotRequired[str]
    ressortId: NotRequired[RessortId]
    ressortIdHome: NotRequired[RessortId]
    trackRessortId: NotRequired[RessortId]
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


class Country(TypedDict):
    """Upstream model for a country."""

    id: CountryId
    shortName: str
    longName: str
    isoName: str
    iconSmall: str


class Stadium(TypedDict):
    """Upstream model for a sports venue."""

    id: StadiumId
    name: str
    city: str


class Team(TypedDict):
    """Upstream model for a sports team."""

    id: TeamId
    defaultLeagueId: LeagueId
    shortName: str
    longName: str
    countryId: NotRequired[CountryId]
    stadium: NotRequired[Stadium]


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


class Gameday(TypedDict):
    """Upstream model for a match day."""

    id: GamedayId
    title: str
    dateFrom: NotRequired[NaiveDateTime]
    dateTo: NotRequired[NaiveDateTime]
    hideForTable: NotRequired[bool]


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
    currentPeriod: int
    approvalId: ApprovalId
    approvalName: str
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


type MediaObject = Any
"""Upstream abstraction for a document, slideshow, or video."""


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


class MyTeamSync(TypedDict):
    """Upstream model for live or upcoming matches played by a
    given team.
    """

    id: TeamId
    countryId: NotRequired[CountryId]
    defaultLeagueId: LeagueId
    shortName: str
    longName: str

    matches: Mapping[MatchId, Match]
    """Matches played by this team, indexed by match ID."""

    objects: Mapping[
        Literal['documents', 'slideshows ', 'videos'],
        Mapping[ObjectId, MediaObject],
    ]
    table: LeagueTable
    league: League
    iconSmall: str
    iconBig: str
    changeMeinKicker: NotRequired[bool]
    syncMeinKicker: NotRequired[bool]
