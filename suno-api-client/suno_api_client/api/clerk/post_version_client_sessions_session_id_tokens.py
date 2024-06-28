from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_info import TokenInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    session_id: str,
    *,
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["_clerk_js_version"] = field_clerk_js_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/{version}/client/sessions/{session_id}/tokens",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TokenInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TokenInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TokenInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    session_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Response[TokenInfo]:
    """Get session token.

    Args:
        version (str):
        session_id (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenInfo]
    """

    kwargs = _get_kwargs(
        version=version,
        session_id=session_id,
        field_clerk_js_version=field_clerk_js_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    session_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Optional[TokenInfo]:
    """Get session token.

    Args:
        version (str):
        session_id (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenInfo
    """

    return sync_detailed(
        version=version,
        session_id=session_id,
        client=client,
        field_clerk_js_version=field_clerk_js_version,
    ).parsed


async def asyncio_detailed(
    version: str,
    session_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Response[TokenInfo]:
    """Get session token.

    Args:
        version (str):
        session_id (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenInfo]
    """

    kwargs = _get_kwargs(
        version=version,
        session_id=session_id,
        field_clerk_js_version=field_clerk_js_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    session_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_clerk_js_version: Union[Unset, str] = UNSET,
) -> Optional[TokenInfo]:
    """Get session token.

    Args:
        version (str):
        session_id (str):
        field_clerk_js_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenInfo
    """

    return (
        await asyncio_detailed(
            version=version,
            session_id=session_id,
            client=client,
            field_clerk_js_version=field_clerk_js_version,
        )
    ).parsed
