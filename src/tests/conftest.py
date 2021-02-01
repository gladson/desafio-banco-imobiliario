import pytest

from banco_imobiliario import __version__
from banco_imobiliario.board.factory import create_board, create_player
from banco_imobiliario.config import settings


@pytest.fixture
def test_version():
    '''
    teste de verificação da versão do projeto
    '''
    assert __version__ == '0.1.0'

@pytest.fixture(scope='session', autouse=True)
def set_test_settings():
    settings.configure(ENV_FOR_DYNACONF='testing')


@pytest.fixture
def board(set_test_settings):
    return create_board()


@pytest.fixture
def player_impulsive():
    return create_player('impulsive')


@pytest.fixture
def player_demanding():
    return create_player('demanding')


@pytest.fixture
def player_cautious():
    return create_player('cautious')


@pytest.fixture
def player_randomer():
    return create_player('randomer')
