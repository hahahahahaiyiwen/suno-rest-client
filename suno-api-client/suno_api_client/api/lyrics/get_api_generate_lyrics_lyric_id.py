from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lyrics_result import LyricsResult
from ...types import Response


def _get_kwargs(
    lyric_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/generate/lyrics/{lyric_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[LyricsResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LyricsResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[LyricsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lyric_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[LyricsResult]:
    """Get generated lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LyricsResult]
    """

    kwargs = _get_kwargs(
        lyric_id=lyric_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lyric_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[LyricsResult]:
    """Get generated lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LyricsResult
    """

    return sync_detailed(
        lyric_id=lyric_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    lyric_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[LyricsResult]:
    """Get generated lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LyricsResult]
    """

    kwargs = _get_kwargs(
        lyric_id=lyric_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lyric_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[LyricsResult]:
    """Get generated lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LyricsResult
    """

    return (
        await asyncio_detailed(
            lyric_id=lyric_id,
            client=client,
        )
    ).parsed
