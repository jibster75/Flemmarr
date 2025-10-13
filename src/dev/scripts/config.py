from dev.scripts.utils.model import DockerComposeConfig, ArrXmlConfig
from dev.scripts.utils.enum import App, Dir


sonarr = DockerComposeConfig(
    app=App.SONARR,
    gen_api_key=True,
    image="linuxserver/sonarr",
    container_xml_config=ArrXmlConfig(
        InstanceName=App.SONARR,
        Port=App.SONARR.port,
        SslPort=App.SONARR.ssl_port,
    ),
)
sonarr.volumes = [
    {sonarr.local_config_dir: [Dir.CONFIG.value]},
    {sonarr.local_data_dir: [Dir.TV.value, Dir.DOWNLOADS.value]},
]

sonarr.exposed_ports = [App.SONARR.port]

configs = [sonarr]
