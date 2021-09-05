import src.ui.tools as tool


def request_move(minimum, maximum, board):
    """
    Asks the user to give a move.

    Args:
        minimum: The minimum allowed value
        maximum: The maximum allowed value.
    """
    raw = input("Your move: ")
    converted = tool.attempt_int_conversion(raw, minimum, maximum)
    if not converted:
        return request_move(minimum, maximum, board)
    else:
        if board[converted] != 0:
            print("This square is taken. Please try another one.")
            return request_move(minimum, maximum, board)
        return converted

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