"""
Demo code to get started:

.. code:: python

   import asyncio
   from kickerde_api_client import Api
   from kickerde_api_client.model import LeagueId

   api = Api()
   query = {'league': LeagueId.BUNDESLIGA, 'season': '2024/25'}
   season = asyncio.run(api.league_season(**query))

   print(season['longName'])             # 'Bundesliga'
   print(season['country']['longName'])  # 'Deutschland'

   print([
       team['shortName']
       for team in season['teams'].values()
       if team['shortName'].startswith('B')
   ])                                    # ['Bayern', 'Bremen', 'Bochum']

   day = season['gamedays'][34]
   print(str(day['dateFrom'].date()))    # '2025-05-17'
"""

# Re-export these symbols
# (This promotes them from kickerde_api_client.api to kickerde_api_client)
from kickerde_api_client.api import Api as Api

from kickerde_api_client.version import version

__all__ = [
    # Modules that every subpackage should see
    'settings',
]

__version__ = version()
