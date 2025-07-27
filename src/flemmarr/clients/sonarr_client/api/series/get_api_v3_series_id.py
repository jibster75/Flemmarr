from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.series_resource import SeriesResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    include_season_images: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeSeasonImages"] = include_season_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v3/series/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SeriesResource]:
    if response.status_code == 200:
        response_200 = SeriesResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SeriesResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_season_images: Union[Unset, bool] = False,
) -> Response[SeriesResource]:
    """
    Args:
        id (int):
        include_season_images (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeriesResource]
    """

    kwargs = _get_kwargs(
        id=id,
        include_season_images=include_season_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_season_images: Union[Unset, bool] = False,
) -> Optional[SeriesResource]:
    """
    Args:
        id (int):
        include_season_images (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeriesResource
    """

    return sync_detailed(
        id=id,
        client=client,
        include_season_images=include_season_images,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_season_images: Union[Unset, bool] = False,
) -> Response[SeriesResource]:
    """
    Args:
        id (int):
        include_season_images (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeriesResource]
    """

    kwargs = _get_kwargs(
        id=id,
        include_season_images=include_season_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_season_images: Union[Unset, bool] = False,
) -> Optional[SeriesResource]:
    """
    Args:
        id (int):
        include_season_images (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeriesResource
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_season_images=include_season_images,
        )
    ).parsed
