from banco_imobiliario.config import settings

from banco_imobiliario.board.factory import create_board
from banco_imobiliario.board.game_statistics import show_statistics


def main():
    '''
    Uma execução do programa proposto deve rodar 300
    simulações, imprimindo no console os dados
    referentes às execuções.
    '''
    results = []
    for index in range(int(settings.ENV_NUMBER_SIMULATION)):
        board = create_board()
        while board.winner is None:
            for player in board.players:
                if player.gameover:
                    board.remove(player)
                winner = board.check_winner(player)
                if winner:
                    board.winner = winner
                    break
                board.play(player, board)
            board.played += 1
        results.append(board.finish())
    show_statistics(results)


if __name__ == "__main__":
    main()
