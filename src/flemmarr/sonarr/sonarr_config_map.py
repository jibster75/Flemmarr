from flemmarr.logger import setup_logging
from utils.models.config import ConfigItem

from flemmarr.utils.models.general import OpenApiModelResource, OpenApiModuleResource

from flemmarr.clients.sonarr_client.api.host_config import (
    get_api_v3_config_host,
    put_api_v3_config_host_id,
)
from flemmarr.clients.sonarr_client.api.naming_config import (
    get_api_v3_config_naming,
    put_api_v3_config_naming_id,
)
from flemmarr.clients.sonarr_client.api.media_management_config import (
    get_api_v3_config_mediamanagement,
    put_api_v3_config_mediamanagement_id,
)
from flemmarr.clients.sonarr_client.api.root_folder import (
    delete_api_v3_rootfolder_id,
    get_api_v3_rootfolder,
    post_api_v3_rootfolder,
)
from flemmarr.clients.sonarr_client.api.quality_definition import (
    get_api_v3_qualitydefinition,
    put_api_v3_qualitydefinition_id,
)
from flemmarr.clients.sonarr_client.api.indexer import (
    delete_api_v3_indexer_id,
    get_api_v3_indexer,
    get_api_v3_indexer_schema,
    post_api_v3_indexer,
    put_api_v3_indexer_id,
)
from flemmarr.clients.sonarr_client.api.quality_profile import (
    delete_api_v3_qualityprofile_id,
    get_api_v3_qualityprofile,
    post_api_v3_qualityprofile,
    put_api_v3_qualityprofile_id,
)
from flemmarr.clients.sonarr_client.api.quality_profile_schema import (
    get_api_v3_qualityprofile_schema,
)

from flemmarr.clients.sonarr_client.api.download_client import (
    delete_api_v3_downloadclient_id,
    get_api_v3_downloadclient,
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

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")


configs = [
    ConfigItem(
        config_name="Host",
        root_config_name="Config",
        get=OpenApiModuleResource(api=get_api_v3_config_host),
        update=OpenApiModuleResource(api=put_api_v3_config_host_id),
        model=OpenApiModelResource(resource=HostConfigResource),
    ),
    ConfigItem(
        config_name="Naming",
        root_config_name="Config",
        get=OpenApiModuleResource(api=get_api_v3_config_naming),
        update=OpenApiModuleResource(api=put_api_v3_config_naming_id),
        model=OpenApiModelResource(resource=NamingConfigResource),
    ),
    ConfigItem(
        config_name="MediaManagement",
        root_config_name="Config",
        get=OpenApiModuleResource(api=get_api_v3_config_mediamanagement),
        update=OpenApiModuleResource(api=put_api_v3_config_mediamanagement_id),
        model=OpenApiModelResource(resource=MediaManagementConfigResource),
    ),
    ConfigItem(
        config_name="RootFolder",
        delete=OpenApiModuleResource(api=delete_api_v3_rootfolder_id),
        get=OpenApiModuleResource(api=get_api_v3_rootfolder),
        create=OpenApiModuleResource(api=post_api_v3_rootfolder),
        model=OpenApiModelResource(resource=RootFolderResource),
    ),
    ConfigItem(
        config_name="QualityDefinition",
        get=OpenApiModuleResource(api=get_api_v3_qualitydefinition),
        update=OpenApiModuleResource(api=put_api_v3_qualitydefinition_id),
        model=OpenApiModelResource(resource=QualityDefinitionResource),
    ),
    ConfigItem(
        config_name="Indexer",
        delete=OpenApiModuleResource(api=delete_api_v3_indexer_id),
        get=OpenApiModuleResource(api=get_api_v3_indexer),
        get_schema=OpenApiModuleResource(api=get_api_v3_indexer_schema),
        create=OpenApiModuleResource(api=post_api_v3_indexer),
        update=OpenApiModuleResource(api=put_api_v3_indexer_id),
        model=OpenApiModelResource(resource=IndexerResource),
    ),
    ConfigItem(
        config_name="QualityProfile",
        delete=OpenApiModuleResource(api=delete_api_v3_qualityprofile_id),
        get=OpenApiModuleResource(api=get_api_v3_qualityprofile),
        get_schema=OpenApiModuleResource(api=get_api_v3_qualityprofile_schema),
        create=OpenApiModuleResource(api=post_api_v3_qualityprofile),
        update=OpenApiModuleResource(api=put_api_v3_qualityprofile_id),
        model=OpenApiModelResource(resource=QualityProfileResource),
    ),
    ConfigItem(
        config_name="DownloadClient",
        delete=OpenApiModuleResource(api=delete_api_v3_downloadclient_id),
        get=OpenApiModuleResource(api=get_api_v3_downloadclient),
        get_schema=OpenApiModuleResource(api=get_api_v3_downloadclient_schema),
        create=OpenApiModuleResource(api=post_api_v3_downloadclient),
        update=OpenApiModuleResource(api=put_api_v3_downloadclient_id),
        model=OpenApiModelResource(resource=DownloadClientResource),
    ),
]

for config in configs:
    logger.debug(f"{config}")
breakpoint()
