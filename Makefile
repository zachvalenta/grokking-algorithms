.PHONY: test

help:
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "cov:     view HTML coverage report in browser"
	@echo "fmt:     auto format code using Black"
	@echo "lint:    lint using flake8"
	@echo "test:    run unit tests, view basic coverage report in terminal"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "pipfr:   freeze dependencies into requirements.txt"
	@echo "pipin:   install dependencies from requirements.txt"
	@echo "piprs:   remove any installed pkg *not* in requirements.txt"
	@echo

cov:test
	coverage html; open htmlcov/index.html

fmt:
	black src test

lint:
	flake8 src

pipfr:
	pip freeze > requirements.txt

pipin:
	pip install -r requirements.txt

piprs:
	pip freeze > pkgs-to-rm.txt
	pip uninstall -y -r pkgs-to-rm.txt
	rm pkgs-to-rm.txt
	pip install -r requirements.txt

test:
	coverage run --source='src' -m pytest -v && coverage report -m
