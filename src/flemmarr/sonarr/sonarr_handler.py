import requests
from typing import Any, Union, Dict, List
from urllib3.util import Retry
import yaml

from flemmarr.logger import setup_logging
from flemmarr.utils.performance import profile
from flemmarr.utils.enum import Strategy
from flemmarr.utils.constants import api_key_path_suffix
from utils.models.config import ConfigItem

from flemmarr.sonarr.sonarr_config_map import configs

from flemmarr.clients.sonarr_client import AuthenticatedClient
from flemmarr.clients.sonarr_client.types import UNSET
from flemmarr.clients.sonarr_client.errors import UnexpectedStatus
from flemmarr.clients.sonarr_client.api.api_info import get_api as get_api_info


logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")


class SonarrConfigHandler:
    def __init__(self, address, port, retrieve_config: bool, apiKey=""):
        self.address = address
        self.port = port
        self.retrieve_config = retrieve_config
        self.apiKey = apiKey
        self.api_key_path_suffix = api_key_path_suffix

        adapter = requests.adapters.HTTPAdapter(
            max_retries=Retry(total=10, backoff_factor=0.1)
        )

        self.r = requests.Session()
        self.r.mount("http://", adapter)
        self.r.mount("https://", adapter)

    # bool static methods
    @staticmethod
    def _is_successful_http_response(e: UnexpectedStatus) -> bool:
        return e.status_code in range(200, 301)

    @staticmethod
    def _is_list_of_dicts(item: Any) -> bool:
        """
        Checks if an item is a list containing only dictionaries.

        Args:
            item: The item to check.

        Returns:
            bool: True if the item is a list of dictionaries, False otherwise.
        """
        if not isinstance(item, list):
            return False  # Not a list
        if not all(isinstance(element, dict) for element in item):
            return False  # Not all elements are dictionaries
        return True

    # conversion static methods
    @staticmethod
    def _convert_to_list(x: Union[Any, List]):
        # Check if list
        if not isinstance(x, list):
            x = [x]

        return x

    @staticmethod
    def _convert_to_raw_config_map(
        configs: List[Dict],
        primary_key: str,
        secondary_level: str = "",
    ):
        """
        Creates map of key to dictionary from list of dicts
        for key based searching on a list of dicts
        """

        raw_config_map = {}
        for config in configs:
            key = primary_key
            if primary_key in config and config[primary_key]:
                key = config[primary_key]

            elif (
                secondary_level in config
                and primary_key in config[secondary_level]
                and config[secondary_level][primary_key]
            ):
                key = config[secondary_level][primary_key]
            raw_config_map[key] = config

        return raw_config_map

    @staticmethod
    def _convert_to_raw_config(config):
        """
        Converts list of OpenAPI objects to list of dicts
        """
        return config.to_dict()

    @staticmethod
    def _convert_to_modeled_config(model: Any, config: Any) -> Any:
        """
        Converts OpenAPI dict to object
        """
        return model().from_dict(config)

    # other static methods
    @staticmethod
    def _get_config_id(config):
        id = getattr(config, "id", None)
        logger.debug(f"Retrieved the following ID: {id}")
        return id

    def _url(self):
        address = (
            self.address
            if self.address.startswith("http")
            else "http://" + self.address
        )
        return "{}:{}".format(address, self.port)

    def _auto_retrieve_api_key(self):
        logger.debug("Attempting to auto retrieve API key.")

        response = self.r.get(f"{self._url()}/{self.api_key_path_suffix}")

        response_data = response.json()
        self.apiKey = response_data["apiKey"]

        logger.info("Successfully retrieved API key.")

    def _set_up_client(self):
        logger.debug(f"Setting up client with the following url: {self._url()}")
        self.client = AuthenticatedClient(
            base_url=f"{self._url()}",
            token=self.apiKey,
            prefix="",
            auth_header_name="X-Api-Key",
            raise_on_unexpected_status=True,
        )

    def _handle_api_call(self, api, api_args: Dict[str, Any] = {}):
        default_args: Dict[str, Any] = {
            "client": self.client,
        }
        if not api_args:
            api_args = default_args
        try:
            logger.debug(f"API Args: {api_args}")
            return api.sync_detailed(**api_args).parsed
        except UnexpectedStatus as e:
            logger.debug("Attempting to check Unexpected Status http exception.")
            if not self._is_successful_http_response(e):
                logger.debug(
                    f"HTTP Status code is not successful one: {e.status_code}\tType: {type(e.status_code)}"
                )
                raise e
            logger.debug(f"HTTP Status code is a successful one: {e.status_code}")

    def _get_api_info(self):
        self._handle_api_call(api=get_api_info)

    def _convert_to_raw_configs(self, configs):
        """
        Converts list of OpenAPI objects to list of dicts
        """
        return [self._convert_to_raw_config(config) for config in configs]

    def _convert_to_modeled_configs(
        self, model: Any, configs: Union[Any, List[Any]]
    ) -> List[Any]:
        """
        Converts list of OpenAPI dicts to list of objects
        """
        configs = self._convert_to_list(configs)
        return [self._convert_to_modeled_config(model, config) for config in configs]

    def _merge_raw_config_maps(
        self,
        original_config_map,
        new_config_map,
    ):
        # return dicts
        merged_result = {}
        new_result = {}

        for key in list(original_config_map.keys()) + list(new_config_map.keys()):
            # try to get value for both dicts
            original_value = original_config_map.get(key)
            new_value = new_config_map.get(key)

            # if the key is not present in the new config, then merge so we retain existing config
            if key not in new_config_map:
                merged_result[key] = original_value

            # check if key is in original config map,
            # helps determine if we're updating config or creating new config
            elif key in original_config_map:
                merged_result[key] = self._recursive_merge_dicts(
                    original_dict=original_value,
                    new_dict=new_value,
                )

            # if above conditions not met, then we must have new config present
            else:
                new_result[key] = new_value

        return merged_result, new_result

    def _recurse_merge_handle_list_of_dicts(self, original_configs, new_configs):
        if not self._is_list_of_dicts(new_configs):
            return
        # convert list of dicts to config map and merge
        new_config_map = self._convert_to_raw_config_map(
            configs=new_configs,
            primary_key="name",
            secondary_level="quality",
        )
        original_config_map = self._convert_to_raw_config_map(
            configs=original_configs,
            primary_key="name",
            secondary_level="quality",
        )
        merged_config_map, _ = self._merge_raw_config_maps(
            original_config_map=original_config_map,
            new_config_map=new_config_map,
        )

        return list(merged_config_map.values())

    def _recurse_merge_handle_dicts(self, original_config, new_config):
        if not isinstance(new_config, dict):
            return

        return self._recursive_merge_dicts(
            original_dict=original_config,
            new_dict=new_config,
        )

    def _recurse_merge_handle_single(self, original_config, new_config):
        if self._is_list_of_dicts(new_config) or isinstance(new_config, dict):
            return

        # check for None type as new config could be 0 or empty string
        return new_config if new_config is not None else original_config

    def _recursive_merge_dicts(
        self,
        original_dict,
        new_dict,
    ) -> Dict:
        merged_dict = {}
        for key in list(original_dict.keys()) + list(new_dict.keys()):
            # try to get value for both dicts
            original_value = original_dict.get(key)
            new_value = new_dict.get(key)

            result = None

            # if either original value or new value is None, result should be whichever one has a value
            if new_value is None and original_value is not None:
                result = original_value
            elif original_value is None and new_value is not None:
                result = new_value

            # if the value in the dict is a list of dicts, we must handle it
            if result is None:
                result = self._recurse_merge_handle_list_of_dicts(
                    original_configs=original_value,
                    new_configs=new_value,
                )
            if result is None:
                # recurse if type is dict, this will handle Dict[str, Union[List, Dict]]
                result = self._recurse_merge_handle_dicts(
                    original_config=original_value,
                    new_config=new_value,
                )
            if result is None:
                result = self._recurse_merge_handle_single(
                    original_config=original_value,
                    new_config=new_value,
                )

            # checking against None type as some dictionary values may be interpreted as false (i.e. 0)
            if result is not None:
                merged_dict[key] = result

        return merged_dict

    def _process_raw_configs(
        self,
        config: ConfigItem,
    ):
        """
        Merges desired raw config map into derived raw config map.

        Updates new raw config map with new config.
        """
        config.merged_raw_config_map, config.new_raw_config_map = (
            self._merge_raw_config_maps(
                original_config_map=config.derived_raw_config_map,
                new_config_map=config.desired_raw_config_map,
            )
        )

    def _get_config_ids(self, configs):
        return [self._get_config_id(config=config) for config in configs]

    def _clean_new_config(self, config):
        """
        Config for a post operation should not contain an ID
        This function strips ID's
        """
        if type(config) is list:
            return [self._clean_new_config(x) for x in config]
        config.id = UNSET
        return config

    def initialize(self):
        # Auto retrieve API key if one is not provided
        if not self.apiKey:
            self._auto_retrieve_api_key()

        self._set_up_client()

        self._get_api_info()

        logger.info("Successfully set up client.")

    def _convert_to_update_modeled_configs(self, config: ConfigItem):
        config.update_modeled_configs = self._convert_to_modeled_configs(
            model=config.model.resource,
            configs=list(
                config.merged_raw_config_map.values(),
            ),
        )
        logger.debug(f"Update modeled configs: {config.update_modeled_configs}")

    def _convert_to_new_modeled_configs(self, config: ConfigItem):
        pre_new_modeled_configs = self._convert_to_modeled_configs(
            model=config.model.resource,
            configs=list(
                config.new_raw_config_map.values(),
            ),
        )
        config.new_modeled_configs = self._clean_new_config(
            config=pre_new_modeled_configs
        )
        logger.debug(f"New modeled configs: {config.new_modeled_configs}")

    def process_configs(
        self,
        config: ConfigItem,
    ):
        """
        Uses derived and desired config maps to separate new config and
        exisitng config that is being updated.
        """
        logger.debug(
            f"Attempting to process derived and desired configs for: {config.model.name}"
        )

        # process raw configs
        self._process_raw_configs(config=config)

        # Convert to modeled config
        self._convert_to_update_modeled_configs(config=config)
        self._convert_to_new_modeled_configs(config=config)

        logger.info(
            f"Successfully processed derived and desired configs for: {config.model.name}"
        )

    def get_desired_raw_configs(self, config: ConfigItem, desired_user_configs) -> List:
        """
        Takes in full user configs and retrieves only
        the section of config we are currently working on
        """
        desired_raw_configs = []

        # config names
        config_name = config.config_name.lower()
        root_config_name = config.root_config_name.lower()

        # get root config, if it exists
        root_raw_config = desired_user_configs.get(root_config_name)

        if root_raw_config:
            desired_raw_configs = root_raw_config.get(config_name)
        else:
            desired_raw_configs = desired_user_configs.get(config_name)

        return self._convert_to_list(desired_raw_configs) if desired_raw_configs else []

    def get_derived_config(self, config: ConfigItem) -> List[Any]:
        if not config.get.api:
            raise Exception(f"Get API undefined for config: {config.model.name}")
        if not config.get.name:
            logger.warning(f"Get API Name undefined for config: {config.get.api}")

        logger.debug(
            f"Attempting to retrieve derived config using the following api: {config.get.name}"
        )

        derived_config = self._handle_api_call(api=config.get.api)
        logger.info(
            f"Successfully retrieved derived config using the following api: {config.get.name}"
        )

        return self._convert_to_list(derived_config)

    def delete_existing_configs(self, config: ConfigItem):
        # If we're using the create api, we should delete config to avoid conflicts
        if not config.delete.api:
            logger.info(
                f"No delete api specified for: {config.model.name} skipping delete.."
            )
            return

        delete_config_args: Dict[str, Any] = {
            "client": self.client,
        }
        config_ids = self._get_config_ids(config.derived_modeled_configs)
        for id in config_ids:
            delete_config_args["id"] = id
            logger.debug(f"Attempting to delete id: {id} via {config.delete.name}")
            self._handle_api_call(api=config.delete.api, api_args=delete_config_args)
            logger.info(f"Successfully deleted id: {id} via {config.delete.name}")

    def _apply_new_config_single(self, config: ConfigItem):
        if not (config.create.strategy == Strategy.SINGLE):
            return
        logger.debug(
            f"Attempting to apply new config using the following api: {config.create.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
        }
        for new_modeled_config in config.new_modeled_configs:
            args["body"] = new_modeled_config
            self._handle_api_call(api=config.create.api, api_args=args)
        logger.info(
            f"Successfully applied new config using the following api: {config.create.name}"
        )

    def _apply_new_config_bulk(self, config: ConfigItem):
        if not (config.create.strategy == Strategy.BULK):
            return
        logger.debug(
            f"Attempting to apply new config using the following bulk api: {config.create.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
            "body": config.new_modeled_configs,
        }
        self._handle_api_call(api=config.create.api, api_args=args)
        logger.info(
            f"Successfully applied new config using the following bulk api: {config.create.name}"
        )

    def _apply_update_config_single(self, config: ConfigItem):
        if not (
            config.update_modeled_configs
            and config.update.strategy == Strategy.SINGLE
            and config.update.api
        ):
            return
        logger.debug(
            f"Attempting to update config using the following api: {config.update.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
        }
        for update_modeled_config in config.update_modeled_configs:
            args["body"] = update_modeled_config
            args["id"] = self._get_config_id(config=update_modeled_config)
            self._handle_api_call(api=config.update.api, api_args=args)
        logger.info(
            f"Successfully updated config using the following api: {config.update.name}"
        )

    def _apply_update_config_bulk(self, config: ConfigItem):
        if not (
            config.update_modeled_configs
            and config.update.strategy == Strategy.BULK
            and config.update.api
        ):
            return
        logger.debug(
            f"Attempting to update config using the following bulk api: {config.update.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
            "body": config.update_modeled_configs,
        }
        self._handle_api_call(api=config.update.api, api_args=args)
        logger.info(
            f"Successfully updated config using the following bulk api: {config.update.name}"
        )

    def _delete_and_recreate_config_single(self, config: ConfigItem):
        if not (
            config.update_modeled_configs
            and config.create.strategy == Strategy.SINGLE
            and not config.update.api
        ):
            return
        self.delete_existing_configs(config=config)
        logger.debug(
            f"Attempting to recreate config using the following api: {config.create.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
        }
        for update_modeled_config in config.update_modeled_configs:
            args["body"] = update_modeled_config
            self._handle_api_call(api=config.create.api, api_args=args)
        logger.info(
            f"Successfully recreated config using the following api: {config.create.name}"
        )

    def _delete_and_recreate_config_bulk(self, config: ConfigItem):
        if not (
            config.update_modeled_configs
            and config.update.strategy == Strategy.BULK
            and not config.update.api
        ):
            return
        self.delete_existing_configs(config=config)
        logger.debug(
            f"Attempting to recreate config using the following bulk api: {config.create.name}"
        )
        args: Dict[str, Any] = {
            "client": self.client,
            "body": config.update_modeled_configs,
        }
        self._handle_api_call(api=config.create.api, api_args=args)
        logger.info(
            f"Successfully recreated config using the following bulk api: {config.create.name}"
        )

    def apply_config(self, config: ConfigItem):
        # break out early if there's no config to apply
        if not config.update_modeled_configs and not config.new_modeled_configs:
            logger.info(
                f"No existing configs to update or new configs to apply for: {config.model.name} skipping.."
            )
            return

        # apply new config
        if config.new_modeled_configs:
            self._apply_new_config_single(config=config)
            self._apply_new_config_bulk(config=config)
        else:
            logger.info(
                f"No new configs to apply for: {config.model.name} continuing.."
            )

        # break out early if there's no diff between derived and update config
        if config.update_modeled_configs == config.derived_modeled_configs:
            logger.info(
                f"No diff between existing configs and update configs: {config.model.name} skipping.."
            )
            return

        if config.update_modeled_configs:
            # delete and recreate config (if needed)
            self._delete_and_recreate_config_single(config=config)
            self._delete_and_recreate_config_bulk(config=config)

            # apply update config
            self._apply_update_config_single(config=config)
            self._apply_update_config_bulk(config=config)
        else:
            logger.info(f"No configs to update for: {config.model.name} skipping..")

    def _merge_desired_configs_with_schema(self, config: ConfigItem):
        if not config.schemas:
            return

        merged = []
        for raw_desired_config in config.desired_raw_configs:
            # convert to config map as there can be multiple versions for the schema
            schema_merge_key_lower = config.schema_merge_key.name.lower()

            raw_desired_config_map = self._convert_to_raw_config_map(
                configs=self._convert_to_list(raw_desired_config),
                primary_key=schema_merge_key_lower,
            )

            resolved_schema_merge_key = raw_desired_config.get(
                schema_merge_key_lower,
                schema_merge_key_lower,
            )
            merged_raw_config = self._recursive_merge_dicts(
                original_dict=config.raw_schema_map[resolved_schema_merge_key],
                new_dict=raw_desired_config_map[resolved_schema_merge_key],
            )

            merged.append(merged_raw_config)

        config.desired_raw_configs = merged

    def fetch_and_prepare_config(
        self, config: ConfigItem, desired_user_configs, derived_only: bool = False
    ):
        # derived configs
        config.derived_modeled_configs = self.get_derived_config(config=config)
        logger.debug(f"Derived Modeled Configs: {config.derived_modeled_configs}")

        config.derived_raw_configs = self._convert_to_raw_configs(
            configs=config.derived_modeled_configs
        )
        # break out early if user only wants derived config
        if derived_only:
            return

        # desired configs
        config.desired_raw_configs = self.get_desired_raw_configs(
            config, desired_user_configs
        )
        logger.debug(f"Desired Raw Configs: {config.desired_raw_configs}")

        # break out early if no desired raw configs
        if not config.desired_raw_configs:
            return

        # config schema
        if config.get_schema:
            pre_config_schema = self._handle_api_call(api=config.get_schema.api)
            config.schemas = self._convert_to_list(pre_config_schema)

            config.raw_schemas = self._convert_to_raw_configs(config.schemas)
            config.raw_schema_map = self._convert_to_raw_config_map(
                configs=config.raw_schemas,
                primary_key=config.schema_merge_key.name.lower(),
            )

        # format with config schema, if it exists
        self._merge_desired_configs_with_schema(config=config)

        # config maps
        merge_key_lower = config.merge_key.name.lower()
        config.derived_raw_config_map = self._convert_to_raw_config_map(
            configs=config.derived_raw_configs,
            primary_key=merge_key_lower,
        )
        logger.debug(f"Derived Raw Config Map: {config.derived_raw_config_map}")

        config.desired_raw_config_map = self._convert_to_raw_config_map(
            configs=config.desired_raw_configs,
            primary_key=merge_key_lower,
        )
        logger.debug(f"Desired Raw Config Map: {config.desired_raw_config_map}")

    @profile
    def handle_config_base(
        self,
        config: ConfigItem,
        desired_user_configs: Dict,
    ):
        self.fetch_and_prepare_config(
            config=config,
            desired_user_configs=desired_user_configs,
            derived_only=self.retrieve_config,
        )

        if self.retrieve_config:
            derived_raw_configs = {config.config_name: config.derived_raw_configs}
            logger.info(
                f"Retrieved config for: {config.model.name}\n{yaml.dump(derived_raw_configs, indent=4)}"
            )
            return

        if not config.desired_raw_configs:
            logger.info(
                f"No desired config for {config.model.name} config to handle, continuing.. "
            )
            return

        self.process_configs(config=config)

        self.apply_config(config=config)

    @profile
    def apply(self, desired_user_configs):
        for config in configs:
            self.handle_config_base(
                config=config,
                desired_user_configs=desired_user_configs,
            )
