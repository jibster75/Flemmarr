import subprocess
import requests
from dev.utils.constants import (
    SONARR_SCHEMA_URL,
    SONARR_SCHEMA_PATH,
    CLIENT_OUTPUT_DIR,
    SONARR_CLIENT_CONFIG_PATH,
)
import json


def fetch_schema():
    print(f"🔄 Fetching schema from {SONARR_SCHEMA_URL} ...")
    response = requests.get(SONARR_SCHEMA_URL)
    response.raise_for_status()
    SONARR_SCHEMA_PATH.parent.mkdir(parents=True, exist_ok=True)
    SONARR_SCHEMA_PATH.write_text(response.text)
    print(f"✅ Schema saved to {SONARR_SCHEMA_PATH}")


def write_config():
    print("📝 Writing openapi-python-client config...")
    CLIENT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    config = {
        "package_name_override": "sonarr_client",
        "project_name_override": "sonarr-client",
        "content_type_overrides": {"text/plain": "application/json"},
    }
    SONARR_CLIENT_CONFIG_PATH.write_text(json.dumps(config, indent=2))
    print(f"✅ Config written to {SONARR_CLIENT_CONFIG_PATH}")


def generate_client():
    print("🛠️ Generating client with openapi-python-client...")
    subprocess.run(
        [
            "openapi-python-client",
            "generate",
            "--config",
            str(SONARR_CLIENT_CONFIG_PATH),
            "--output-path",
            str(CLIENT_OUTPUT_DIR),
            "--path",
            str(SONARR_SCHEMA_PATH),
            "--overwrite",
        ],
        check=True,
    )
    print("✅ Client successfully generated!")


if __name__ == "__main__":
    fetch_schema()
    write_config()
    generate_client()
