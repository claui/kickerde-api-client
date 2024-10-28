# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use

import datetype
import pytest

from kickerde_api_client import Api
from kickerde_api_client.model import ApprovalId, MatchResults, Period
from kickerde_api_client.provider import ResponseProvider


@pytest.fixture(name='api')
def fixture_api(canned_response_provider: ResponseProvider) -> Api:
    return Api(provider=canned_response_provider)


def test_lecce(api: Api) -> None:
    team = api.my_team_sync(team=713)
    assert team['id'] == 713
    assert team['countryId'] == 'I'
    assert team['changeMeinKicker'] is False
    assert team['syncMeinKicker'] is False
    assert len(team['matches']) == 2
    assert 4937475 in team['matches']

    match = team['matches'][4937475]
    assert match['leagueLongName'] == 'Serie A'
    assert match['state'] == 'Regulär'
    assert match['completed'] is False
    assert match['timeConfirmed'] is True
    assert match['currentMinute'] == 83
    assert match['currentPeriod'] == Period.SECOND_HALF
    assert match['approvalId'] == ApprovalId.LIVE
    assert match['approvalName'] == 'Live'
    assert match['leaguePriority'] == 1
    assert match['modifiedAt'] == datetype.fromisoformat(
        '2024-10-26T16:34:50'
    )
    assert match['currentDateTime'] == datetype.fromisoformat(
        '2024-10-26T16:40:54'
    )

    home_team = match['homeTeam']
    assert home_team['id'] == 717
    assert home_team['defaultLeagueId'] == 700
    assert home_team['shortName'] == 'Neapel'
    assert home_team['token'] == 'NEA'

    away_team = match['guestTeam']
    assert away_team['id'] == 713
    assert away_team['defaultLeagueId'] == 700
    assert away_team['shortName'] == 'Lecce'
    assert away_team['token'] == 'LEC'

    assert match['results'] == MatchResults(
        hergAktuell=1,
        aergAktuell=0,
        hergHz=0,
        aergHz=0,
    )

    videos = team['objects']['videos']
    assert len(videos) == 3
    assert 1062584 in videos

    table = team['table']
    assert 'entries' in table
    assert len(table['entries']) == 4
    assert table['entries'].keys() == {
        711,
        1758,
        713,
        1428,
    }
    assert [entry['rank'] for entry in table['entries'].values()] == [
        17,
        18,
        19,
        20,
    ]
    assert [
        entry['shortName'] for entry in table['entries'].values()
    ] == [
        'Parma',
        'Genoa',
        'Lecce',
        'Venedig',
    ]

    league = team['league']
    assert league['id'] == 700
    assert league['longName'] == 'Serie A'
    assert league['currentSeasonId'] == '2024/25'
    assert league['currentRoundId'] == 9
    assert league['table'] == 2
    assert league['sportId'] == 1
    assert league['imId'] == 700
    assert league['priority'] == 1


def test_barca(api: Api) -> None:
    team = api.my_team_sync(team=912)
    assert team['id'] == 912
    assert team['countryId'] == 'E'
    assert 4922675 in team['matches']

    match = team['matches'][4922675]
    assert match['approvalName'] == 'Live'
    assert match['timeConfirmed'] is True
    assert match['currentMinute'] == 60
    assert match['roundId'] == 11
    assert match['leagueLongName'] == 'La Liga'
    assert match['completed'] is False
    assert match['currentPeriod'] == Period.SECOND_HALF
    assert match['modifiedAt'] == datetype.fromisoformat(
        '2024-10-26T22:17:43'
    )
    assert match['currentDateTime'] == datetype.fromisoformat(
        '2024-10-26T22:19:12'
    )

    home_team = match['homeTeam']
    assert home_team['id'] == 908
    assert home_team['longName'] == 'Real Madrid'
    assert home_team['token'] == 'RMA'

    away_team = match['guestTeam']
    assert away_team['id'] == 912
    assert away_team['longName'] == 'FC Barcelona'
    assert away_team['token'] == 'BAR'

    assert match['results'] == MatchResults(
        hergAktuell=0,
        aergAktuell=2,
        hergHz=0,
        aergHz=0,
    )
