from pathlib import Path

SONARR_SCHEMA_URL = "https://raw.githubusercontent.com/Sonarr/Sonarr/develop/src/Sonarr.Api.V3/openapi.json"
SONARR_SCHEMA_PATH = Path("src/dev/schema/sonarr_openapi.json")
CLIENT_OUTPUT_DIR = Path("src/flemmarr/clients")
DEV_OPENAPI_CONFIG_OUTPUT_DIR = Path("src/flemmarr/clients")
OPEN_API_CLIENT_CONFIG_SUFFIX = "-openapi-python-client-config.json"
SONARR_CLIENT_CONFIG_PATH = Path(f"{str(DEV_OPENAPI_CONFIG_OUTPUT_DIR)}/sonarr{OPEN_API_CLIENT_CONFIG_SUFFIX}")
