from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Revision")


@_attrs_define
class Revision:
    """
    Attributes:
        version (Union[Unset, int]):
        real (Union[Unset, int]):
        is_repack (Union[Unset, bool]):
    """

    version: Union[Unset, int] = UNSET
    real: Union[Unset, int] = UNSET
    is_repack: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        real = self.real

        is_repack = self.is_repack

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if real is not UNSET:
            field_dict["real"] = real
        if is_repack is not UNSET:
            field_dict["isRepack"] = is_repack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        real = d.pop("real", UNSET)

        is_repack = d.pop("isRepack", UNSET)

        revision = cls(
            version=version,
            real=real,
            is_repack=is_repack,
        )

        return revision
