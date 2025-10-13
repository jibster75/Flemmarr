from enum import Enum, StrEnum, auto


class Dir(StrEnum):
    CONFIG = auto()
    DATA = auto()
    VOLUMES = auto()
    MEDIA = f"{DATA}/media"  # data/media
    DOWNLOADS = f"{MEDIA}/downloads"  # data/media/downloads
    TV = f"{MEDIA}/tv"  # data/media/tv


class FilePath(StrEnum):
    CONFIG_XML = "config.xml"


class Port(Enum):
    SONARR_WEB = 8989
    SONARR_HTTPS = 9898
    SABNZBD_WEB = 8080


class App(StrEnum):
    NONE = auto()
    SONARR = auto()
    SABNZBD = auto()

    def __init__(
        self,
        value: str,
    ):
        self._value_ = value

        port = Port.__members__.get(f"{value.upper()}_WEB")
        ssl_port = Port.__members__.get(f"{value.upper()}_HTTPS")

        self.port = str(port.value) if port else ""
        self.ssl_port = str(ssl_port.value) if ssl_port else ""
