install:
	pip3 install .

test:
	FLASK_ENV=test pytest tests/ -v