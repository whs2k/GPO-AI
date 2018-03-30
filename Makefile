
DEBUG := 1


run:
	FLASK_APP=challenge.py FLASK_DEBUG=$(DEBUG) flask run

run_sim:
	FLASK_APP=challenge.py FLASK_DEBUG=$(DEBUG) LOC_SIM=1 flask run
