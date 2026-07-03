APP_MODULE=app.main:app
ALEMBIC=alembic

.PHONY: run migrate-up migrate-down migrate-create docker-up docker-down

run:
	uvicorn $(APP_MODULE) --host 0.0.0.0 --port 8000 --reload

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1

migrate-create:
	alembic revision --autogenerate -m "$(m)"

docker-up:
	docker compose up --build

docker-down:
	docker compose down -v
