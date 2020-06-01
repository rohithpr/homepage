build:
	docker-compose build

up:
	docker-compose up

bash:
	docker exec -it homepage_web_1 bash

reset:
	docker-compose exec web ./manage.py reset_db --noinput -c
	docker-compose exec web ./manage.py migrate
	docker-compose exec web ./manage.py loaddata collections
	docker-compose exec web ./manage.py loaddata items
