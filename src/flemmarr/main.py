import yaml
from flemmarr.logger import setup_logging
from sonarr.sonarr_handler import SonarrConfigHandler

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")

def main():
    logger.info("Starting Flemmarr")
    configs = yaml.safe_load(open('./config/config.yml', 'r'))

    for key in configs:
        config = configs[key]
        server = config['server']
        config.pop('server')

        if key == "sonarr":
            sonarr = SonarrConfigHandler(server['address'], server['port'])
            logger.info('Trying to connect to {}'.format(key))
            sonarr.initialize()
            logger.info('Starting to apply configuration')
            sonarr.apply(config)

    logger.info('Finished to apply configurations')

if __name__ == "__main__":
    main()