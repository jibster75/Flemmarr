from flemmarr.clients.sonarr_client.api.host_config import (
    get_api_v3_config_host,
    get_api_v3_config_host_id,
    put_api_v3_config_host_id,
)
from flemmarr.clients.sonarr_client.api.naming_config import (
    get_api_v3_config_naming,
    get_api_v3_config_naming_id,
    put_api_v3_config_naming_id,
)
from flemmarr.clients.sonarr_client.api.media_management_config import (
    get_api_v3_config_mediamanagement,
    get_api_v3_config_mediamanagement_id,
    put_api_v3_config_mediamanagement_id,
)
from flemmarr.clients.sonarr_client.api.root_folder import (
    delete_api_v3_rootfolder_id,
    get_api_v3_rootfolder,
    get_api_v3_rootfolder_id,
    post_api_v3_rootfolder,
)
from flemmarr.clients.sonarr_client.api.quality_definition import (
    get_api_v3_qualitydefinition,
    get_api_v3_qualitydefinition_id,
    put_api_v3_qualitydefinition_id,
)
from flemmarr.clients.sonarr_client.api.indexer import (
    delete_api_v3_indexer_id,
    get_api_v3_indexer,
    get_api_v3_indexer_id,
    get_api_v3_indexer_schema,
    post_api_v3_indexer,
    put_api_v3_indexer_id,
)
from flemmarr.clients.sonarr_client.api.quality_profile import (
    delete_api_v3_qualityprofile_id,
    get_api_v3_qualityprofile,
    get_api_v3_qualityprofile_id,
    post_api_v3_qualityprofile,
    put_api_v3_qualityprofile_id,
)
from flemmarr.clients.sonarr_client.api.quality_profile_schema import (
    get_api_v3_qualityprofile_schema,
)

from flemmarr.clients.sonarr_client.api.download_client import (
    delete_api_v3_downloadclient_id,
    get_api_v3_downloadclient,
    get_api_v3_downloadclient_id,
    get_api_v3_downloadclient_schema,
    post_api_v3_downloadclient,
    put_api_v3_downloadclient_id,
)

from flemmarr.clients.sonarr_client.models.host_config_resource import (
    HostConfigResource,
)
from flemmarr.clients.sonarr_client.models.naming_config_resource import (
    NamingConfigResource,
)
from flemmarr.clients.sonarr_client.models.media_management_config_resource import (
    MediaManagementConfigResource,
)
from flemmarr.clients.sonarr_client.models.root_folder_resource import (
    RootFolderResource,
)
from flemmarr.clients.sonarr_client.models.indexer_resource import IndexerResource
from flemmarr.clients.sonarr_client.models.quality_profile_resource import (
    QualityProfileResource,
)

from flemmarr.clients.sonarr_client.models.download_client_resource import (
    DownloadClientResource,
)

from flemmarr.clients.sonarr_client.models.quality_definition_resource import (
    QualityDefinitionResource,
)


from typing import Any, Literal, Optional, Dict, List
from types import ModuleType
from dataclasses import dataclass, field
from flemmarr.logger import setup_logging


logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")

# Strategies for config merge, apply, and delete
single = "single"
bulk = "bulk"

default_key = "default"

api_key_path_suffix = "/initialize.json"


@dataclass
class configItem:
    # mandatory user input
    config_name: str
    root_config_name: str = ""

    # optional user input for generic api's
    create_api: Optional[Any] = None
    delete_api: Optional[Any] = None
    get_api: Optional[Any] = None
    get_api_schema: Optional[Any] = None
    model: Optional[Any] = None
    update_api: Optional[Any] = None

    # optional user input for granular api's
    create_api_single: Optional[Any] = None
    delete_api_single: Optional[Any] = None
    get_api_single: Optional[Any] = None
    update_api_single: Optional[Any] = None

    create_api_bulk: Optional[Any] = None
    delete_api_bulk: Optional[Any] = None
    get_api_bulk: Optional[Any] = None
    update_api_bulk: Optional[Any] = None

    # optional user input for strategies and merge key
    create_strategy: Optional[str] = single
    delete_strategy: Optional[str] = single
    update_strategy: Optional[str] = single
    merge_strategy: Optional[str] = single
    merge_key: str = default_key
    schema_merge_key: str = default_key

    # auto resolved name attrs
    delete_api_name: Optional[str] = None
    get_api_name: Optional[str] = None
    create_api_name: Optional[str] = None
    create_api_single_name: Optional[str] = None
    create_api_bulk_name: Optional[str] = None
    update_api_name: Optional[str] = None
    update_api_single_name: Optional[str] = None
    update_api_bulk_name: Optional[str] = None
    model_name: Optional[str] = None

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

    def _init_template_vars(self):
        """
        Define vars used in _auto_resolve_attrs()
        """

        # static string prefixes and suffixes
        self._get_api_prefix = "get_api_v3"
        self._create_api_prefix = "post_api_v3"
        self._update_api_prefix = "put_api_v3"
        self._delete_api_prefix = "delete_api_v3"

        # templated string prefixes and suffixes
        _resolved_root_config_name = (
            self.root_config_name if type(self.root_config_name) is str else ""
        )
        _api_suffix_prefix = (
            "_" + str(_resolved_root_config_name).lower()
            if _resolved_root_config_name
            else ""
        )

        self._model_prefix = f"{self.config_name}{_resolved_root_config_name}"

        self._single_resource_suffix = "_id"
        self._schema_suffix = "_schema"
        self._api_suffix = f"{_api_suffix_prefix}{f'_{self.config_name.lower()}'}"

    def _init_attr_default_template(self):
        """
        Create map with a default template map for each attr
        """
        self._attr_default_template = {
            "model": globals().get(f"{self._model_prefix}Resource"),
            "get_api_single": globals().get(
                f"{self._get_api_prefix}{self._api_suffix}{self._single_resource_suffix}"
            ),
            "get_api_bulk": globals().get(f"{self._get_api_prefix}{self._api_suffix}"),
            "get_api_schema": globals().get(
                f"{self._get_api_prefix}{self._api_suffix}{self._schema_suffix}"
            ),
            "create_api_single": globals().get(
                f"{self._create_api_prefix}{self._api_suffix}{self._single_resource_suffix}"
            ),
            "create_api_bulk": globals().get(
                f"{self._create_api_prefix}{self._api_suffix}"
            ),
            "update_api_single": globals().get(
                f"{self._update_api_prefix}{self._api_suffix}{self._single_resource_suffix}"
            ),
            "update_api_bulk": globals().get(
                f"{self._update_api_prefix}{self._api_suffix}"
            ),
            "delete_api_single": globals().get(
                f"{self._delete_api_prefix}{self._api_suffix}{self._single_resource_suffix}"
            ),
            "delete_api_bulk": globals().get(
                f"{self._delete_api_prefix}{self._api_suffix}"
            ),
        }

    def _auto_resolve_attrs(self):
        """
        Method to auto resolve attrs to their respective classes and methods.
        This is to reduce the amount of user input required when defining config sections.
        """

        # Create copy of dict to avoid errors when updating the object below
        self._initial_attrs = self.__dict__.copy().items()

        # Iterate through attrs and set default template if value is empty
        for attr_key, value in self._initial_attrs:
            if not value and not attr_key.startswith("_"):
                setattr(
                    self, attr_key, self._attr_default_template.get(attr_key, value)
                )

    def _auto_select_apis_and_strategies(self):
        """
        Method to figure out which api to use based on the ones we were able to resolve
        """
        # Choose bulk methods whenever possible
        self.delete_api = (
            self.delete_api_bulk if self.delete_api_bulk else self.delete_api_single
        )

        self.get_api = self.get_api_single
        if self.get_api_bulk:
            self.get_api = self.get_api_bulk
            self.merge_strategy = (
                bulk if not self.merge_strategy else self.merge_strategy
            )

        self.create_api = (
            self.create_api_bulk if self.create_api_bulk else self.create_api_single
        )
        self.update_api = (
            self.update_api_bulk if self.update_api_bulk else self.update_api_single
        )

        # update to bulk strategies, if applicapable
        if self.create_api is self.create_api_bulk:
            self.create_strategy = (
                bulk if not self.create_strategy else self.create_strategy
            )
        if self.delete_api is self.delete_api_bulk:
            self.delete_strategy = (
                bulk if not self.delete_strategy else self.delete_strategy
            )
        if self.update_api is self.update_api_bulk:
            self.update_strategy = (
                bulk if not self.update_strategy else self.update_strategy
            )

        # auto select merge key
        model_has_name = hasattr(self.model, "name")
        if self.merge_strategy == bulk and not self.merge_key:
            self.merge_key = "name" if model_has_name else "title"

        # TODO: update default here
        model_has_implementation = hasattr(self.model, "implementation")
        if self.schema_merge_key == default_key:
            self.schema_merge_key = (
                "implementation" if model_has_implementation else self.schema_merge_key
            )

    def _add_short_name_for_apis_and_models(self):
        """
        Method to add an attribute with the module name for the apis in this class.
        This is mainly useful for logging purposes.
        """
        for attr_key, value in self._initial_attrs:
            current_attr_value = getattr(self, attr_key)
            if isinstance(current_attr_value, ModuleType):
                module_full_name = getattr(current_attr_value.__spec__, "name")
                module_short_name = str(module_full_name).rsplit(".", 1)[-1]
                setattr(self, f"{attr_key}_name", module_short_name)

            elif callable(current_attr_value):
                callable_name = getattr(current_attr_value, "__name__")
                setattr(self, f"{attr_key}_name", callable_name)

    def __post_init__(self):
        self._init_template_vars()
        self._init_attr_default_template()
        self._auto_resolve_attrs()
        self._auto_select_apis_and_strategies()
        self._add_short_name_for_apis_and_models()

    def __repr__(self) -> str:
        repr = []
        repr.append(
            f"\n\n{self.__class__.__name__} for {getattr(self.model, '__name__')}:\n"
        )

        for attr_key, value in self.__dict__.items():
            if not attr_key.startswith("_"):
                formatted_value = value

                # Ignore string types as these have clear representations already
                if value and type(value) is not str:
                    # Retrieve the Class or method name and only the direct name
                    formatted_value = str(value.__name__).rsplit(".", 1)[-1]
                repr.append(f"Attr: {attr_key:<30}Value: {formatted_value}")

        repr.append("\n")

        return "\n".join(repr)


configs = [
    configItem(
        config_name="Host",
        root_config_name="Config",
    ),
    configItem(
        config_name="Naming",
        root_config_name="Config",
    ),
    configItem(
        config_name="MediaManagement",
        root_config_name="Config",
    ),
    configItem(config_name="RootFolder", create_strategy=single),
    configItem(
        config_name="QualityDefinition",
    ),
    configItem(
        config_name="Indexer",
        create_strategy=single,
    ),
    configItem(
        config_name="QualityProfile",
        create_strategy=single,
    ),
    configItem(
        config_name="DownloadClient",
        create_strategy=single,
    ),
]

for config in configs:
    logger.debug(f"{config}")
