update_pip_and_wheel:
	pip install -U pip wheel

install_dev:
	pip install -e ".[dev,pdf]"

install_prod:
	pip install ".[pdf]"

wheel:
	pip install build twine
	python -m build . --wheel

pytest:
	pytest

pylint:
	pylint

mypy:
	mypy src

coverage_run:
	coverage run -m pytest

coverage_report:
	coverage report

coverage: coverage_run coverage_report

validate_before_push: \
	coverage \
	mypy

	#pylint \

