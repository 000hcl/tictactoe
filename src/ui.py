
import board

def request_move(minimum, maximum, board):
    """
    Asks the user to give a move.

    Args:
        minimum: The minimum allowed value
        maximum: The maximum allowed value.
    """
    raw = input("Your move: ")
    converted = attempt_int_conversion(raw, minimum, maximum)
    if not converted:
        return request_move(minimum, maximum, board)
    else:
        if board[converted] != 0:
            print("This square is taken. Please try another one.")
            return request_move(minimum, maximum, board)
        return converted

def attempt_int_conversion(number, minimum, maximum):
    """
    Checks if the input is can be converted into an integer between "minimum" and "maximum".

    Args:
        number: the input to be converted
        minimum: the minimum allowed value
        maximum: the maximum allowed value

    Returns:
        an integer if the conversion is successful
    """
    try:
        integer = int(number)
        if maximum >= integer >= minimum:
            return integer
        else:
            print("Invalid number. Please retry.")
    except:
        print("Invalid number. Please retry.")

def print_board(board, n):
    """
    Prints the game board.
    """
    print("Board:")
    string = ""
    for x in range(n*n):
        if board[x] == 0:
            if len(str(x)) == 1:
                string += "[ " + str(x)+" ]"
            elif len(str(x)) == 2:
                string += "[" + str(x)+" ]"
            else:
                string += "["+str(x)+"]"
        elif board[x] == 1:
            string += "[ X ]"
        else:
            string += "[ O ]"
        if (x+1) % n == 0:
            print(string)
            string = ""

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

def winner_message(winner):
    """
    Prints a message when a winner is found.
    """
    print("--- WINNER: ", winner, "---")

def tie_message():
    """
    Prints a message when the game has ended in a tie.
    """
    print("--- GAME ENDED IN A TIE ---")
