.PHONY: clean-pyc clean-build docs clean
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 pyglobalgoals tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source pyglobalgoals setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs:
	rm -f docs/pyglobalgoals.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pyglobalgoals
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install

install-env:
	$(MAKE) conda-env-install


pip-freeze:
	# Note: these are not included in the git repo
	pip freeze > ./requirements.global.pipfreeze.txt
	pip freeze -l > ./requirements.local.pipfreeze.txt
	pip freeze --user > ./requirements.user.pipfreeze.txt


CONDAENV_NAME:=pyglobalgoals
conda-env-dump:
	conda env export -n=${CONDAENV_NAME} > environment.yml

conda-env-install:
	conda env create -n=${CONDAENV_NAME} -f=./environment.yml

conda-env-update:
	conda env update -n=${CONDAENV_NAME} -f=./environment.yml

ipython-notebook:
	ipython notebook .

jupyter-notebook:
	jupyter-notebook .

nbconvert:
	jupyter-nbconvert ./notebooks/*.ipynb --to python
	jupyter-nbconvert ./notebooks/*.ipynb --to html
