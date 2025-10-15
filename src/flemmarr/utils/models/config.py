from dataclasses import dataclass, field
from typing import Dict, List

from flemmarr.utils.enum import MergeKey, Strategy
from flemmarr.utils.models.general import OpenApiModuleResource, OpenApiModelResource


@dataclass
class ConfigItem:
    # mandatory user input
    config_name: str
    root_config_name: str = ""

    # optional user input for generic api's
    create: OpenApiModuleResource = field(default_factory=OpenApiModuleResource)
    delete: OpenApiModuleResource = field(default_factory=OpenApiModuleResource)
    get: OpenApiModuleResource = field(default_factory=OpenApiModuleResource)
    get_schema: OpenApiModuleResource = field(default_factory=OpenApiModuleResource)
    update: OpenApiModuleResource = field(default_factory=OpenApiModuleResource)
    model: OpenApiModelResource = field(default_factory=OpenApiModelResource)

    # optional user input for strategies and merge key
    merge_strategy: Strategy = Strategy.NONE
    merge_key: MergeKey = MergeKey.NONE
    schema_merge_key: MergeKey = MergeKey.NONE

    # attributes for storage
    schemas: List = field(default_factory=list)
    raw_schemas: List = field(default_factory=list)

    ## raw configs
    derived_raw_configs: List = field(default_factory=list)
    desired_raw_configs: List[Dict] = field(default_factory=list)
    merged_raw_configs: List = field(default_factory=list)

    ## raw config maps
    derived_raw_config_map: Dict = field(default_factory=dict)
    desired_raw_config_map: Dict = field(default_factory=dict)
    merged_raw_config_map: Dict = field(default_factory=dict)
    new_raw_config_map: Dict = field(default_factory=dict)
    raw_schema_map: Dict = field(default_factory=dict)

    ## modeled configs
    derived_modeled_configs: List = field(default_factory=list)
    desired_modeled_configs: List = field(default_factory=list)
    new_modeled_configs: List = field(default_factory=list)
    update_modeled_configs: List = field(default_factory=list)

    def _auto_select_apis_and_strategies(self):
        """
        Method to figure out which api to use based on the ones we were able to resolve
        """

        # resolve config merge strategy based off get strategy unless overriden
        self.merge_strategy = (
            self.get.strategy
            if self.get.strategy and self.merge_strategy is Strategy.NONE
            else self.merge_strategy
        )

        # resolve config merge key unless overriden
        if self.merge_key is MergeKey.NONE:
            model_has_name = hasattr(self.model, MergeKey.NAME.name.lower())
            if self.merge_strategy == Strategy.BULK and not self.merge_key.value:
                self.merge_key = MergeKey.NAME if model_has_name else MergeKey.TITLE
            else:
                self.merge_key = MergeKey.SINGLE_ITEM

        # sometimes we have multiple schemas so we need a key to merge with
        if self.schema_merge_key is MergeKey.NONE:
            model_has_implementation = hasattr(
                self.model.resource, MergeKey.IMPLEMENTATION.name.lower()
            )
            self.schema_merge_key = (
                MergeKey.IMPLEMENTATION
                if model_has_implementation
                else MergeKey.SINGLE_ITEM
            )

    def __post_init__(self):
        self._auto_select_apis_and_strategies()

    def __repr__(self) -> str:
        repr = []
        repr.append(
            f"\n\n{self.__class__.__name__} for {getattr(self.model, 'name')}:\n"
        )

        for attr_key, value in self.__dict__.items():
            if not attr_key.startswith("_"):
                repr.append(f"Attr: {attr_key:<30}Value: {value}")

        repr.append("\n")

        return "\n".join(repr)
