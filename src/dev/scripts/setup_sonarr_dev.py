import yaml
from typing import Optional, List
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


from dev.scripts.config import configs
from dev.scripts.utils.model import ArrXmlConfig


def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, "utf-8")
    parsed = minidom.parseString(rough_string)
    return parsed.toprettyxml(indent="  ")


def write_config_xml(output_path: Path, xml_config: ArrXmlConfig):
    if not output_path.name or not xml_config:
        return

    config = Element("Config")

    fields = xml_config.__dict__

    for key, value in fields.items():
        SubElement(config, key).text = str(value)

    xml_str = prettify_xml(config)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(xml_str)
    print(f"✅ Wrote formatted config.xml to: {output_path}")


def setup_directories(config_dir, data_dir):
    config_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 Created config directory at: {config_dir}")
    print(f"📁 Created data directory at: {data_dir}")


def write_docker_compose_file(
    app_name: Optional[str] = "",
    image: str = "",
    docker_compose_path: Path = Path(),
    volumes: List = [],
    exposed_ports: List = [],
):
    compose_config = {
        "services": {
            app_name: {
                "image": image,
                "container_name": f"flemmarr_{app_name}_dev",
                "ports": [f"{port}:{port}" for port in exposed_ports],
                "environment": [
                    "PUID=1000",
                    "PGID=1000",
                    "TZ=Etc/UTC",
                ],
                "volumes": [
                    f"{local_dir.resolve()}:/{container_dir}"
                    for volume in volumes
                    for local_dir, container_dirs in volume.items()
                    for container_dir in container_dirs
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
    for config in configs:
        setup_directories(
            config_dir=config.local_config_dir,
            data_dir=config.local_data_dir,
        )
        write_config_xml(
            output_path=config.local_xml_output,
            xml_config=config.container_xml_config,
        )
        write_docker_compose_file(
            app_name=config.app_name,
            image=config.image,
            docker_compose_path=config.output_path,
            volumes=config.volumes,
            exposed_ports=config.exposed_ports,
        )
