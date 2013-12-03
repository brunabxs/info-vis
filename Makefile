deploy:
	sudo pip install -r requirements.txt

runserver:
	python treasure_hunt/manage.py runserver  

syncdb:
	python treasure_hunt/manage.py syncdb
