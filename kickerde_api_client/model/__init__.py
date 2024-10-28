"""Python types for the upstream API."""

from collections.abc import Mapping
from typing import Literal, NotRequired, TypedDict


# Re-export these symbols
# (This promotes them from .model.api to .model)
from .association import Association as Association
from .core import (
    Country as Country,
    CountryId as CountryId,
    MediaObject as MediaObject,
    ObjectId as ObjectId,
    RessortId as RessortId,
    RessortIdHome as RessortIdHome,
    SportId as SportId,
    StadiumId as StadiumId,
    Stadium as Stadium,
    StateId as StateId,
    TrackRessortId as TrackRessortId,
)
from .match import (
    ApprovalId as ApprovalId,
    Match as Match,
    MatchId as MatchId,
    MatchResults as MatchResults,
    MatchTeam as MatchTeam,
    Period as Period,
    TeamToken as TeamToken,
)
from .league import (
    ConferenceId as ConferenceId,
    DivisionId as DivisionId,
    Gameday as Gameday,
    GamedayId as GamedayId,
    GroupId as GroupId,
    League as League,
    LeagueSeason as LeagueSeason,
    LeagueTable as LeagueTable,
    LeagueTableEntry as LeagueTableEntry,
    LeagueTableId as LeagueTableId,
    Season as Season,
    SeasonId as SeasonId,
)
from .league_id import LeagueId as LeagueId
from .team import TeamId as TeamId, Team as Team


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
