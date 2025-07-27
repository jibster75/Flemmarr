import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.download_protocol import DownloadProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.language import Language
    from ..models.quality_model import QualityModel
    from ..models.series_resource import SeriesResource


T = TypeVar("T", bound="BlocklistResource")


@_attrs_define
class BlocklistResource:
    """
    Attributes:
        id (Union[Unset, int]):
        series_id (Union[Unset, int]):
        episode_ids (Union[None, Unset, list[int]]):
        source_title (Union[None, Unset, str]):
        languages (Union[None, Unset, list['Language']]):
        quality (Union[Unset, QualityModel]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        date (Union[Unset, datetime.datetime]):
        protocol (Union[Unset, DownloadProtocol]):
        indexer (Union[None, Unset, str]):
        message (Union[None, Unset, str]):
        series (Union[Unset, SeriesResource]):
    """

    id: Union[Unset, int] = UNSET
    series_id: Union[Unset, int] = UNSET
    episode_ids: Union[None, Unset, list[int]] = UNSET
    source_title: Union[None, Unset, str] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    protocol: Union[Unset, DownloadProtocol] = UNSET
    indexer: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, str] = UNSET
    series: Union[Unset, "SeriesResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        series_id = self.series_id

        episode_ids: Union[None, Unset, list[int]]
        if isinstance(self.episode_ids, Unset):
            episode_ids = UNSET
        elif isinstance(self.episode_ids, list):
            episode_ids = self.episode_ids

        else:
            episode_ids = self.episode_ids

        source_title: Union[None, Unset, str]
        if isinstance(self.source_title, Unset):
            source_title = UNSET
        else:
            source_title = self.source_title

        languages: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item = languages_type_0_item_data.to_dict()
                languages.append(languages_type_0_item)

        else:
            languages = self.languages

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        custom_formats: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_formats, Unset):
            custom_formats = UNSET
        elif isinstance(self.custom_formats, list):
            custom_formats = []
            for custom_formats_type_0_item_data in self.custom_formats:
                custom_formats_type_0_item = custom_formats_type_0_item_data.to_dict()
                custom_formats.append(custom_formats_type_0_item)

        else:
            custom_formats = self.custom_formats

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        indexer: Union[None, Unset, str]
        if isinstance(self.indexer, Unset):
            indexer = UNSET
        else:
            indexer = self.indexer

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        series: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if series_id is not UNSET:
            field_dict["seriesId"] = series_id
        if episode_ids is not UNSET:
            field_dict["episodeIds"] = episode_ids
        if source_title is not UNSET:
            field_dict["sourceTitle"] = source_title
        if languages is not UNSET:
            field_dict["languages"] = languages
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if date is not UNSET:
            field_dict["date"] = date
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if indexer is not UNSET:
            field_dict["indexer"] = indexer
        if message is not UNSET:
            field_dict["message"] = message
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.language import Language
        from ..models.quality_model import QualityModel
        from ..models.series_resource import SeriesResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        series_id = d.pop("seriesId", UNSET)

        def _parse_episode_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                episode_ids_type_0 = cast(list[int], data)

                return episode_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        episode_ids = _parse_episode_ids(d.pop("episodeIds", UNSET))

        def _parse_source_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_title = _parse_source_title(d.pop("sourceTitle", UNSET))

        def _parse_languages(data: object) -> Union[None, Unset, list["Language"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = Language.from_dict(languages_type_0_item_data)

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Language"]], data)

        languages = _parse_languages(d.pop("languages", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_custom_formats(data: object) -> Union[None, Unset, list["CustomFormatResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_formats_type_0 = []
                _custom_formats_type_0 = data
                for custom_formats_type_0_item_data in _custom_formats_type_0:
                    custom_formats_type_0_item = CustomFormatResource.from_dict(custom_formats_type_0_item_data)

                    custom_formats_type_0.append(custom_formats_type_0_item)

                return custom_formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CustomFormatResource"]], data)

        custom_formats = _parse_custom_formats(d.pop("customFormats", UNSET))

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, DownloadProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = DownloadProtocol(_protocol)

        def _parse_indexer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        indexer = _parse_indexer(d.pop("indexer", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        _series = d.pop("series", UNSET)
        series: Union[Unset, SeriesResource]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = SeriesResource.from_dict(_series)

        blocklist_resource = cls(
            id=id,
            series_id=series_id,
            episode_ids=episode_ids,
            source_title=source_title,
            languages=languages,
            quality=quality,
            custom_formats=custom_formats,
            date=date,
            protocol=protocol,
            indexer=indexer,
            message=message,
            series=series,
        )

        return blocklist_resource
