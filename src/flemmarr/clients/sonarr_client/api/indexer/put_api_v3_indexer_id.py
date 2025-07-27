from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.indexer_resource import IndexerResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: IndexerResource,
    force_save: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["forceSave"] = force_save

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v3/indexer/{id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IndexerResource]:
    if response.status_code == 200:
        response_200 = IndexerResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IndexerResource]:
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
    body: IndexerResource,
    force_save: Union[Unset, bool] = False,
) -> Response[IndexerResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (IndexerResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexerResource]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        force_save=force_save,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexerResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[IndexerResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (IndexerResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexerResource
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        force_save=force_save,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexerResource,
    force_save: Union[Unset, bool] = False,
) -> Response[IndexerResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (IndexerResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexerResource]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        force_save=force_save,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexerResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[IndexerResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (IndexerResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexerResource
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            force_save=force_save,
        )
    ).parsed
