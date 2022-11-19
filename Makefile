DC:=CURRENT_UID=$(UID) docker-compose -f "docker-compose.yml"

up:
	$(DC) up -d db

down:
	$(DC) down