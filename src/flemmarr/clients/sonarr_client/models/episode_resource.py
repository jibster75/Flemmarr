import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.episode_file_resource import EpisodeFileResource
    from ..models.media_cover import MediaCover
    from ..models.series_resource import SeriesResource


T = TypeVar("T", bound="EpisodeResource")


@_attrs_define
class EpisodeResource:
    """
    Attributes:
        id (Union[Unset, int]):
        series_id (Union[Unset, int]):
        tvdb_id (Union[Unset, int]):
        episode_file_id (Union[Unset, int]):
        season_number (Union[Unset, int]):
        episode_number (Union[Unset, int]):
        title (Union[None, Unset, str]):
        air_date (Union[None, Unset, str]):
        air_date_utc (Union[None, Unset, datetime.datetime]):
        last_search_time (Union[None, Unset, datetime.datetime]):
        runtime (Union[Unset, int]):
        finale_type (Union[None, Unset, str]):
        overview (Union[None, Unset, str]):
        episode_file (Union[Unset, EpisodeFileResource]):
        has_file (Union[Unset, bool]):
        monitored (Union[Unset, bool]):
        absolute_episode_number (Union[None, Unset, int]):
        scene_absolute_episode_number (Union[None, Unset, int]):
        scene_episode_number (Union[None, Unset, int]):
        scene_season_number (Union[None, Unset, int]):
        unverified_scene_numbering (Union[Unset, bool]):
        end_time (Union[None, Unset, datetime.datetime]):
        grab_date (Union[None, Unset, datetime.datetime]):
        series (Union[Unset, SeriesResource]):
        images (Union[None, Unset, list['MediaCover']]):
    """

    id: Union[Unset, int] = UNSET
    series_id: Union[Unset, int] = UNSET
    tvdb_id: Union[Unset, int] = UNSET
    episode_file_id: Union[Unset, int] = UNSET
    season_number: Union[Unset, int] = UNSET
    episode_number: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    air_date: Union[None, Unset, str] = UNSET
    air_date_utc: Union[None, Unset, datetime.datetime] = UNSET
    last_search_time: Union[None, Unset, datetime.datetime] = UNSET
    runtime: Union[Unset, int] = UNSET
    finale_type: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    episode_file: Union[Unset, "EpisodeFileResource"] = UNSET
    has_file: Union[Unset, bool] = UNSET
    monitored: Union[Unset, bool] = UNSET
    absolute_episode_number: Union[None, Unset, int] = UNSET
    scene_absolute_episode_number: Union[None, Unset, int] = UNSET
    scene_episode_number: Union[None, Unset, int] = UNSET
    scene_season_number: Union[None, Unset, int] = UNSET
    unverified_scene_numbering: Union[Unset, bool] = UNSET
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    grab_date: Union[None, Unset, datetime.datetime] = UNSET
    series: Union[Unset, "SeriesResource"] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        series_id = self.series_id

        tvdb_id = self.tvdb_id

        episode_file_id = self.episode_file_id

        season_number = self.season_number

        episode_number = self.episode_number

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        air_date: Union[None, Unset, str]
        if isinstance(self.air_date, Unset):
            air_date = UNSET
        else:
            air_date = self.air_date

        air_date_utc: Union[None, Unset, str]
        if isinstance(self.air_date_utc, Unset):
            air_date_utc = UNSET
        elif isinstance(self.air_date_utc, datetime.datetime):
            air_date_utc = self.air_date_utc.isoformat()
        else:
            air_date_utc = self.air_date_utc

        last_search_time: Union[None, Unset, str]
        if isinstance(self.last_search_time, Unset):
            last_search_time = UNSET
        elif isinstance(self.last_search_time, datetime.datetime):
            last_search_time = self.last_search_time.isoformat()
        else:
            last_search_time = self.last_search_time

        runtime = self.runtime

        finale_type: Union[None, Unset, str]
        if isinstance(self.finale_type, Unset):
            finale_type = UNSET
        else:
            finale_type = self.finale_type

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        episode_file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.episode_file, Unset):
            episode_file = self.episode_file.to_dict()

        has_file = self.has_file

        monitored = self.monitored

        absolute_episode_number: Union[None, Unset, int]
        if isinstance(self.absolute_episode_number, Unset):
            absolute_episode_number = UNSET
        else:
            absolute_episode_number = self.absolute_episode_number

        scene_absolute_episode_number: Union[None, Unset, int]
        if isinstance(self.scene_absolute_episode_number, Unset):
            scene_absolute_episode_number = UNSET
        else:
            scene_absolute_episode_number = self.scene_absolute_episode_number

        scene_episode_number: Union[None, Unset, int]
        if isinstance(self.scene_episode_number, Unset):
            scene_episode_number = UNSET
        else:
            scene_episode_number = self.scene_episode_number

        scene_season_number: Union[None, Unset, int]
        if isinstance(self.scene_season_number, Unset):
            scene_season_number = UNSET
        else:
            scene_season_number = self.scene_season_number

        unverified_scene_numbering = self.unverified_scene_numbering

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        grab_date: Union[None, Unset, str]
        if isinstance(self.grab_date, Unset):
            grab_date = UNSET
        elif isinstance(self.grab_date, datetime.datetime):
            grab_date = self.grab_date.isoformat()
        else:
            grab_date = self.grab_date

        series: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        images: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if series_id is not UNSET:
            field_dict["seriesId"] = series_id
        if tvdb_id is not UNSET:
            field_dict["tvdbId"] = tvdb_id
        if episode_file_id is not UNSET:
            field_dict["episodeFileId"] = episode_file_id
        if season_number is not UNSET:
            field_dict["seasonNumber"] = season_number
        if episode_number is not UNSET:
            field_dict["episodeNumber"] = episode_number
        if title is not UNSET:
            field_dict["title"] = title
        if air_date is not UNSET:
            field_dict["airDate"] = air_date
        if air_date_utc is not UNSET:
            field_dict["airDateUtc"] = air_date_utc
        if last_search_time is not UNSET:
            field_dict["lastSearchTime"] = last_search_time
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if finale_type is not UNSET:
            field_dict["finaleType"] = finale_type
        if overview is not UNSET:
            field_dict["overview"] = overview
        if episode_file is not UNSET:
            field_dict["episodeFile"] = episode_file
        if has_file is not UNSET:
            field_dict["hasFile"] = has_file
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if absolute_episode_number is not UNSET:
            field_dict["absoluteEpisodeNumber"] = absolute_episode_number
        if scene_absolute_episode_number is not UNSET:
            field_dict["sceneAbsoluteEpisodeNumber"] = scene_absolute_episode_number
        if scene_episode_number is not UNSET:
            field_dict["sceneEpisodeNumber"] = scene_episode_number
        if scene_season_number is not UNSET:
            field_dict["sceneSeasonNumber"] = scene_season_number
        if unverified_scene_numbering is not UNSET:
            field_dict["unverifiedSceneNumbering"] = unverified_scene_numbering
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if grab_date is not UNSET:
            field_dict["grabDate"] = grab_date
        if series is not UNSET:
            field_dict["series"] = series
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.episode_file_resource import EpisodeFileResource
        from ..models.media_cover import MediaCover
        from ..models.series_resource import SeriesResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        series_id = d.pop("seriesId", UNSET)

        tvdb_id = d.pop("tvdbId", UNSET)

        episode_file_id = d.pop("episodeFileId", UNSET)

        season_number = d.pop("seasonNumber", UNSET)

        episode_number = d.pop("episodeNumber", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_air_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        air_date = _parse_air_date(d.pop("airDate", UNSET))

        def _parse_air_date_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                air_date_utc_type_0 = isoparse(data)

                return air_date_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        air_date_utc = _parse_air_date_utc(d.pop("airDateUtc", UNSET))

        def _parse_last_search_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_search_time_type_0 = isoparse(data)

                return last_search_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_search_time = _parse_last_search_time(d.pop("lastSearchTime", UNSET))

        runtime = d.pop("runtime", UNSET)

        def _parse_finale_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        finale_type = _parse_finale_type(d.pop("finaleType", UNSET))

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("overview", UNSET))

        _episode_file = d.pop("episodeFile", UNSET)
        episode_file: Union[Unset, EpisodeFileResource]
        if isinstance(_episode_file, Unset):
            episode_file = UNSET
        else:
            episode_file = EpisodeFileResource.from_dict(_episode_file)

        has_file = d.pop("hasFile", UNSET)

        monitored = d.pop("monitored", UNSET)

        def _parse_absolute_episode_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        absolute_episode_number = _parse_absolute_episode_number(d.pop("absoluteEpisodeNumber", UNSET))

        def _parse_scene_absolute_episode_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scene_absolute_episode_number = _parse_scene_absolute_episode_number(d.pop("sceneAbsoluteEpisodeNumber", UNSET))

        def _parse_scene_episode_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scene_episode_number = _parse_scene_episode_number(d.pop("sceneEpisodeNumber", UNSET))

        def _parse_scene_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scene_season_number = _parse_scene_season_number(d.pop("sceneSeasonNumber", UNSET))

        unverified_scene_numbering = d.pop("unverifiedSceneNumbering", UNSET)

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_grab_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grab_date_type_0 = isoparse(data)

                return grab_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        grab_date = _parse_grab_date(d.pop("grabDate", UNSET))

        _series = d.pop("series", UNSET)
        series: Union[Unset, SeriesResource]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = SeriesResource.from_dict(_series)

        def _parse_images(data: object) -> Union[None, Unset, list["MediaCover"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = MediaCover.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediaCover"]], data)

        images = _parse_images(d.pop("images", UNSET))

        episode_resource = cls(
            id=id,
            series_id=series_id,
            tvdb_id=tvdb_id,
            episode_file_id=episode_file_id,
            season_number=season_number,
            episode_number=episode_number,
            title=title,
            air_date=air_date,
            air_date_utc=air_date_utc,
            last_search_time=last_search_time,
            runtime=runtime,
            finale_type=finale_type,
            overview=overview,
            episode_file=episode_file,
            has_file=has_file,
            monitored=monitored,
            absolute_episode_number=absolute_episode_number,
            scene_absolute_episode_number=scene_absolute_episode_number,
            scene_episode_number=scene_episode_number,
            scene_season_number=scene_season_number,
            unverified_scene_numbering=unverified_scene_numbering,
            end_time=end_time,
            grab_date=grab_date,
            series=series,
            images=images,
        )

        return episode_resource
