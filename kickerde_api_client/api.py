"""The primary module in kickerde_api_client."""

import json
import sys
from typing import Any

import datetype

from .mapping.league_list import league_list_home_to_dict
from .mapping.league_season_info import league_season_info_to_dict
from .mapping.my_team_sync import my_team_sync_to_dict
from .mapping.season_list import league_season_list_to_dict
from .logging import get_logger
from .model import (
    League,
    LeagueId,
    LeagueSeason,
    MyTeamSync,
    Season,
    SeasonId,
    Team,
    TeamId,
)
from .provider import DefaultResponseProvider, ResponseProvider

logger = get_logger(__name__)


class Api:
    """The primary API client and entry point for all requests."""

    def __init__(
        self,
        provider: ResponseProvider | None = None,
    ) -> None:
        self._provider = provider or DefaultResponseProvider()

    async def leagues(self) -> dict[LeagueId, League]:
        """Returns all leagues and tournaments known to the system.

        :return:
            a dictionary of :py:class:`~.model.League` objects, indexed
            by league ID.
        """
        return league_list_home_to_dict(
            await self._provider.get('LeagueListHome/3'),
        )

    async def seasons(
        self, league: League | LeagueId
    ) -> dict[SeasonId, Season]:
        """Returns all known seasons for the given league or tournament.

        :param league:
            the ID of the league or tournament.
            Alternatively, a :py:class:`~.model.League` object.

        :return:
            a dictionary of :py:class:`~.model.Season` objects, indexed
            by season ID.
        """
        league_id = league['id'] if isinstance(league, dict) else league
        return league_season_list_to_dict(
            await self._provider.get(
                f'LeagueSeasonList/3/ligid/{league_id}'
            ),
        )

    async def league_season(
        self,
        league: League | LeagueId,
        season: Season | SeasonId,
    ) -> LeagueSeason:
        """Returns an informational structure for the given league and
        season. Aside from league properties, the structure contains
        dictionaries that provide info on teams and match days (aka
        gamedays).

        :param league:
            the ID of the league or tournament.
            Alternatively, a :py:class:`~.model.League` object.

        :param season:
            the ID of the season.
            Alternatively, a :py:class:`~.model.Season` object.

        :return: a :py:class:`~.model.LeagueSeason` object.
        """
        league_id = league['id'] if isinstance(league, dict) else league
        season_id = season['id'] if isinstance(season, dict) else season
        return league_season_info_to_dict(
            await self._provider.get(
                f'LeagueSeasonInfo/3/ligid/{league_id}/saison/{season_id}'
            ),
        )

    async def my_team_sync(self, team: Team | TeamId) -> MyTeamSync:
        """Returns an informational structure for live and upcoming
        matches played by the given team.

        :param team:
            the ID of the team.
            Alternatively, a :py:class:`~.model.Team` object.

        :return: a :py:class:`~.model.MyTeamSync` object.
        """
        team_id = team['id'] if isinstance(team, dict) else team
        return my_team_sync_to_dict(
            await self._provider.get(f'MyTeamSync/3/vrnid/{team_id}')
        )

    async def dump_leagues(self) -> None:
        """Dumps all leagues to stdout in JSON format."""
        json.dump(
            await self.leagues(),
            sys.stdout,
            ensure_ascii=False,
            indent=4,
        )

    async def dump_seasons(self, league: League | LeagueId) -> None:
        """Dumps all seasons to stdout in JSON format.

        :param league:
            the ID of the league or tournament.
            Alternatively, a :py:class:`~.model.League` object.
        """
        json.dump(
            await self.seasons(league=league),
            sys.stdout,
            ensure_ascii=False,
            indent=4,
        )

    async def dump_league_season(
        self,
        league: League | LeagueId,
        season: Season | SeasonId,
    ) -> None:
        """Dumps a :py:class:`~.model.LeagueSeason` object to stdout
        in JSON format.

        :param league:
            the ID of the league or tournament.
            Alternatively, a :py:class:`~.model.League` object.

        :param season:
            the ID of the season.
            Alternatively, a :py:class:`~.model.Season` object.
        """
        json.dump(
            await self.league_season(league=league, season=season),
            sys.stdout,
            default=_serialize_with_datetime_support,
            ensure_ascii=False,
            indent=4,
        )

    async def dump_my_team_sync(self, team: Team | TeamId) -> None:
        """Dumps a :py:class:`~.model.MyTeamSync` object to stdout in
        JSON format.

        :param team:
            the ID of the team.
            Alternatively, a :py:class:`~.model.Team` object.
        """
        json.dump(
            await self.my_team_sync(team=team),
            sys.stdout,
            default=_serialize_with_datetime_support,
            ensure_ascii=False,
            indent=4,
        )


def _serialize_with_datetime_support(
    obj: datetype.NaiveDateTime | Any,
) -> str:
    if isinstance(obj, datetype.NaiveDateTime):
        return obj.isoformat()
    raise TypeError(f'Cannot serialize {type(obj)} to JSON')
