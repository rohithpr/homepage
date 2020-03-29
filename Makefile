reset:
	python manage.py reset_db --noinput
	python manage.py migrate
	python manage.py loaddata collections
	python manage.py loaddata items
