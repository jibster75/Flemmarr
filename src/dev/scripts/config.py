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
    {sonarr.local_data_dir: [Dir.DATA.value]},
    {sonarr.app_volumes_dir / Dir.TV: []},
]

sonarr.exposed_ports = [App.SONARR.port]


sabnzbd = DockerComposeConfig(
    app=App.SABNZBD,
    gen_api_key=True,
    image="linuxserver/sabnzbd",
)
sabnzbd.volumes = [
    {sabnzbd.local_config_dir: [Dir.CONFIG.value]},
    {sabnzbd.local_data_dir: [Dir.DATA.value]},
]

sabnzbd.exposed_ports = [App.SABNZBD.port]

configs = [
    sonarr,
    sabnzbd,
]
