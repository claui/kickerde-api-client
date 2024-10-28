# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use

import pytest

from kickerde_api_client import Api
from kickerde_api_client.model import (
    League,
    LeagueId,
    RessortId,
    TableCalculatorType,
    TrackRessortId,
    SportId,
)
from kickerde_api_client.provider import ResponseProvider


@pytest.fixture(name='api')
def fixture_api(canned_response_provider: ResponseProvider) -> Api:
    return Api(provider=canned_response_provider)


def test_2_bundesliga(api: Api) -> None:
    leagues = api.leagues()
    assert 2 in leagues
    assert leagues[LeagueId(2)] == League(
        {
            'id': LeagueId.BUNDESLIGA_2,
            'shortName': '2.BL',
            'longName': '2. Bundesliga',
            'currentSeasonId': '2024/25',
            'currentRoundId': 10,
            'displayKey': 1463946397394926719,
            'displayKey2': 114688,
            'table': 2,
            'countryId': 'D',
            'sportId': SportId.ASSOCIATION_FOOTBALL,
            'imId': 2,
            'urlName': '2-bundesliga',
            'uShortName': '2.BL',
            'ressortId': RessortId.BUNDESLIGA_2,
            'trackRessortId': TrackRessortId.BUNDESLIGA_2,
            'trackRessortName': '2. Bundesliga',
            'tblcalc': TableCalculatorType.LEAGUE,
            'tickerQuoteAd': True,
            'gamedayQuoteAd': True,
            'socialmedia': True,
            'goalgetters': True,
            'history': True,
        }
    )


def test_friendlies(api: Api) -> None:
    leagues = api.leagues()
    assert 999 in leagues
    assert leagues[LeagueId(999)] == League(
        {
            'id': LeagueId.FRIENDLIES,
            'shortName': 'Freundschaft',
            'longName': 'Freundschaftsspiele',
            'currentSeasonId': '2023',
            'currentRoundId': 1,
            'displayKey': 4294967296,
            'displayKey2': 0,
            'table': 1,
            'countryId': 'S2',
            'sportId': SportId.ASSOCIATION_FOOTBALL,
            'imId': 999,
            'urlName': 'freundschaftsspiele',
            'uShortName': 'FREUND',
            'ressortId': RessortId.NON_DOMESTIC_TIER_3,
            'trackRessortId': TrackRessortId.HOME,
            'trackRessortName': 'Home',
            'goalgetters': False,
            'history': False,
        }
    )
