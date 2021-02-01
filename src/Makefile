run_main:
	python -m main

run_main_flake8_isort:
	flake8 banco_imobiliario/*.*
	isort **/*.py

run_main_test: run_main_flake8_isort
	pytest --cov-append --cov=banco_imobiliario tests/

run_main_test_to_html:
	rm -rf htmlcov
	pytest --cov-report html --cov=banco_imobiliario tests/