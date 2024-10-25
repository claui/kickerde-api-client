"""
Unofficial client for the public kicker.de news API

To install this library from PyPI, open a shell and run:

.. code:: shell

   pip install kickerde-api-client
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
