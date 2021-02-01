from banco_imobiliario.board.card_patrimony import Patrimony


def test_income_or_sale_player_demanding_less_than_50(
    board, player_impulsive, player_demanding
):
    patrimony = Patrimony(0, type_of_strategy=player_impulsive)
    patrimony.income = 49
    patrimony.property_price = 100
    player_demanding.income_or_sale(patrimony, board)
    assert player_demanding.money == 51


def test_sale_patrimony_player_impulsive(player_impulsive):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price = 100
    player_impulsive.income_or_sale(patrimony)
    assert player_impulsive.money >= 200
    assert player_impulsive.gameover == False


def test_sale_patrimony_player_random(player_randomer):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price >= 150
    player_randomer.income_or_sale(patrimony)
    assert player_randomer.money > 100
    assert player_randomer.gameover == False

def test_income_or_sale_player_demanding_less_than_50(
    board, player_demanding
):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.income = 40
    patrimony.property_price = 200
    player_demanding.income_or_sale(patrimony, board)
    assert player_demanding.money >= 100


def test_income_or_sale_player_demanding_more_than_50(
    board, player_demanding
):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.income = 60
    patrimony.property_price = 60
    player_demanding.income_or_sale(patrimony, board)
    assert player_demanding.money >= 50


def test_income_or_sale_player_player_cautious_cant_sale(
    board, player_cautious
):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.income = 100
    patrimony.property_price = 50
    player_cautious.income_or_sale(patrimony, board)
    assert player_cautious.money >= 100


def test_income_or_sale_player_player_cautious_can_sale(
    board, player_cautious
):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.income = 100
    patrimony.property_price = 20
    player_cautious.income_or_sale(patrimony, board)
    assert player_cautious.money >= 80
