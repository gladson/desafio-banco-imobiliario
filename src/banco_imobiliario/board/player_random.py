from random import randint

from .base import BasePlayer


class PlayerRandom(BasePlayer):
    '''
    O jogador aleatório compra a propriedade
    que ele parar em cima com probabilidade
    de 50%.
    '''
    def _roles_to_payment(self, patrimony):
        if randint(0, 1) > 0:
            self.paid(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
