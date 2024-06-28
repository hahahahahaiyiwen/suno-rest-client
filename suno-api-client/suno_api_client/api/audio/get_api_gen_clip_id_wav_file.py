from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wav_info import WavInfo
from ...types import Response


def _get_kwargs(
    clip_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/gen/{clip_id}/wav_file/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WavInfo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WavInfo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, WavInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clip_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, WavInfo]]:
    """Get audio clip in wav format.

    Args:
        clip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WavInfo]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clip_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, WavInfo]]:
    """Get audio clip in wav format.

    Args:
        clip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WavInfo]
    """

    return sync_detailed(
        clip_id=clip_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clip_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, WavInfo]]:
    """Get audio clip in wav format.

    Args:
        clip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WavInfo]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clip_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, WavInfo]]:
    """Get audio clip in wav format.

    Args:
        clip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WavInfo]
    """

    return (
        await asyncio_detailed(
            clip_id=clip_id,
            client=client,
        )
    ).parsed
