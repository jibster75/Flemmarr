.PHONY: default install generate run format

default: install generate

install:
	poetry install

generate:
	poetry run python src/dev/scripts/generate_models.py
	poetry run python src/dev/scripts/generate_example_config.py

generate_models:
	poetry run python src/dev/scripts/generate_models.py

run:
	poetry run python -m flemmarr

run_retrieve_config:
	FLEMMARR_RETRIEVE_CONFIG="TRUE" poetry run python -m flemmarr

run_debug:
	FLEMMARR_LOG_LEVEL="DEBUG" poetry run python -m flemmarr

format:
	poetry run black src/flemmarr
	poetry run isort src/flemmarr

sonarr_docker_up:
	docker-compose -f src/dev/docker/sonarr-docker-compose.yaml up -d

sabnzbd_docker_up:
	docker-compose -f src/dev/docker/sabnzbd-docker-compose.yaml up -d

sonarr_docker_down: 
	docker-compose -f src/dev/docker/sonarr-docker-compose.yaml down 

sabnzbd_docker_down: 
	docker-compose -f src/dev/docker/sabnzbd-docker-compose.yaml down 

dev_up:
	$(MAKE) install
	poetry run python src/dev/scripts/setup_sonarr_dev.py
	$(MAKE) sonarr_docker_up
	$(MAKE) sabnzbd_docker_up

dev_down:
	$(MAKE) sonarr_docker_down
	$(MAKE) sabnzbd_docker_down
