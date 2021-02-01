# Desafio - Semelhante a um banco imobiliário

## [Desafio](DESAFIO.md)

### Caso precise de ajuda com os comandos
> comando
```shell
❯ make help
```
> resultado
```shell
Comandos - Banco Imobiliario
Ajuda

uso: make <sub comando>
Sub comandos:
    run                                         Rodar projeto
    pkg_install_poetry                          Instalar o gerenciador de dependencia - Poetry
    pkg_install_dev                             Instalar dependencias no ambiente de desenvolvimento
    pkg_install_prod                            Instalar dependencias - 'requirements.txt' no ambiente de produção
    pkg_req_create                              Exportar arquivo 'requirements.txt'
    pkg_req_del                                 Apagar arquivo 'requirements.txt'
    pkg_add_dev pkg=nome_dependencia            Adicionar dependencia para desenvolvimento
    pkg_add_prod pkg=nome_dependencia           Adicionar dependencia para produção
    run_test                                    Rodar teste de cobertura de codigo e pytest com modular fixture
    run_test_to_html                            Exportar teste de cobertura de codigo em uma pasta 'htmlcov'
```

## Instalação
### 1º Instale o gerenciador de dependências
> comando
```shell
❯ make pkg_install_poetry
```
> resultado
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

$HOME/.poetry/bin

This path will then be added to your `PATH` environment variable by
modifying the profile file located at:

$HOME/.profile

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing version: 1.1.4
  - Downloading poetry-1.1.4-linux.tar.gz (57.03MB)

Poetry (1.1.4) is installed now. Great!

To get started you need Poetry's bin directory ($HOME/.poetry/bin) in your `PATH`
environment variable. Next time you log in this will be done
automatically.

To configure your current shell run `source $HOME/.poetry/env`
```

### 2º Instação do ambiente - Dev
> comando
```shell
❯ make pkg_install_dev
```
> resultado
```shell
poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: banco-imobiliario (0.1.0)
poetry shell
Spawning shell within /home/gladson/.cache/pypoetry/virtualenvs/banco-imobiliario-YHc5w1h_-py3.8
. /home/gladson/.cache/pypoetry/virtualenvs/banco-imobiliario-YHc5w1h_-py3.8/bin/activate

desafio-banco-imobiliario on  main [!⇡] is 📦 v0.1.0 via 🐍 v3.8.5 
❯ . /home/gladson/.cache/pypoetry/virtualenvs/banco-imobiliario-YHc5w1h_-py3.8/bin/activate
desafio-banco-imobiliario on  main [!⇡] is 📦 v0.1.0 via 🐍 v3.8.5 (banco-imobiliario-YHc5w1h_-py3.8)
```

### 3º Rodar o projeto
> comando
```shell
❯ make run
```
> resultado
```shell
make -C src run_main
make[1]: Entrando no diretório '/desafio-banco-imobiliario/src'
python -m main
Quantas partidas terminam por tempo esgotado(timeout): 38
Quantos turnos em média demora uma partida: 150.1
Qual o comportamento que mais venceu:
        impulsive
        venceu: 129
Qual a porcentagem de vitórias por comportamento dos jogadores
  *   impulsive: 43%
  *   demanding: 28%
  *   cautious: 23%
  *   randomer: 5%
make[1]: Saindo do diretório '/desafio-banco-imobiliario/src'
```

