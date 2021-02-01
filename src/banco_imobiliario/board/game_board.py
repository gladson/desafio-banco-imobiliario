from datetime import datetime
from random import randint

from banco_imobiliario.config import settings

from .card_patrimony import Patrimony


class GameBoard:

    def __init__(self, *args, **kwargs):
        self._winner = None
        self._played = 0
        self._players = []
        self.start_time = datetime.now()
        self._cards = [
            Patrimony(index, None)
            for index in range(
                int(settings.ENV_QUANTITY_OF_PROPERTIES)
            )
        ]

    @property
    def played(self):
        return self._played

    @played.setter
    def played(self, played):
        self._played = played

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner):
        self._winner = winner

    @property
    def play_dice(self):
        '''
        No começo da sua vez, o jogador joga um
        dado equiprovável de 6 faces que determina
        quantas espaços no tabuleiro o jogador vai
        andar.
        '''
        return randint(1, 6)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, patrimony):
        self._cards[position] = patrimony

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"

    def __repr__(self):
        return f"{self._cards}"

    def remove(self, player):
        for patrimony in self._cards:
            if patrimony.type_of_strategy == player:
                patrimony.type_of_strategy = None
        self._players.remove(player)

    def walk(self, player, _dice=None):
        go_to_position = player.position + (_dice or self.play_dice)
        if go_to_position >= int(settings.ENV_QUANTITY_OF_PROPERTIES):
            '''
            Ao completar uma volta no tabuleiro,
            o jogador ganha 100 de saldo.
            '''
            player.money += float(settings.ENV_PLAYER_MONEY_ROUND)
            go_to_position -= int(settings.ENV_QUANTITY_OF_PROPERTIES)
        player.position = go_to_position
        return go_to_position

    def check_winner(self, player):
        '''
        Termina quando restar somente um jogador
        com saldo positivo, a qualquer momento da
        partida. Esse jogador é declarado o
        vencedor.
        '''
        if len(self.players) == 1:
            return player
        if int(settings.ENV_TIMEOUT_ROUND) <= self.played:
            money = 0
            winner = None
            for _player in self._players:
                if _player.money > money:
                    money = _player.money
                    winner = _player
            return winner

        elements = [
            _player.money
            for _player in self._players if _player != player
        ]
        if sum(elements) < 0:
            return player

        return None

    def play(self, player, board):
        '''
        Um jogador que fica com saldo negativo
        perde o jogo, e não joga mais. Perde
        suas propriedades e portanto podem ser
        compradas por qualquer outro jogador.
        '''
        if player.money <= 0:
            player.gameover = True
            return

        patrimony = self._cards[self.walk(player)]
        player.income_or_sale(patrimony, board)

    def finish(self):
        return {
            "time_it": (datetime.now() - self.start_time).total_seconds(),
            "winner": self.winner,
            "money": self.winner.money,
            "played": self.played,
            "strategy": self.winner,
            "time_out": self.played > int(settings.ENV_TIMEOUT_ROUND),
        }
