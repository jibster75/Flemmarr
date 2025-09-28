import yaml
import secrets
import string
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from constants import (
    SONARR_DEV_CONFIG_DIR,
    SONARR_DEV_DATA_DIR,
    SONARR_DEV_CONFIG_PATH,
    SONARR_DOCKER_COMPOSE_PATH,
)


def generate_api_key(length=32):
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, "utf-8")
    parsed = minidom.parseString(rough_string)
    return parsed.toprettyxml(indent="  ")


def write_config_xml(output_path: Path, api_key: str = ""):
    config = Element("Config")

    fields = {
        "BindAddress": "*",
        "Port": "8989",
        "SslPort": "9898",
        "EnableSsl": "False",
        "LaunchBrowser": "True",
        "ApiKey": api_key,
        "AuthenticationMethod": "External",
        "AuthenticationRequired": "DisabledForLocalAddresses",
        "Branch": "main",
        "LogLevel": "debug",
        "SslCertPath": "",
        "SslCertPassword": "",
        "UrlBase": "",
        "InstanceName": "Sonarr",
        "UpdateMechanism": "Docker",
    }

    for key, value in fields.items():
        SubElement(config, key).text = value

    xml_str = prettify_xml(config)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(xml_str)
    print(f"✅ Wrote formatted config.xml to: {output_path}")


def setup_directories(config_dir, data_dir):
    config_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 Created config directory at: {config_dir}")
    print(f"📁 Created data directory at: {data_dir}")

    return config_dir


def write_docker_compose_file(config_dir, data_dir, docker_compose_path):
    compose_config = {
        "services": {
            "sonarr": {
                "image": "linuxserver/sonarr",
                "container_name": "flemmarr_sonarr_dev",
                "ports": [
                    "8989:8989",
                ],
                "environment": [
                    "PUID=1000",
                    "PGID=1000",
                    "TZ=Etc/UTC",
                ],
                "volumes": [
                    f"{config_dir.resolve()}:/config",
                    f"{data_dir.resolve() / 'tv'}:/data/media/tv",
                    f"{data_dir.resolve() / 'downloads'}:/downloads",
                ],
                "restart": "unless-stopped",
            }
        }
    }

    docker_compose_path.parent.mkdir(parents=True, exist_ok=True)
    with open(docker_compose_path, "w") as f:
        yaml.dump(compose_config, f, default_flow_style=False)

    print(f"✅ docker-compose.yml written to {docker_compose_path}")


if __name__ == "__main__":
    config_dir = setup_directories(SONARR_DEV_CONFIG_DIR, SONARR_DEV_DATA_DIR)
    api_key = generate_api_key()
    write_config_xml(SONARR_DEV_CONFIG_PATH, api_key)
    write_docker_compose_file(
        SONARR_DEV_CONFIG_DIR,
        SONARR_DEV_DATA_DIR,
        SONARR_DOCKER_COMPOSE_PATH,
    )
