import os
import time
import yaml


from flemmarr.logger import setup_logging
from flemmarr.utils.performance import profile

from flemmarr.sonarr.sonarr_handler import SonarrConfigHandler

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")


def handle_retrieve_config(app):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    retrieved_config_file = f"./config/retrieved/{app}_config_{timestamp}.yml"

    return retrieved_config_file


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
            retrieved_config_filename = handle_retrieve_config(app=key)
            sonarr = SonarrConfigHandler(
                server["address"], server["port"], retrieve_config
            )

            logger.info("Trying to connect to {}".format(key))
            sonarr.initialize()
            logger.info("Starting configuration handling")
            retrieved_configs = sonarr.apply(config)

            if retrieve_config:
                with open(retrieved_config_filename, "w") as file:
                    yaml.dump(retrieved_configs, file)

    logger.info("Finished configuration handling")


if __name__ == "__main__":
    main()
