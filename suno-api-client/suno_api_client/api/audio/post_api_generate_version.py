from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audio_generation_request import AudioGenerationRequest
from ...models.audio_result import AudioResult
from ...types import Response


def _get_kwargs(
    version: str = "v2",
    *,
    body: AudioGenerationRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/generate/{version}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AudioResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AudioResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AudioResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str = "v2",
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioGenerationRequest,
) -> Response[AudioResult]:
    """Generate audio based on Prompt.

    Args:
        version (str):  Default: 'v2'.
        body (AudioGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AudioResult]
    """

    kwargs = _get_kwargs(
        version=version,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str = "v2",
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioGenerationRequest,
) -> Optional[AudioResult]:
    """Generate audio based on Prompt.

    Args:
        version (str):  Default: 'v2'.
        body (AudioGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AudioResult
    """

    return sync_detailed(
        version=version,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    version: str = "v2",
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioGenerationRequest,
) -> Response[AudioResult]:
    """Generate audio based on Prompt.

    Args:
        version (str):  Default: 'v2'.
        body (AudioGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AudioResult]
    """

    kwargs = _get_kwargs(
        version=version,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str = "v2",
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioGenerationRequest,
) -> Optional[AudioResult]:
    """Generate audio based on Prompt.

    Args:
        version (str):  Default: 'v2'.
        body (AudioGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AudioResult
    """

    return (
        await asyncio_detailed(
            version=version,
            client=client,
            body=body,
        )
    ).parsed
