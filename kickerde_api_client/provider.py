"""Abstract HTTP response provider for testability."""

from abc import ABC, abstractmethod

import requests

from .settings import DEFAULT_ENDPOINT_URL, REQUEST_TIMEOUT_SEC


class ResponseProvider(ABC):  # pylint: disable=too-few-public-methods
    """Abstract HTTP response provider for testability."""

    @abstractmethod
    async def get(self, path: str) -> str:
        """Returns an HTTP response as a string.

        :param path:
            Relative path to the endpoint

        :return:
            HTTP response payload
        """


class DefaultResponseProvider(ResponseProvider):  # pylint: disable=too-few-public-methods
    """The default provider, which issues actual HTTP requests."""

    def __init__(self, base_url: str = DEFAULT_ENDPOINT_URL):
        """
        :param base_url:
            The Kicker API endpoint to connect to.
            The default value is the public production endpoint.
        """
        self._base_url = base_url

    async def get(self, path: str) -> str:
        response = requests.get(
            f'{self._base_url}/{path}',
            timeout=REQUEST_TIMEOUT_SEC,
        )
        response.raise_for_status()
        return response.text
