import yaml
import os
from flemmarr.logger import setup_logging
from flemmarr.utils.performance import profile

from sonarr.sonarr_handler import SonarrConfigHandler

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")


@profile
def main():
    # Check if we're in retrieve config mode
    retrieve_config = bool(os.getenv("FLEMMARR_RETRIEVE_CONFIG", False))

    logger.info("Starting Flemmarr")
    configs = yaml.safe_load(open("./config/config.yml", "r"))

    for key in configs:
        config = configs[key]
        server = config.pop("server")

        if key == "sonarr":
            sonarr = SonarrConfigHandler(
                server["address"], server["port"], retrieve_config
            )
            logger.info("Trying to connect to {}".format(key))
            sonarr.initialize()
            logger.info("Starting configuration handling")
            sonarr.apply(config)

    logger.info("Finished configuration handling")


if __name__ == "__main__":
    main()
