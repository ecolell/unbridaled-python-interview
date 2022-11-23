ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DC:=CURRENT_UID=$(UID) docker-compose -f "docker-compose.yml"
DC_DEV:=CURRENT_UID=$(UID) docker-compose -f "docker-compose-dev.yml"

freeze-requirements:
	cd store && poetry export --without-hashes --format=requirements.txt > requirements.txt
	cd store && poetry export --only dev --without-hashes --format=requirements.txt > requirements_dev.txt

build:
	$(DC) build web

build-dev:
	$(DC_DEV) build web

pipeline-backend-static-check:
	$(DC_DEV) run --rm -w "/usr/src/app" web mypy app

pipeline-backend-test:
	$(DC_DEV) down
	$(DC_DEV) up -d db
	sleep 1;
	$(DC_DEV) run web alembic upgrade head
	touch web.env
	$(DC_DEV) run --rm -w "/usr/src/app" web py.test -s | tee pytest-coverage.txt
	$(DC_DEV) down

dev-bash:
	$(DC_DEV) run --rm -v "$(ROOT_DIR):/usr/src/dapp" -w "/usr/src/dapp" web bash

up:
	$(DC) up -d db web

down:
	$(DC) down

db-migrate:
	$(DC) run web alembic revision --autogenerate -m "${MESSAGE}"

db-upgrade:
	$(DC) run web alembic upgrade head

db-downgrade:
	$(DC) run web alembic downgrade -1

ps:
	$(DC) ps

logs:
	$(DC) logs -f web

pgadmin:
	docker pull dpage/pgadmin4
	docker run --rm -p 5051:80 \
		--network="unbridaled-python-interview_intranet" \
		--link="db_1" \
		-e "PGADMIN_DEFAULT_EMAIL=admin@example.com" \
		-e "PGADMIN_DEFAULT_PASSWORD=admin" \
		dpage/pgadmin4
