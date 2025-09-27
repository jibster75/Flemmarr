from pathlib import Path

# Constants for fetching API schemas
SONARR_SCHEMA_URL = "https://raw.githubusercontent.com/Sonarr/Sonarr/develop/src/Sonarr.Api.V3/openapi.json"
SONARR_SCHEMA_PATH = Path("src/dev/schema/sonarr_openapi.json")

# Constants for python API client generation
CLIENT_OUTPUT_DIR = Path("src/flemmarr/clients")
DEV_OPENAPI_CONFIG_OUTPUT_DIR = Path("src/dev/openapi-python-client-config")
OPEN_API_CLIENT_CONFIG_SUFFIX = "-openapi-python-client-config.json"
SONARR_CLIENT_CONFIG_PATH = (
    DEV_OPENAPI_CONFIG_OUTPUT_DIR / f"sonarr{OPEN_API_CLIENT_CONFIG_SUFFIX}"
)

# Constants for docker compose local set up
DEV_DOCKER_DIR = Path("src/dev/docker")
DEV_VOLUMES_DIR = DEV_DOCKER_DIR / "volumes"

# Constants for sonarr local dev set up
SONARR_DOCKER_COMPOSE_PATH = DEV_DOCKER_DIR / "sonarr-docker-compose.yaml"
SONARR_DEV_VOLUME_DIR = DEV_VOLUMES_DIR / "sonarr"
SONARR_DEV_CONFIG_DIR = SONARR_DEV_VOLUME_DIR / "config"
SONARR_DEV_CONFIG_PATH = SONARR_DEV_CONFIG_DIR / "config.xml"
SONARR_DEV_DATA_DIR = SONARR_DEV_VOLUME_DIR / "data"
