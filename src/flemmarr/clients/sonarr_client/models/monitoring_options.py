from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.monitor_types import MonitorTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringOptions")


@_attrs_define
class MonitoringOptions:
    """
    Attributes:
        ignore_episodes_with_files (Union[Unset, bool]):
        ignore_episodes_without_files (Union[Unset, bool]):
        monitor (Union[Unset, MonitorTypes]):
    """

    ignore_episodes_with_files: Union[Unset, bool] = UNSET
    ignore_episodes_without_files: Union[Unset, bool] = UNSET
    monitor: Union[Unset, MonitorTypes] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ignore_episodes_with_files = self.ignore_episodes_with_files

        ignore_episodes_without_files = self.ignore_episodes_without_files

        monitor: Union[Unset, str] = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ignore_episodes_with_files is not UNSET:
            field_dict["ignoreEpisodesWithFiles"] = ignore_episodes_with_files
        if ignore_episodes_without_files is not UNSET:
            field_dict["ignoreEpisodesWithoutFiles"] = ignore_episodes_without_files
        if monitor is not UNSET:
            field_dict["monitor"] = monitor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_episodes_with_files = d.pop("ignoreEpisodesWithFiles", UNSET)

        ignore_episodes_without_files = d.pop("ignoreEpisodesWithoutFiles", UNSET)

        _monitor = d.pop("monitor", UNSET)
        monitor: Union[Unset, MonitorTypes]
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = MonitorTypes(_monitor)

        monitoring_options = cls(
            ignore_episodes_with_files=ignore_episodes_with_files,
            ignore_episodes_without_files=ignore_episodes_without_files,
            monitor=monitor,
        )

        return monitoring_options
