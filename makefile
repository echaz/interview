# NOTE: This makefile is expected to be run locally, in a linux-y world.

build:
	docker build . -t echaz_interview

test:
	docker run --rm -t echaz_interview py.test tests.py

# runs the example sentence
run_example:
	docker run --rm -t echaz_interview python3 main.py The dog jumped over the fence too

# ipython, a super helpful interactive interpreter.  Unless you know what this, you 
# probably wont want it.
python-interactive:
	docker run --rm -ti echaz_interview ipython

# break into the container via bash, where you can run "python3 main.py <sentence>" to your hearts content
bash:
	docker run --rm -ti echaz_interview /bin/bash

