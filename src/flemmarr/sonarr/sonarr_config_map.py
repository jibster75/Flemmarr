from flemmarr.clients.sonarr_client.api.indexer import (
    get_api_v3_indexer,
    post_api_v3_indexer,
)
from clients.sonarr_client.api.host_config import (
    get_api_v3_config_host,
    put_api_v3_config_host_id,
)
from clients.sonarr_client.api.indexer import delete_api_v3_indexer_id
from clients.sonarr_client.api.media_management_config import (
    get_api_v3_config_mediamanagement,
    put_api_v3_config_mediamanagement_id,
)
from clients.sonarr_client.api.naming_config import (
    get_api_v3_config_naming,
    put_api_v3_config_naming_id,
)
from clients.sonarr_client.api.quality_definition import (
    get_api_v3_qualitydefinition,
    put_api_v3_qualitydefinition_update,
)
from clients.sonarr_client.api.root_folder import (
    delete_api_v3_rootfolder_id,
    get_api_v3_rootfolder,
    post_api_v3_rootfolder,
)
from clients.sonarr_client.models.indexer_resource import IndexerResource
from clients.sonarr_client.models.media_management_config_resource import (
    MediaManagementConfigResource,
)
from clients.sonarr_client.models.naming_config_resource import NamingConfigResource
from clients.sonarr_client.models.quality_definition_resource import (
    QualityDefinitionResource,
)
from clients.sonarr_client.models.root_folder_resource import RootFolderResource
from clients.sonarr_client.models.host_config_resource import HostConfigResource

merge = "merge"
bulk = "bulk"

config_key_to_args = {
    "config": {
        "host": {
            "model": HostConfigResource,
            "get_api": get_api_v3_config_host,
            "strategy": merge,
            "create_api": put_api_v3_config_host_id,
        },
        "naming": {
            "model": NamingConfigResource,
            "get_api": get_api_v3_config_naming,
            "strategy": merge,
            "create_api": put_api_v3_config_naming_id,
        },
        "mediamanagement": {
            "model": MediaManagementConfigResource,
            "get_api": get_api_v3_config_mediamanagement,
            "strategy": merge,
            "create_api": put_api_v3_config_mediamanagement_id,
        },
    },
    "rootfolder": {
        "model": RootFolderResource,
        "get_api": get_api_v3_rootfolder,
        "delete_api": delete_api_v3_rootfolder_id,
        "create_api": post_api_v3_rootfolder,
    },
    "qualityDefinition": {
        "model": QualityDefinitionResource,
        "get_api": get_api_v3_qualitydefinition,
        "strategy": bulk,
        "create_api": put_api_v3_qualitydefinition_update,
    },
    # "indexer": {
    #     "model": IndexerResource,
    #     "get_api": get_api_v3_indexer,
    #     "delete_api": delete_api_v3_indexer_id,
    #     "create_api": post_api_v3_indexer,
    # },
}
