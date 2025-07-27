from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagDetailsResource")


@_attrs_define
class TagDetailsResource:
    """
    Attributes:
        id (Union[Unset, int]):
        label (Union[None, Unset, str]):
        delay_profile_ids (Union[None, Unset, list[int]]):
        import_list_ids (Union[None, Unset, list[int]]):
        notification_ids (Union[None, Unset, list[int]]):
        restriction_ids (Union[None, Unset, list[int]]):
        indexer_ids (Union[None, Unset, list[int]]):
        download_client_ids (Union[None, Unset, list[int]]):
        auto_tag_ids (Union[None, Unset, list[int]]):
        series_ids (Union[None, Unset, list[int]]):
    """

    id: Union[Unset, int] = UNSET
    label: Union[None, Unset, str] = UNSET
    delay_profile_ids: Union[None, Unset, list[int]] = UNSET
    import_list_ids: Union[None, Unset, list[int]] = UNSET
    notification_ids: Union[None, Unset, list[int]] = UNSET
    restriction_ids: Union[None, Unset, list[int]] = UNSET
    indexer_ids: Union[None, Unset, list[int]] = UNSET
    download_client_ids: Union[None, Unset, list[int]] = UNSET
    auto_tag_ids: Union[None, Unset, list[int]] = UNSET
    series_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        delay_profile_ids: Union[None, Unset, list[int]]
        if isinstance(self.delay_profile_ids, Unset):
            delay_profile_ids = UNSET
        elif isinstance(self.delay_profile_ids, list):
            delay_profile_ids = self.delay_profile_ids

        else:
            delay_profile_ids = self.delay_profile_ids

        import_list_ids: Union[None, Unset, list[int]]
        if isinstance(self.import_list_ids, Unset):
            import_list_ids = UNSET
        elif isinstance(self.import_list_ids, list):
            import_list_ids = self.import_list_ids

        else:
            import_list_ids = self.import_list_ids

        notification_ids: Union[None, Unset, list[int]]
        if isinstance(self.notification_ids, Unset):
            notification_ids = UNSET
        elif isinstance(self.notification_ids, list):
            notification_ids = self.notification_ids

        else:
            notification_ids = self.notification_ids

        restriction_ids: Union[None, Unset, list[int]]
        if isinstance(self.restriction_ids, Unset):
            restriction_ids = UNSET
        elif isinstance(self.restriction_ids, list):
            restriction_ids = self.restriction_ids

        else:
            restriction_ids = self.restriction_ids

        indexer_ids: Union[None, Unset, list[int]]
        if isinstance(self.indexer_ids, Unset):
            indexer_ids = UNSET
        elif isinstance(self.indexer_ids, list):
            indexer_ids = self.indexer_ids

        else:
            indexer_ids = self.indexer_ids

        download_client_ids: Union[None, Unset, list[int]]
        if isinstance(self.download_client_ids, Unset):
            download_client_ids = UNSET
        elif isinstance(self.download_client_ids, list):
            download_client_ids = self.download_client_ids

        else:
            download_client_ids = self.download_client_ids

        auto_tag_ids: Union[None, Unset, list[int]]
        if isinstance(self.auto_tag_ids, Unset):
            auto_tag_ids = UNSET
        elif isinstance(self.auto_tag_ids, list):
            auto_tag_ids = self.auto_tag_ids

        else:
            auto_tag_ids = self.auto_tag_ids

        series_ids: Union[None, Unset, list[int]]
        if isinstance(self.series_ids, Unset):
            series_ids = UNSET
        elif isinstance(self.series_ids, list):
            series_ids = self.series_ids

        else:
            series_ids = self.series_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if delay_profile_ids is not UNSET:
            field_dict["delayProfileIds"] = delay_profile_ids
        if import_list_ids is not UNSET:
            field_dict["importListIds"] = import_list_ids
        if notification_ids is not UNSET:
            field_dict["notificationIds"] = notification_ids
        if restriction_ids is not UNSET:
            field_dict["restrictionIds"] = restriction_ids
        if indexer_ids is not UNSET:
            field_dict["indexerIds"] = indexer_ids
        if download_client_ids is not UNSET:
            field_dict["downloadClientIds"] = download_client_ids
        if auto_tag_ids is not UNSET:
            field_dict["autoTagIds"] = auto_tag_ids
        if series_ids is not UNSET:
            field_dict["seriesIds"] = series_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_delay_profile_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                delay_profile_ids_type_0 = cast(list[int], data)

                return delay_profile_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        delay_profile_ids = _parse_delay_profile_ids(d.pop("delayProfileIds", UNSET))

        def _parse_import_list_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                import_list_ids_type_0 = cast(list[int], data)

                return import_list_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        import_list_ids = _parse_import_list_ids(d.pop("importListIds", UNSET))

        def _parse_notification_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_ids_type_0 = cast(list[int], data)

                return notification_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        notification_ids = _parse_notification_ids(d.pop("notificationIds", UNSET))

        def _parse_restriction_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restriction_ids_type_0 = cast(list[int], data)

                return restriction_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        restriction_ids = _parse_restriction_ids(d.pop("restrictionIds", UNSET))

        def _parse_indexer_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexer_ids_type_0 = cast(list[int], data)

                return indexer_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        indexer_ids = _parse_indexer_ids(d.pop("indexerIds", UNSET))

        def _parse_download_client_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                download_client_ids_type_0 = cast(list[int], data)

                return download_client_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        download_client_ids = _parse_download_client_ids(d.pop("downloadClientIds", UNSET))

        def _parse_auto_tag_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auto_tag_ids_type_0 = cast(list[int], data)

                return auto_tag_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        auto_tag_ids = _parse_auto_tag_ids(d.pop("autoTagIds", UNSET))

        def _parse_series_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_ids_type_0 = cast(list[int], data)

                return series_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        series_ids = _parse_series_ids(d.pop("seriesIds", UNSET))

        tag_details_resource = cls(
            id=id,
            label=label,
            delay_profile_ids=delay_profile_ids,
            import_list_ids=import_list_ids,
            notification_ids=notification_ids,
            restriction_ids=restriction_ids,
            indexer_ids=indexer_ids,
            download_client_ids=download_client_ids,
            auto_tag_ids=auto_tag_ids,
            series_ids=series_ids,
        )

        return tag_details_resource
