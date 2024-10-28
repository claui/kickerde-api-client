# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use

import datetype
import pytest

from kickerde_api_client import Api
from kickerde_api_client.model import LeagueId
from kickerde_api_client.provider import ResponseProvider


@pytest.fixture(name='api')
def fixture_api(canned_response_provider: ResponseProvider) -> Api:
    return Api(provider=canned_response_provider)


async def test_league_season_2_bundesliga(api: Api) -> None:
    league_season = await api.league_season(
        league=LeagueId(2), season='2024/25'
    )
    assert league_season['id'] == LeagueId.BUNDESLIGA_2
    assert league_season['country']['id'] == 'D'
    assert league_season['syncMeinKicker'] is False
    assert league_season['goalgetters'] is True
    assert 98 in league_season['teams']

    svd = league_season['teams'][98]
    assert svd['longName'] == 'SV Darmstadt 98'
    assert svd['defaultLeagueId'] == LeagueId.BUNDESLIGA_2
    assert svd['stadium']['name'] == 'Merck-Stadion am Böllenfalltor'

    gamedays = league_season['gamedays']
    assert 0 not in gamedays
    assert gamedays[1]['title'] == '1. Spieltag'
    assert gamedays[1]['dateFrom'] == datetype.fromisoformat(
        '2024-08-02T20:30:00'
    )
    assert gamedays[1]['dateTo'] == datetype.fromisoformat(
        '2024-08-04T13:30:00'
    )


async def test_league_season_landespokal_hessen(api: Api) -> None:
    league_season = await api.league_season(
        league=LeagueId(6081), season='2024/25'
    )
    assert league_season['id'] == LeagueId.LPHS
    assert league_season['country']['id'] == 'D'
    assert league_season['syncMeinKicker'] is False
    assert league_season['goalgetters'] is False

    gamedays = league_season['gamedays']
    assert 0 not in gamedays
    assert [gameday['title'] for gameday in gamedays.values()] == [
        '1. Spieltag',
        '2. Spieltag',
        'Achtelfinale',
        'Viertelfinale',
        'Halbfinale',
        'Finale',
    ]
