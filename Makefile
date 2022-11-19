DC:=CURRENT_UID=$(UID) docker-compose -f "docker-compose.yml"

build:
	$(DC) build web

up:
	$(DC) up -d db web

down:
	$(DC) down

ps:
	$(DC) ps