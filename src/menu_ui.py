import src.board as board
from src.tools import attempt_int_conversion

def menu():
    """
    Main menu loop.
    """
    while True:
        print("1: start a game where the player starts.")
        print("2: start a game where the AI starts.")
        print("0: Exit program.")
        raw = input("Your input: ")
        converted = attempt_int_conversion(raw, 0, 2)
        if converted == 1:
            game = board.Board(30)
            game.start_game_player_start()
        elif converted == 2:
            game = board.Board(30)
            game.start_game_AI_start()
        elif converted == 0:
            exit()