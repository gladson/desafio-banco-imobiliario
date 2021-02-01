default: help

help:
	@echo "Comandos - Banco Imobiliario"
	@echo "Ajuda"
	@echo
	@echo  "uso: make <sub comando>"
	@echo  "Sub comandos:"
	@echo  "    run""					        ""Rodar projeto"
	@echo  "    pkg_install_poetry""				""Instalar o gerenciador de dependencia - Poetry"
	@echo  "    pkg_install_dev""				""Instalar dependencias no ambiente de desenvolvimento"
	@echo  "    pkg_install_prod""				""Instalar dependencias - 'requirements.txt' no ambiente de produção"
	@echo  "    pkg_req_create""				""Exportar arquivo 'requirements.txt'"
	@echo  "    pkg_req_del""					""Apagar arquivo 'requirements.txt'"
	@echo  "    pkg_add_dev pkg=nome_dependencia""		""Adicionar dependencia para desenvolvimento"
	@echo  "    pkg_add_prod pkg=nome_dependencia""		""Adicionar dependencia para produção"
	@echo  "    run_test""					""Rodar teste de cobertura de codigo e pytest com modular fixture"
	@echo  "    run_test_to_html""				""Exportar teste de cobertura de codigo em uma pasta 'htmlcov'"

pkg_req_del:
	rm -rf requirements.txt

pkg_install_poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

pkg_req_create:
	poetry export -f requirements.txt -o requirements.txt

pkg_install_dev:
	poetry install
	poetry shell

pkg_install_prod: pkg_req_del pkg_req_create
	pip install --require-hashes -r requirements.txt

pkg_add_dev:
	poetry add -D ${pkg}

pkg_add_prod:
	poetry add ${pkg}

pkg_search:
	poetry search ${pkg}

pkg_list_env:
	poetry env list

pkg_info_env:
	poetry env info

run_test:
	$(MAKE) -C src run_main_test

run_test_to_html: run_test
	$(MAKE) -C src run_main_test_to_html

run:
	$(MAKE) -C src run_main