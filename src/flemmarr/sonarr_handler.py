from flemmarr.clients.sonarr_client import AuthenticatedClient
from flemmarr.logger import setup_logging
from flemmarr.clients.sonarr_client.api.api_info import get_api
from flemmarr.clients.sonarr_client.types import Response
import requests
from urllib3.util import Retry


logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")

class SonarrConfigHandler(object):

    def __init__(self, address, port, apiKey=""):
        self.address = address
        self.port = port
        self.apiKey = apiKey

        adapter = requests.adapters.HTTPAdapter(max_retries=Retry(total=10, backoff_factor=0.1))

        self.r = requests.Session()
        self.r.mount('http://', adapter)
        self.r.mount('https://', adapter)

    def __url(self):
        address = self.address if self.address.startswith('http') else 'http://' + self.address
        return '{}:{}'.format(address, self.port)

    def initialize(self):
        # Auto retrieve API key if one is not provided
        if not self.apiKey:
            response = self.r.get('{}/initialize.json'.format(self.__url()))

            response_data = response.json()
            
            self.apiKey = response_data["apiKey"]

        logger.debug(f"Setting up client with the following url: {self.__url()}")
        self.client = AuthenticatedClient(
            base_url=f"{self.__url()}",
            token=self.apiKey,
            prefix="",
            auth_header_name="X-Api-Key",
        )

        with self.client as client:
            api: Response = get_api.sync_detailed(client=client)
            logger.debug(f"API Info response from Sonarr: {api.content}")

        logger.info('Successfully connected to the server and fetched the API key')
    
    def construct_desired_config(self, desired_config):
        logger.debug(f"Desired config: {desired_config}")
        pass
    def get_derived_config(self):
        pass

    def apply(self, desired_config):
        self.construct_desired_config(desired_config)
        self.get_derived_config()
