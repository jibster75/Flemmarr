from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.queue_bulk_resource import QueueBulkResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        QueueBulkResource,
        QueueBulkResource,
    ],
    remove_from_client: Union[Unset, bool] = True,
    blocklist: Union[Unset, bool] = False,
    skip_redownload: Union[Unset, bool] = False,
    change_category: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["removeFromClient"] = remove_from_client

    params["blocklist"] = blocklist

    params["skipRedownload"] = skip_redownload

    params["changeCategory"] = change_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v3/queue/bulk",
        "params": params,
    }

    if isinstance(body, QueueBulkResource):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, QueueBulkResource):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QueueBulkResource,
        QueueBulkResource,
    ],
    remove_from_client: Union[Unset, bool] = True,
    blocklist: Union[Unset, bool] = False,
    skip_redownload: Union[Unset, bool] = False,
    change_category: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        remove_from_client (Union[Unset, bool]):  Default: True.
        blocklist (Union[Unset, bool]):  Default: False.
        skip_redownload (Union[Unset, bool]):  Default: False.
        change_category (Union[Unset, bool]):  Default: False.
        body (QueueBulkResource):
        body (QueueBulkResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        remove_from_client=remove_from_client,
        blocklist=blocklist,
        skip_redownload=skip_redownload,
        change_category=change_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QueueBulkResource,
        QueueBulkResource,
    ],
    remove_from_client: Union[Unset, bool] = True,
    blocklist: Union[Unset, bool] = False,
    skip_redownload: Union[Unset, bool] = False,
    change_category: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        remove_from_client (Union[Unset, bool]):  Default: True.
        blocklist (Union[Unset, bool]):  Default: False.
        skip_redownload (Union[Unset, bool]):  Default: False.
        change_category (Union[Unset, bool]):  Default: False.
        body (QueueBulkResource):
        body (QueueBulkResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        remove_from_client=remove_from_client,
        blocklist=blocklist,
        skip_redownload=skip_redownload,
        change_category=change_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
