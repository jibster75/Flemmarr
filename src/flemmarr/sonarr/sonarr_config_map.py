from flemmarr.clients.sonarr_client.api.indexer import (
    get_api_v3_indexer,
    post_api_v3_indexer,
)
from clients.sonarr_client.api.host_config import (
    get_api_v3_config_host,
    put_api_v3_config_host_id,
)
from clients.sonarr_client.api.indexer import delete_api_v3_indexer_id
from clients.sonarr_client.api.root_folder import (
    delete_api_v3_rootfolder_id,
    get_api_v3_rootfolder,
    post_api_v3_rootfolder,
)
from clients.sonarr_client.models.indexer_resource import IndexerResource
from clients.sonarr_client.models.root_folder_resource import RootFolderResource
from clients.sonarr_client.models.host_config_resource import HostConfigResource


config_key_to_args = {
    "config": {
        "host": {
            "model": HostConfigResource,
            "get_api": get_api_v3_config_host,
            "create_api": put_api_v3_config_host_id,
        }
    },
    "rootfolder": {
        "model": RootFolderResource,
        "get_api": get_api_v3_rootfolder,
        "delete_api": delete_api_v3_rootfolder_id,
        "create_api": post_api_v3_rootfolder,
    },
    "indexer": {
        "model": IndexerResource,
        "get_api": get_api_v3_indexer,
        "delete_api": delete_api_v3_indexer_id,
        "create_api": post_api_v3_indexer,
    },
}
