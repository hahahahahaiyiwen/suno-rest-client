from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_result import ClientResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    *,
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["_clerk_js_version"] = field_clerk_js_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{version}/client",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ClientResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClientResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ClientResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Response[ClientResult]:
    """Get sessions.

    Args:
        version (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientResult]
    """

    kwargs = _get_kwargs(
        version=version,
        field_clerk_js_version=field_clerk_js_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Optional[ClientResult]:
    """Get sessions.

    Args:
        version (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientResult
    """

    return sync_detailed(
        version=version,
        client=client,
        field_clerk_js_version=field_clerk_js_version,
    ).parsed


async def asyncio_detailed(
    version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Response[ClientResult]:
    """Get sessions.

    Args:
        version (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientResult]
    """

    kwargs = _get_kwargs(
        version=version,
        field_clerk_js_version=field_clerk_js_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Optional[ClientResult]:
    """Get sessions.

    Args:
        version (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientResult
    """

    return (
        await asyncio_detailed(
            version=version,
            client=client,
            field_clerk_js_version=field_clerk_js_version,
        )
    ).parsed
