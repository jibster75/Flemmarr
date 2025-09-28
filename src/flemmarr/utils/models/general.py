from dataclasses import dataclass
from typing import Any, Optional
from types import ModuleType
from typing import get_type_hints, get_origin, get_args

from flemmarr.utils.enum import Strategy


@dataclass
class OpenApiModelResource:
    resource: Optional[object | Any] = None
    name: Optional[str] = ""

    # if we resolve the api, then this object is usable
    def __bool__(self) -> bool:
        return bool(self.resource)

    def __repr__(self) -> str:
        if not self.name or not self.resource:
            return "Empty"
        return self.name

    def _add_short_name_for_resource(self):
        """
        Method to add an attribute with the module name for the api.
        This is mainly useful for logging purposes.
        """
        if not callable(self.resource):
            return

        callable_name = getattr(self.resource, "__name__")
        self.name = callable_name

    def __post_init__(self):
        self._add_short_name_for_resource()


@dataclass
class OpenApiModuleResource:
    api: Optional[ModuleType | Any] = None
    strategy: Optional[Strategy] = Strategy.SINGLE
    name: Optional[str] = ""

    # if we resolve the api, then this object is usable
    def __bool__(self) -> bool:
        return bool(self.api)

    def __repr__(self) -> str:
        if not self.name or not self.api:
            return "Empty"
        return self.name

    def _get_api_strategy(self):
        if not self.api:
            return

        return_type = get_type_hints(self.api.sync_detailed).get("return")
        return_arguments = get_args(return_type)

        for return_argument in return_arguments:
            if get_origin(return_argument) is list:
                self.strategy = Strategy.BULK

                # return once we know return is bulk response
                return

    def _add_short_name_for_resource(self):
        """
        Method to add an attribute with the module name for the api.
        This is mainly useful for logging purposes.
        """
        if not isinstance(self.api, ModuleType):
            return
        module_spec = getattr(self.api, "__spec__")
        module_full_name = getattr(module_spec, "name")
        module_short_name = str(module_full_name).rsplit(".", 1)[-1]
        self.name = module_short_name

    def __post_init__(self):
        self._get_api_strategy()
        self._add_short_name_for_resource()
