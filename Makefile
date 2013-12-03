deploy:
	sudo pip install -r requirements.txt

runserver:
	python caca_ao_tesouro/manage.py runserver  

syncdb:
	python caca_ao_tesouro/manage.py syncdb
