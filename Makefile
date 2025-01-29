APP_CONTAINER = app

up:
	@docker-compose up

build:
	@docker-compose build

down:
	@docker-compose down

restart:
	@docker-compose down && docker-compose up --build -d

logs:
	@docker-compose logs -f $(APP_CONTAINER)

migrate:
	@docker-compose exec $(APP_CONTAINER) alembic upgrade head

makemigrations:
	@docker-compose exec $(APP_CONTAINER) alembic revision --autogenerate -m "Initial migration"

update_alembic:
	@docker-compose exec $(APP_CONTAINER) alembic upgrade --sql

downgrade:
	@docker-compose exec $(APP_CONTAINER) alembic downgrade -1

test:
	@docker-compose exec $(APP_CONTAINER) pytest

clean:
	@docker-compose down -v

shell:
	@docker-compose exec $(APP_CONTAINER) /bin/bash


init1:
	@docker-compose exec $(APP_CONTAINER) aerich init -t app.core.config.TORTOISE_ORM

init2:
	@docker-compose exec $(APP_CONTAINER) aerich init-db
