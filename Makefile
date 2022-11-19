DC:=CURRENT_UID=$(UID) docker-compose -f "docker-compose.yml"

build:
	$(DC) build web

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

pgadmin:
	docker pull dpage/pgadmin4
	docker run --rm -p 5051:80 \
		--network="unbridaled-python-interview_intranet" \
		--link="db_1" \
		-e "PGADMIN_DEFAULT_EMAIL=admin@example.com" \
		-e "PGADMIN_DEFAULT_PASSWORD=admin" \
		dpage/pgadmin4