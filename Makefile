
DEBUG := 1


run:
	FLASK_APP=challenge.py FLASK_DEBUG=$(DEBUG) flask run
