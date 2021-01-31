default: help

help:
	@echo "Comandos - Banco Imobiliario"
	@echo "Ajuda"
	@echo
	@echo  "uso: make <sub comando>"
	@echo  "Sub comandos:"
	@echo  "    pkg_req_del""					""Apagar arquivo 'requirements.txt'"
	@echo  "    pkg_req_create""				""Exportar arquivo 'requirements.txt'"
	@echo  "    pkg_install_prod""				""Instalar dependencias - 'requirements.txt' no ambiente de produção"
	@echo  "    pkg_add_dev pkg=nome_dependencia""		""Adicionar dependencia para desenvolvimento"
	@echo  "    pkg_add_prod pkg=nome_dependencia""		""Adicionar dependencia para produção"
	@echo  "    run_test""					""Rodar teste de cobertura de codigo e pytest com modular fixture"
	@echo  "    run_test_to_html""				""Exportar teste de cobertura de codigo em uma pasta 'htmlcov'"


pkg_req_del:
	rm -rf requirements.txt

pkg_req_create:
	poetry export -f requirements.txt -o requirements.txt

pkg_install_prod: pkg_req_del pkg_req_create
	pip install --require-hashes -r requirements.txt

pkg_add_dev:
	poetry add -D ${pkg}

pkg_add_prod:
	poetry add ${pkg}

run_test:
	rm -rf ./.coverage
	pytest --cov-append --cov=banco_imobiliario tests/

run_test_to_html: run_test
	rm -rf htmlcov
	pytest --cov-report html --cov=banco_imobiliario tests/