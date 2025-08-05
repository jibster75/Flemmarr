from flemmarr.clients.sonarr_client import AuthenticatedClient
from flemmarr.logger import setup_logging
from flemmarr.clients.sonarr_client.api.api_info import get_api
from flemmarr.clients.sonarr_client.types import Response, Unset
import requests
from urllib3.util import Retry
from flemmarr.sonarr.sonarr_config_map import config_key_to_args, merge, bulk

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")


class SonarrConfigHandler(object):
    def __init__(self, address, port, apiKey=""):
        self.address = address
        self.port = port
        self.apiKey = apiKey

        adapter = requests.adapters.HTTPAdapter(
            max_retries=Retry(total=10, backoff_factor=0.1)
        )

        self.r = requests.Session()
        self.r.mount("http://", adapter)
        self.r.mount("https://", adapter)

    def __url(self):
        address = (
            self.address
            if self.address.startswith("http")
            else "http://" + self.address
        )
        return "{}:{}".format(address, self.port)

    def initialize(self):
        # Auto retrieve API key if one is not provided
        if not self.apiKey:
            response = self.r.get("{}/initialize.json".format(self.__url()))

            response_data = response.json()

            self.apiKey = response_data["apiKey"]

        logger.debug(f"Setting up client with the following url: {self.__url()}")
        self.client = AuthenticatedClient(
            base_url=f"{self.__url()}",
            token=self.apiKey,
            prefix="",
            auth_header_name="X-Api-Key",
        )

        api: Response = get_api.sync_detailed(client=self.client)
        logger.debug(f"API Info response from Sonarr: {api.content}")

        logger.info("Successfully connected to the server and fetched the API key")

    def convert_to_list(self, object):
        # Check if list
        if not isinstance(object, list):
            object = [object]

        return object

    def get_desired_config(
        self,
        desired_raw_config,
        model,
    ):
        desired_raw_config = self.convert_to_list(desired_raw_config)

        desired_config = [model().from_dict(config) for config in desired_raw_config]

        return desired_config

    def merge_desired_config_with_desired(
        self,
        desired_raw_config,
        derived_config,
    ):
        derived_raw_config = derived_config.to_dict()
        derived_raw_config.update(desired_raw_config)
        derived_config = derived_config.from_dict(derived_raw_config)
        derived_config = self.convert_to_list(derived_config)

        return derived_config

    def get_derived_config(self, derived_config_api):
        logger.debug(f"Derived API provided: {derived_config_api.__name__}")
        derived_config = derived_config_api.sync(client=self.client)

        return derived_config

    def get_config_ids(self, configs):
        id_list = [getattr(config, "id", "") for config in configs]

        return id_list

    def delete_configs(self, configs, delete_api):
        config_ids = self.get_config_ids(configs)
        for id in config_ids:
            self.delete_config_by_id(id, delete_api)

    def delete_config_by_id(self, id, delete_api):
        logger.info(f"Attempting to delete id: {id} via {delete_api.__name__}")
        response = delete_api.sync_detailed(client=self.client, id=id)
        if str(response.status_code) == "200":
            logger.info(f"Successfully deleted id: {id} via {delete_api.__name__}")
        else:
            logger.warning(
                f"Error while deleting {id} via {delete_api.__name__}. \nStatus code: {response.status_code}\nContent: {response.content}"
            )

    def apply_desired_config(self, desired_config, apply_api, strategy):
        if strategy == bulk:
            apply_api.sync_detailed(client=self.client, body=desired_config)
            logger.debug(f"Desired Config: {desired_config}")
            return
        for config in desired_config:
            kwargs = {}
            id = getattr(config, "id", None)
            if id:
                kwargs["id"] = id
                logger.debug(f"ID for config apply request: {id}")

            apply_api.sync_detailed(client=self.client, body=config, **kwargs)

    def handle_config_base(
        self,
        desired_raw_config,
        config_key,
        strategy=None,
        model=None,
        get_api=None,
        delete_api=None,
        create_api=None,
        **kwargs,
    ):
        desired_raw_config = desired_raw_config.get(config_key, [])
        if not desired_raw_config:
            logger.info(f"No desired {model.__name__} config to handle, continuing.. ")
            return
        # If additional kwargs are passed, recurse
        if kwargs:
            for config_key, value in kwargs.items():
                logger.debug(f"Config Key: {config_key}\nValue: {value}")
                self.handle_config_base(
                    desired_raw_config=desired_raw_config,
                    config_key=config_key,
                    **value,
                )
            return

        derived_config = self.get_derived_config(get_api)

        if strategy == merge:
            desired_config = self.merge_desired_config_with_desired(
                desired_raw_config=desired_raw_config,
                derived_config=derived_config,
            )
        else:
            desired_config = self.get_desired_config(
                desired_raw_config,
                model=model,
            )
        if delete_api:
            self.delete_configs(derived_config, delete_api)
        self.apply_desired_config(desired_config, create_api, strategy)

    def apply(self, desired_raw_config):
        for config_key, value in config_key_to_args.items():
            self.handle_config_base(
                desired_raw_config=desired_raw_config, config_key=config_key, **value
            )
