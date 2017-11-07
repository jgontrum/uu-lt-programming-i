.PHONY: all clean

PIPOPTIONS=

all: env/bin/python

env/bin/python:
	python3 -m venv env
	env/bin/pip install $(PIPOPTIONS) --upgrade pip
	env/bin/pip install $(PIPOPTIONS) wheel
	env/bin/pip install $(PIPOPTIONS) -r requirements.txt
	env/bin/python setup.py develop

clean:
	rm -rfv bin develop-eggs dist downloads eggs env parts
	rm -fv .DS_Store .coverage .installed.cfg bootstrap.py
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;
