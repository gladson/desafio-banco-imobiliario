from typing import Counter

from banco_imobiliario.config import settings


def test_quantity_of_properties(board):
    assert len(board) == int(settings.ENV_QUANTITY_OF_PROPERTIES)

def test_board_walk(board, player_impulsive):
    player_impulsive.position = 19
    assert board.walk(player_impulsive, 1) == 0

def test_board_check_winner(board, player_impulsive):
    for p in board.players:
        if player_impulsive != p:
            p.money = -1
    _player = board.check_winner(player_impulsive)
    board.winner = _player
    assert board.winner == player_impulsive

def test_board_quantity_of_players(board):
    assert sum(Counter(board.players).values()) == 4

def test_board_play_dice(board):
    assert board.play_dice in list(range(1, 7))
    assert type(board.play_dice) == int