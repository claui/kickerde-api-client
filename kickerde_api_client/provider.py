"""Abstract HTTP response provider for testability."""

from abc import ABC, abstractmethod

import httpx

from .settings import DEFAULT_ENDPOINT_URL


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

    # Internally re-use a single HTTP client for all object instances
    # which do not bring their own
    _internal_client: httpx.AsyncClient | None = None

    _httpx_client: httpx.AsyncClient

    def __init__(
        self,
        http_client: httpx.AsyncClient | None = None,
        base_url: str = DEFAULT_ENDPOINT_URL,
    ):
        """
        :param http_client:
            An optional HTTP client to re-use.
            The default value is `None`, which means that an internal
            HTTP client will be used.

        :param base_url:
            The Kicker API endpoint to connect to.
            The default value is the public production endpoint.
        """
        self._base_url = base_url

        if (
            http_client is None
            and DefaultResponseProvider._internal_client is None
        ):
            DefaultResponseProvider._internal_client = (
                httpx.AsyncClient()
            )
        existing_client = (
            http_client or DefaultResponseProvider._internal_client
        )
        assert existing_client is not None
        self._httpx_client = existing_client

    async def get(self, path: str) -> str:
        response = await self._httpx_client.get(
            f'{self._base_url}/{path}',
            follow_redirects=False,
            headers={
                'Accept': 'application/xml',
                'Cache-Control': 'no-cache',
            },
        )
        response.raise_for_status()
        return response.text
