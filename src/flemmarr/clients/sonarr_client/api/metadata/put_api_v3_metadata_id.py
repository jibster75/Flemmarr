from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_resource import MetadataResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: MetadataResource,
    force_save: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["forceSave"] = force_save

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v3/metadata/{id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MetadataResource]:
    if response.status_code == 200:
        response_200 = MetadataResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MetadataResource]:
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
    body: MetadataResource,
    force_save: Union[Unset, bool] = False,
) -> Response[MetadataResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (MetadataResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataResource]
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
    body: MetadataResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[MetadataResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (MetadataResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataResource
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
    body: MetadataResource,
    force_save: Union[Unset, bool] = False,
) -> Response[MetadataResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (MetadataResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataResource]
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
    body: MetadataResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[MetadataResource]:
    """
    Args:
        id (int):
        force_save (Union[Unset, bool]):  Default: False.
        body (MetadataResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataResource
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            force_save=force_save,
        )
    ).parsed
