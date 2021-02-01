from abc import ABC, abstractmethod

from banco_imobiliario.config import settings


class BasePlayer(ABC):

    def __init__(
        self, strategy, position=0,
        money=settings.ENV_PLAYER_MONEY
    ):
        self.position = position
        self.money = money
        self.strategy = strategy
        self.gameover = False

    def __str__(self):
        return f"{self.strategy}"

    def __repr__(self):
        return f"{self.strategy}"

    def income_or_sale(self, patrimony, board=None):
        if patrimony.type_of_strategy:
            if self != patrimony.type_of_strategy:
                self.paid(patrimony.rental_price, patrimony.type_of_strategy)
            return

        if self._roles_to_payment(patrimony):
            patrimony.type_of_strategy = self

    @abstractmethod
    def _roles_to_payment(self, patrimony, board):
        raise NotImplementedError()

    def paid(self, property_price, type_of_strategy=None):
        self.money -= property_price
        if type_of_strategy:
            type_of_strategy.money += property_price
        if not self.money:
            self.gameover = True
