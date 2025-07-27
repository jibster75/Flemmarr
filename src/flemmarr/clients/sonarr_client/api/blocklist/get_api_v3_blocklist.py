from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from ...models.download_protocol import DownloadProtocol
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocols: Union[Unset, list[DownloadProtocol]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sortKey"] = sort_key

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_series_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(series_ids, Unset):
        json_series_ids = series_ids

    params["seriesIds"] = json_series_ids

    json_protocols: Union[Unset, list[str]] = UNSET
    if not isinstance(protocols, Unset):
        json_protocols = []
        for protocols_item_data in protocols:
            protocols_item = protocols_item_data.value
            json_protocols.append(protocols_item)

    params["protocols"] = json_protocols

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/blocklist",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BlocklistResourcePagingResource]:
    if response.status_code == 200:
        response_200 = BlocklistResourcePagingResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BlocklistResourcePagingResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocols: Union[Unset, list[DownloadProtocol]] = UNSET,
) -> Response[BlocklistResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        series_ids (Union[Unset, list[int]]):
        protocols (Union[Unset, list[DownloadProtocol]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocklistResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        series_ids=series_ids,
        protocols=protocols,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocols: Union[Unset, list[DownloadProtocol]] = UNSET,
) -> Optional[BlocklistResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        series_ids (Union[Unset, list[int]]):
        protocols (Union[Unset, list[DownloadProtocol]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocklistResourcePagingResource
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        series_ids=series_ids,
        protocols=protocols,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocols: Union[Unset, list[DownloadProtocol]] = UNSET,
) -> Response[BlocklistResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        series_ids (Union[Unset, list[int]]):
        protocols (Union[Unset, list[DownloadProtocol]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocklistResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        series_ids=series_ids,
        protocols=protocols,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocols: Union[Unset, list[DownloadProtocol]] = UNSET,
) -> Optional[BlocklistResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        series_ids (Union[Unset, list[int]]):
        protocols (Union[Unset, list[DownloadProtocol]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocklistResourcePagingResource
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            series_ids=series_ids,
            protocols=protocols,
        )
    ).parsed
