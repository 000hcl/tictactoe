class Board:
    """
    Represents a game board for the game tic tac toe.
    Args:
        n = length of one side of the board
    """

    def __init__(self, n):
        """
        Attributes:
            n = length of one side of the board
            board = The game board as a list.
            x = the amount of symbols that are needed to get in a row to win the game.
        """
        self.n = n
        self.board = self.__new_board(self.n)
        # TEMPORARY:
        if self.n == 3:
            self.x = 3
        if self.n == 4:
            self.x = 4
        else:
            self.x = 5

    def __new_board(self, n):
        """
        Creates a new board.
        Args:
            n = the length of one side of the board.
        Returns:
            The created game board.
        """
        board = [None for _ in range(n*n)]
        return board

    def player_move(self):
        # TODO: Needs input verification
        """
        Places the player's token on the board by asking for input.
        """
        move = int(input("Your move:"))
        if move == -1:
            return
        self.board[move] = "X"

    def print_board(self):
        """
        Prints the game board.
        """
        board = self.board
        print("Board:")
        st = ""
        for x in range(self.n*self.n):
            if board[x] == None:
                if len(str(x)) == 1:
                    st += "[ " + str(x)+" ]"
                elif len(str(x)) == 2:
                    st += "[" + str(x)+" ]"
                else:
                    st += "["+str(x)+"]"
            elif board[x] == "X":
                st += "[ X ]"
            else:
                st += "[ O ]"
            if (x+1) % self.n == 0:
                print(st)
                st = ""

    def ai_move(self):
        """
        Assesses which move is best for the AI to take and places the AI's token on the board.
        """
        #TODO: WIP
        move = self.ai_best_move()
        self.board[move] = "O"
        print("AI moves to", move)

    def end(self):
        #TODO: WIP
        """
        Checks if the game has ended and exits if it has.
        """
        if self.check_winner(self.x, self.board) != None:
            print("WINNER:", self.check_winner(self.x, self.board))
            print(self.board, self.wins)
            exit()
        if self.check_tie(self.board):
            print("GAME ENDED IN TIE")
            exit()

    def start_game(self):
        """
        Starts the game.
        """
        while True:
            self.end()
            self.print_board()
            self.player_move()
            self.end()
            self.ai_move()
            self.end()

    def check_tie(self, board):
        """
        Checks if the game has ended in a tie.
        Args:
            board: Which game board to check.
        """
        if None in board:
            return False
        return True

    def check_winner(self, x, board):
        """
        Checks if someone has won the game, returns the winner.
        Returns:
            "X": If the player has won.
            "O": If the AI has won.
            None: If there is no winner.
        """
        wins = []
        wins.append(self.check_verticals(x, board))
        wins.append(self.check_horizontal(x, board))
        wins.append(self.check_diagonal_rd(x, board))
        wins.append(self.check_diagonal_ld(x, board))

        for result in wins:
            if result != None:
                self.wins = wins
                return result
        return None

    def check_verticals(self, x, board):
        """
        Checks if there are x tokens of the same type (X or O) in a vertical row.
        Args:
            x: The amount of tokens that are needed in a row to win.
            board: The game board to check.
        """
        for i in range(self.n):
            count = 1
            for j in range(self.n, self.n*self.n, self.n):
                if board[i+j] != None:
                    if board[i+j] == board[i+j-self.n]:
                        count += 1
                        if count == x:
                            return board[i+j]
                    else:
                        count = 1
        return None

    def check_horizontal(self, x, board):
        """
        Checks if there are x tokens of the same type (X or O) in a horizontal row.
        Args:
            x: The amount of tokens that are needed in a row to win.
            board: The game board to check.
        """
        for i in range(0, self.n*self.n, self.n):
            count = 1
            for j in range(1, self.n):
                if board[i+j] != None:
                    if board[i+j] == board[i+j-1]:
                        count += 1
                        if count == x:
                            return board[i+j]
                    else:
                        count = 1
        return None

    def check_diagonal_rd(self, x, board):
        """
        Checks if there are x tokens of the same type (X or O) in a diagonal right-down row.
        Args:
            x: The amount of tokens that are needed in a row to win.
            board: The game board to check.
        """
        for i in range(0, self.n-x+1):
            count = 1
            for j in range(0, self.n*self.n-i-1, self.n+1):
                #board[i+j] = "a"
                
                if board[i+j] != None:
                    if board[i+j] == board[i+j+(self.n+1)]:
                        count += 1
                        if count == x:
                            #pass
                            return board[i+j]
                    else:
                        count = 1
                if (i+j+2) % self.n == 0:
                    break
                

        for i in range(2*self.n+1, self.n*(self.n-x+1)+2, self.n):
            count = 1
            for j in range(0, self.n*self.n-i, self.n+1):
                #board[i+j] = "X"
                if board[i+j] != None:
                    if board[i+j] == board[i+j-(self.n+1)]:
                        count += 1
                        if count == x:
                            #pass
                            return board[i+j]
                    else:
                        count = 1
        return None

    def check_diagonal_ld(self, x, board):
        """
        Checks if there are x tokens of the same type (X or O) in a diagonal left-down row.
        Args:
            x: The amount of tokens that are needed in a row to win.
            board: The game board to check.
        """
        for i in range(x-1, self.n):
            count = 1
            for j in range(0, self.n*(self.n-2), self.n-1):
                if (i+j) % self.n == 0:
                    break
                #board[i+j] = "a"

                if board[i+j] != None:
                    if board[i+j] == board[i+j+(self.n-1)]:
                        count += 1
                        if count == x:
                            return board[i+j]
                            #pass
                    else:
                        count = 1

        for i in range(3*self.n-2, self.n*(self.n-x+2), self.n):
            count = 1
            for j in range(0, self.n*self.n-i, self.n-1):
                #board[i+j] = "X"
                if board[i+j] != None:
                    if board[i+j] == board[i+j-(self.n-1)]:
                        count += 1
                        if count == x:
                            return board[i+j]
                            #pass
                    else:
                        count = 1

        return None

    def ai_best_move(self):
        """
        Finds the best move for the AI.
        Returns: The best move to make for the AI.
        """
        best_value = -100
        best_move = -1
        for i in range(self.n*self.n):
            new_board = self.board.copy()
            if self.board[i] == None:
                new_board[i] = "O"
                new_value = self.minmax(new_board, self.n, -100, 100, False)
                # print(i,new_value)
                if new_value > best_value:

                    best_value = new_value
                    best_move = i
        return best_move

    def minmax(self, board, n, a, b, ai_turn):
        """
        Finds the value of a move.
        Args:
            board: The game board to check.
            n: The length of one side of the board.
            a: alpha used in alpha-beta pruning
            b: beta used in alpha-beta pruning
            ai_turn: True if it's the AI's turn.
        """
        if self.check_winner(self.x, board) == "O":
            return 10
        if self.check_winner(self.x, board) == "X":
            return -10
        if self.check_tie(board):
            return 0

        if ai_turn:
            value = -100

            for i in range(n*n):
                new_board = board.copy()
                if new_board[i] == None:
                    new_board[i] = "O"
                    value = max(value, self.minmax(new_board, n, a, b, False))
                    if value >= b:
                        break
                    a = max(a, value)
                    # print("max",i,value)
            return value
        else:
            value = 100
            for i in range(n*n):
                new_board = board.copy()
                if new_board[i] == None:
                    new_board[i] = "X"
                    value = min(value, self.minmax(new_board, n, a, b, True))
                    if value <= a:
                        break
                    b = min(b, value)
                    # print("min",i,value)
            return value