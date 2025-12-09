# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use, too-few-public-methods

import re
from typing import NamedTuple
from urllib.parse import unquote_plus

import pytest

from kickerde_api_client.provider import ResponseProvider


def _load_canned_response(path_to_canned_xml: str) -> str:
    with open(
        f'tests/fixtures/{path_to_canned_xml}',
        encoding='utf-8',
        mode='r',
    ) as file:
        return file.read()


class _LeagueSeasonUrlMatch(NamedTuple):
    league_id: str
    season_id: str


def _match_single_value(
    property_name: str, pattern: str | re.Pattern[str], path: str
) -> str | None:
    if match := re.fullmatch(pattern, path):
        return match.group(property_name)
    return None


def _match_league_id(
    pattern: str | re.Pattern[str], path: str
) -> str | None:
    return _match_single_value('league_id', pattern, path)


def _match_league_season_id(
    pattern: str | re.Pattern[str], path: str
) -> _LeagueSeasonUrlMatch | None:
    if match := re.fullmatch(pattern, path):
        return _LeagueSeasonUrlMatch(
            league_id=match.group('league_id'),
            season_id=unquote_plus(match.group('season_id')).replace(
                '/', '-'
            ),
        )
    return None


def _match_team_id(
    pattern: str | re.Pattern[str], path: str
) -> str | None:
    return _match_single_value('team_id', pattern, path)


class CannedResponseProvider(ResponseProvider):
    """Fake response provider that uses only canned responses."""

    async def get(self, path: str) -> str:
        return _load_canned_response(
            CannedResponseProvider._path_to_xml_file(path)
        )

    @staticmethod
    def _path_to_xml_file(path: str) -> str:
        if path == 'LeagueListHome/3':
            return 'league-list-home.xml'

        if league_id := _match_league_id(
            r'LiveConference/3/ligid/(?P<league_id>\d+)',
            path,
        ):
            return f'live-conference/league-{league_id}.xml'

        if league_id := _match_league_id(
            r'LeagueSeasonList/3/ligid/(?P<league_id>\d+)',
            path,
        ):
            return f'league-season-list/league-{league_id}.xml'

        if league_season_tuple := _match_league_season_id(
            r'LeagueSeasonInfo/3/ligid/(?P<league_id>\d+)/saison/(?P<season_id>.+)',
            path,
        ):
            league_id, season_id = league_season_tuple
            return (
                f'league-season-info/league-{league_id}-{season_id}.xml'
            )

        if team_id := _match_team_id(
            r'MyTeamSync/3/vrnid/(?P<team_id>\d+)',
            path,
        ):
            return f'my-team-sync/team-{team_id}.xml'

        raise ValueError(
            f'No canned response for URL path: {path}',
        )


@pytest.fixture(name='canned_response_provider')
def fixture_canned_response_provider() -> CannedResponseProvider:
    return CannedResponseProvider()
