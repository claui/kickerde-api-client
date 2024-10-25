# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use

import pytest

from kickerde_api_client import Api
from kickerde_api_client.model import Season
from kickerde_api_client.provider import ResponseProvider


@pytest.fixture(name='api')
def fixture_api(canned_response_provider: ResponseProvider) -> Api:
    return Api(provider=canned_response_provider)


def test_seasons(api: Api) -> None:
    seasons = api.seasons(league=2)
    assert '2023/24' in seasons
    assert seasons['2023/24'] == Season(
        {
            'id': '2023/24',
            'currentRoundId': 34,
            'displayKey': 1463946397394926719,
            'displayKey2': 114688,
            'table': 2,
            'winnerId': 18,
            'winnerLongName': 'FC St. Pauli',
            'points': '69',
            'goals': '62:36',
        }
    )
