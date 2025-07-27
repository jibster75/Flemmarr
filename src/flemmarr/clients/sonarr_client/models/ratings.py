from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ratings")


@_attrs_define
class Ratings:
    """
    Attributes:
        votes (Union[Unset, int]):
        value (Union[Unset, float]):
    """

    votes: Union[Unset, int] = UNSET
    value: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        votes = self.votes

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if votes is not UNSET:
            field_dict["votes"] = votes
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        votes = d.pop("votes", UNSET)

        value = d.pop("value", UNSET)

        ratings = cls(
            votes=votes,
            value=value,
        )

        return ratings
