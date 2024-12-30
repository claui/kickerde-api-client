"""Upstream model for sports matches and their state."""

from enum import IntEnum
from typing import NotRequired, TypedDict

from datetype import NaiveDateTime

from .core import CountryId, SportId
from .league import SeasonId
from .league_id import LeagueId
from .team import TeamId

type MatchId = int
"""Upstream ID for a sports match."""

type TeamToken = str
"""Three- to four-letter abbreviation for a match participant."""


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
    """German-language editorial shorthand for the league or tournament.

    Equivalent to the :py:attr:`~.model.League.shortName` of a :py:class:`~.model.League`.

    Example: `2.BL` for `2. Bundesliga`
    """

    leagueLongName: str
    """German-language full-name of the league or tournament.

    Equivalent to the :py:attr:`~.model.League.longName` of a :py:class:`~.model.League`.
    """

    seasonId: SeasonId

    roundId: int
    """Ordinal of the round, 1-based.

    Correlates to :py:attr:`.round`, e.g. `roundId` is `18`
    if `round` is equal to `“18. Spieltag”`.
    """

    homeTeam: MatchTeam
    guestTeam: MatchTeam
    results: NotRequired[MatchResults]

    date: NaiveDateTime
    """Date and time for which the match is scheduled to begin.

    Implies a timezone of `Europe/Berlin`.
    """

    completed: bool
    """`True` if the match is over, `False` otherwise."""

    currentMinute: int
    """How many minutes of the match have passed.
    Includes minutes that have started but not completed.

    Typically equal to 0 if the match has not started.

    Equal to the duration of the match in minutes if the match is over.
    """

    currentPeriod: Period
    """The phase into which the match has progressed."""

    approvalId: ApprovalId
    """Degree of certainty with which this match is scheduled."""

    approvalName: str
    """German-language description of the degree of certainty.
    Correlates with :py:attr:`.approvalId`.

    Examples:

    - `Angesetzt`
    - `Vorschau`
    - `Live`
    """

    timeConfirmed: bool
    """Whether the association has confirmed the date and time."""

    sportId: SportId
    """Upstream ID for the type of sport."""

    displayKey: int
    """Sorting key for editorial purposes."""

    round: str
    """German-language display name of the round or match day.

    Example: `18. Spieltag`
    """

    leaguePriority: int
    """Editorial priority of the league that hosts the match.

    Equivalent to the :py:attr:`~.model.League.priority` of a :py:class:`~.model.League`.
    """

    countryId: CountryId
    """Upstream ID for a country that hosts the match."""

    country: str
    """German-language name of the country hosting the match.

    Correlates with :py:attr:`.countryId`.
    """

    leagueUrlName: str
    """URL-friendly league name. Example: ``serie-a`` for `Serie A`."""

    state: str
    """German-language description of a purpose, status, or rationale.

    Example: `Regulär`
    """

    modifiedAt: NaiveDateTime
    """Server-side timestamp. Implies a timezone of `Europe/Berlin`."""

    currentDateTime: NaiveDateTime
    """Server-side timestamp of when this library has retrieved the data.

    Implies a timezone of `Europe/Berlin`.
    """
