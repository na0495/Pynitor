build:
	python setup.py sdist bdist_wheel

install:
	pip install .

run:
	pynitor