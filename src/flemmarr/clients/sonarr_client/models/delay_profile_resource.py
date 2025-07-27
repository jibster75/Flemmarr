from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.download_protocol import DownloadProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="DelayProfileResource")


@_attrs_define
class DelayProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        enable_usenet (Union[Unset, bool]):
        enable_torrent (Union[Unset, bool]):
        preferred_protocol (Union[Unset, DownloadProtocol]):
        usenet_delay (Union[Unset, int]):
        torrent_delay (Union[Unset, int]):
        bypass_if_highest_quality (Union[Unset, bool]):
        bypass_if_above_custom_format_score (Union[Unset, bool]):
        minimum_custom_format_score (Union[Unset, int]):
        order (Union[Unset, int]):
        tags (Union[None, Unset, list[int]]):
    """

    id: Union[Unset, int] = UNSET
    enable_usenet: Union[Unset, bool] = UNSET
    enable_torrent: Union[Unset, bool] = UNSET
    preferred_protocol: Union[Unset, DownloadProtocol] = UNSET
    usenet_delay: Union[Unset, int] = UNSET
    torrent_delay: Union[Unset, int] = UNSET
    bypass_if_highest_quality: Union[Unset, bool] = UNSET
    bypass_if_above_custom_format_score: Union[Unset, bool] = UNSET
    minimum_custom_format_score: Union[Unset, int] = UNSET
    order: Union[Unset, int] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enable_usenet = self.enable_usenet

        enable_torrent = self.enable_torrent

        preferred_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.preferred_protocol, Unset):
            preferred_protocol = self.preferred_protocol.value

        usenet_delay = self.usenet_delay

        torrent_delay = self.torrent_delay

        bypass_if_highest_quality = self.bypass_if_highest_quality

        bypass_if_above_custom_format_score = self.bypass_if_above_custom_format_score

        minimum_custom_format_score = self.minimum_custom_format_score

        order = self.order

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enable_usenet is not UNSET:
            field_dict["enableUsenet"] = enable_usenet
        if enable_torrent is not UNSET:
            field_dict["enableTorrent"] = enable_torrent
        if preferred_protocol is not UNSET:
            field_dict["preferredProtocol"] = preferred_protocol
        if usenet_delay is not UNSET:
            field_dict["usenetDelay"] = usenet_delay
        if torrent_delay is not UNSET:
            field_dict["torrentDelay"] = torrent_delay
        if bypass_if_highest_quality is not UNSET:
            field_dict["bypassIfHighestQuality"] = bypass_if_highest_quality
        if bypass_if_above_custom_format_score is not UNSET:
            field_dict["bypassIfAboveCustomFormatScore"] = bypass_if_above_custom_format_score
        if minimum_custom_format_score is not UNSET:
            field_dict["minimumCustomFormatScore"] = minimum_custom_format_score
        if order is not UNSET:
            field_dict["order"] = order
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        enable_usenet = d.pop("enableUsenet", UNSET)

        enable_torrent = d.pop("enableTorrent", UNSET)

        _preferred_protocol = d.pop("preferredProtocol", UNSET)
        preferred_protocol: Union[Unset, DownloadProtocol]
        if isinstance(_preferred_protocol, Unset):
            preferred_protocol = UNSET
        else:
            preferred_protocol = DownloadProtocol(_preferred_protocol)

        usenet_delay = d.pop("usenetDelay", UNSET)

        torrent_delay = d.pop("torrentDelay", UNSET)

        bypass_if_highest_quality = d.pop("bypassIfHighestQuality", UNSET)

        bypass_if_above_custom_format_score = d.pop("bypassIfAboveCustomFormatScore", UNSET)

        minimum_custom_format_score = d.pop("minimumCustomFormatScore", UNSET)

        order = d.pop("order", UNSET)

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        delay_profile_resource = cls(
            id=id,
            enable_usenet=enable_usenet,
            enable_torrent=enable_torrent,
            preferred_protocol=preferred_protocol,
            usenet_delay=usenet_delay,
            torrent_delay=torrent_delay,
            bypass_if_highest_quality=bypass_if_highest_quality,
            bypass_if_above_custom_format_score=bypass_if_above_custom_format_score,
            minimum_custom_format_score=minimum_custom_format_score,
            order=order,
            tags=tags,
        )

        return delay_profile_resource
