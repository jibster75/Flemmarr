from pathlib import Path
from dataclasses import dataclass, field, InitVar
import secrets
import string
from typing import Optional, List, Dict

from dev.scripts.utils.constants import DEV_DOCKER_DIR
from dev.scripts.utils.enum import App, Dir, FilePath


def generate_api_key(length=32) -> str:
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


@dataclass
class ArrXmlConfig:
    app: InitVar[App] = field(default=App.NONE)
    InstanceName: Optional[str] = ""
    BindAddress: str = "*"
    Port: str = ""
    SslPort: str = ""
    EnableSsl: bool = False
    LaunchBrowser: bool = True
    ApiKey: str = generate_api_key()
    AuthenticationMethod: str = "External"
    AuthenticationRequired: str = "DisabledForLocalAddresses"
    Branch: str = "main"
    LogLevel: str = "debug"
    SslCertPath: str = ""
    SslCertPassword: str = ""
    UrlBase: str = ""
    UpdateMechanism: str = "Docker"

    def __post_init__(self, app):
        self.InstanceName = self.InstanceName if self.InstanceName else app.value

    def __bool__(self) -> bool:
        return bool(self.InstanceName is not App.NONE.value)


@dataclass
class DockerComposeConfig:
    image: str = ""
    app: InitVar[Optional[App]] = field(default=App.NONE)

    app_name: Optional[str] = field(default=None)
    local_config_dir: Path = field(default=Path())
    local_data_dir: Path = field(default=Path())
    output_path: Path = field(default=Path())
    gen_api_key: bool = False
    container_xml_config: ArrXmlConfig = field(default_factory=ArrXmlConfig)
    local_xml_output: Path = field(default=Path())
    volumes: List[Dict[Path, List]] = field(default_factory=list)
    exposed_ports: List = field(default_factory=list)

    def __post_init__(self, app):
        self.app_name = self.app_name if self.app_name else app.value

        volumes_dir: Path = DEV_DOCKER_DIR / Dir.VOLUMES.value
        app_volumes_dir: Path = volumes_dir / app.value

        self.local_config_dir = (
            self.local_config_dir
            if self.local_config_dir.name
            else app_volumes_dir / Dir.CONFIG.value
        )
        self.local_data_dir = (
            self.local_data_dir
            if self.local_data_dir.name
            else app_volumes_dir / Dir.DATA.value
        )
        self.output_path = (
            self.output_path
            if self.output_path.name
            else (DEV_DOCKER_DIR / f"{app.value}-docker-compose.yaml")
        )
        self.local_xml_output = (
            self.local_xml_output
            if self.local_xml_output.name
            else self.local_config_dir / FilePath.CONFIG_XML
        )
