from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    path: Union[Unset, str] = UNSET,
    include_files: Union[Unset, bool] = False,
    allow_folders_without_trailing_slashes: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["path"] = path

    params["includeFiles"] = include_files

    params["allowFoldersWithoutTrailingSlashes"] = allow_folders_without_trailing_slashes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/filesystem",
        "params": params,
    }

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
    path: Union[Unset, str] = UNSET,
    include_files: Union[Unset, bool] = False,
    allow_folders_without_trailing_slashes: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        path (Union[Unset, str]):
        include_files (Union[Unset, bool]):  Default: False.
        allow_folders_without_trailing_slashes (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path=path,
        include_files=include_files,
        allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    path: Union[Unset, str] = UNSET,
    include_files: Union[Unset, bool] = False,
    allow_folders_without_trailing_slashes: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        path (Union[Unset, str]):
        include_files (Union[Unset, bool]):  Default: False.
        allow_folders_without_trailing_slashes (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path=path,
        include_files=include_files,
        allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
