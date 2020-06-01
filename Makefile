build:
	docker-compose build

up:
	docker-compose up

bash:
	docker exec -it homepage_web_1 bash

reset:
	python manage.py reset_db --noinput -c
	python manage.py migrate
	python manage.py loaddata collections
	python manage.py loaddata items
