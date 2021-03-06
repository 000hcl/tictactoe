from math import inf
import src.game_ui as x
import time


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
            map = Determines which spots on the board are significant to the game.
            turn = turn of the game.
            x = the amount of symbols that are needed to get in a row to win the game.
            player_starts = True if the player starts the game.
        """
        self.n = 30
        self.board = self.__new_board(self.n)
        self.board_map = self.__new_board(self.n)
        self.min_index = inf
        self.max_index = -1
        self.player_starts = True
        self.x = 5

    def remap(self):
        """
        Updates the map.
        """
        for i in range(self.n*(self.n-1)):
            if ((i+1) % self.n != 0):
                scan = self.scan(i)
                if scan:
                    if self.board_map[i] == 0:
                        self.board_map[i] = 1
                    if self.board_map[i+1] == 0:
                        self.board_map[i+1] = 1
                    if self.board_map[i+self.n] == 0:
                        self.board_map[i+self.n] = 1
                    if self.board_map[i+self.n+1] == 0:
                        self.board_map[i+self.n+1] = 1


    def scan(self, i):
        """
        Finds out if i is adjacent to a placed token on the map.

        Args:
            i = index of the top-left corner of the area to be scanned.

        Returns:
            True if the given spot is "adjacent" to a placed token.
            False if the given spot is not "adjacent" to a placed token.
        """

        if (self.horizontal_check(i, 2, self.board_map) >= 100) or (self.vertical_check(i, 2, self.board_map) >= 100) or (self.rd_diagonal_check(i, 2, self.board_map) >= 100) or (self.board_map[i] >= 100):
            return True
        else:
            return False

    def __new_board(self, n):
        """
        Creates a new board.
        Args:
            n = the length of one side of the board.
        Returns:
            The created game board.
        """
        board = [0 for _ in range(n*n)]
        return board

    def player_move(self):
        """
        Places the player's token on the board by asking for input.
        """
        move = x.request_move(0, self.n*self.n-1, self.board)
        self.board_map[move] = 100
        self.board[move] = 1
        self.set_max_min_indices(move)

    def set_max_min_indices(self, i):
        """
        Updates min_index and max_index.
        """
        if self.max_index < i:
            self.max_index = i
        if self.min_index > i:
            self.min_index = i

    def ai_move(self):
        """
        Assesses which move is best for the AI to take and places the AI's token on the board.
        """
        time_start = time.time()
        if sum(self.board_map) == 0:
            move = 404
        else:
            move = self.ai_best_move()
        self.board[move] = 10
        self.board_map[move] = 100
        self.set_max_min_indices(move)
        time_stop = time.time()
        time_difference = time_stop - time_start
        print("Time taken: ",time_difference)



    def end(self):
        """
        Checks if the game has ended and prints the appropriate message.
        """
        winner = self.check_winner(self.x, self.board)
        if winner != 0:
            if winner > 0:
                winner_text = "AI"
            else:
                winner_text = "player"
            x.winner_message(winner_text)
            return True

        if self.check_tie(self.board):
            x.tie_message()
            return True
        return False

    def start_game_AI_start(self):
        """
        Starts the game.
        """
        self.player_starts = False
        while True:

            self.ai_move()
            x.print_board(self.board, self.n)
            if self.end():
                break
            self.remap()
            self.player_move()
            if self.end():
                break
            self.remap()

    def start_game_player_start(self):
        """
        Starts the game, player starts.
        """
        while True:

            x.print_board(self.board, self.n)
            self.player_move()
            self.remap()
            if self.end():
                break
            self.ai_move()
            if self.end():
                break
            self.remap()

    def check_tie(self, board):
        """
        Checks if the game has ended in a tie.
        Args:
            board: Which game board to check.
        """
        if 0 in board:
            return False
        return True

    def check_winner(self, x, board):
        """
        Checks if someone has won the game, returns the winner.
        Returns:
            An integer < 0: If the player has won.
            An integer > 0: If the AI has won.
            0: If there is no winner.
        """
        return self.find_board_score(x, x, board, True)

    def find_board_score(self, x, value, board, real):
        """
        Finds "value" amounts of tokens in rows of x.

        Args:
            x = the "range"
            value = The desired amount of matches in a range.
                (example: x=5, value=4 means 4 tokens in a line
                 with the length of 5 increases the score for
                 the owner of the tokens.)
            board = the board to inspect
            real = 
                True if a game ending win is desired
                False if a guaranteed future win is also acceptable.

        Returns:
            board value
        """
        x_value = 0
        o_value = 0
        for i in range(self.n*self.n):
            if (i > self.max_index) or (i < self.min_index - x - 1 - (x-1)*self.n):
                continue
            if i % self.n <= self.n-x:
                horizontal = self.horizontal_check(i, x, board)
                horizontal_in_row = self.horizontal_check(i, value, board)
                if horizontal == value == horizontal_in_row:
                    x_value += 1
                elif horizontal == (value*10) == horizontal_in_row:
                    o_value += 1
                if not real:
                    if horizontal == value - 1:
                        x_value += 0.5
                    elif horizontal == (value - 1)*10:
                        o_value += 0.5

            if i < self.n*self.n - self.n*(x-1):
                vertical = self.vertical_check(i, x, board)
                vertical_in_row = self.vertical_check(i, value, board)
                if vertical == value == vertical_in_row:
                    x_value += 1
                elif vertical == value*10 == vertical_in_row:
                    o_value += 1
                if not real:
                    if vertical == value-1:
                        x_value += 0.5
                    elif vertical == (value - 1)*10:
                        o_value += 0.5

            if (i < self.n*self.n - self.n*(x-1)) and (i % self.n <= self.n-x):
                rd_diagonal = self.rd_diagonal_check(i, x, board)
                rd_diagonal_in_row = self.rd_diagonal_check(i, value, board)
                if rd_diagonal == value == rd_diagonal_in_row:
                    x_value += 1
                elif rd_diagonal == value*10 == rd_diagonal_in_row:
                    o_value += 1
                if not real:
                    if rd_diagonal_in_row == value-1:
                        x_value += 0.5
                    elif rd_diagonal_in_row == (value-1)*10:
                        o_value += 0.5

            if (i < self.n*self.n - self.n*(x-1)) and (i % self.n >= x-1):
                ld_diagonal = self.ld_diagonal_check(i, x, board)
                ld_diagonal_in_row = self.ld_diagonal_check(i, value, board)
                if ld_diagonal == value == ld_diagonal_in_row:
                    x_value += 1
                elif ld_diagonal == value*10 == ld_diagonal_in_row:
                    o_value += 1
                if not real:
                    if ld_diagonal_in_row == value-1:
                        x_value += 0.5
                    elif ld_diagonal_in_row == (value-1)*10:
                        o_value += 0.5

        if self.player_starts:
            if x_value > o_value:
                return - x_value
            if o_value >= 1:
                return o_value
        else:
            if o_value > x_value:
                return o_value
            if x_value >= 1:
                return - x_value

        return 0

    def vertical_check(self, i, x, board):
        """
        Finds the sum of a x length vertical line, starting at i.

        Args:
            i = Starting index
            x = length of line
            board = the board to inspect

        Returns: sum of the given line

        """
        indices = range(i, i+(self.n*x), self.n)
        return sum(map(board.__getitem__, indices))

    def horizontal_check(self, i, x, board):
        """
        Finds the sum of a x length horizontal line, starting at i.

        Args:
            i = Starting index
            x = length of line
            board = the board to inspect

        Retrns: sum of the given line

        """
        return sum(board[i:i+x])

    def rd_diagonal_check(self, i, x, board):
        """
        Finds the sum of an x length right-down diagonal at i.

        Args:
            i = Starting index
            x = length of diagonal
            board = the board to inspect

        Returns: sum of the given diagonal
        """

        indices = range(i,i+x*self.n,self.n+1)
        return sum(map(board.__getitem__, indices))


    def ld_diagonal_check(self, i, x, board):
        """
        Finds the sum of an x length left-down diagonal at i.

        Args:
            i = Starting index
            x = length of diagonal
            board = the board to inspect

        Returns: sum of the given diagonal
        """
        indices = range(i,i+(x-1)*self.n,self.n-1)
        return sum(map(board.__getitem__, indices))

    def minmax(self, board, n, a, b, ai_turn, depth):
        """
        Finds the value of a move.
        Args:
            board: The game board to check.
            n: The length of one side of the board.
            a: alpha used in alpha-beta pruning
            b: beta used in alpha-beta pruning
            ai_turn: True if it's the AI's turn.
            depth: current depth of the game tree
        
        Returns: 
            The result of the minmax algorithm.
        """
        winner_true = self.find_board_score(5, 5, board, True)
        if winner_true != 0:
            return winner_true*100000000

        if (depth > 1):
            winner_5 = self.find_board_score(5, 5, board, False)
            if (winner_5 != 0):
                return winner_5*1000000

            winner_4 = self.find_board_score(5, 4, board, False)

            if (winner_4 != 0):
                return winner_4*10000

            winner_3 = self.find_board_score(5, 3, board, False)

            if (winner_3 != 0):
                return winner_3*100

            winner_2 = self.find_board_score(5, 2, board, False)

            if (winner_2 != 0):
                return winner_2

            return 0

        if ai_turn:
            value = -inf

            for i in range(n*n):
                new_board = board.copy()
                if (new_board[i] == 0) and (self.board_map[i] == 1):
                    new_board[i] = 10
                    value = max(value, self.minmax(
                        new_board, n, a, b, False, depth + 1))

                    if value >= b:
                        break
                    a = max(a, value)
            return value
        else:
            value = inf
            for i in range(n*n):
                new_board = board.copy()
                if (new_board[i] == 0) and (self.board_map[i] == 1):
                    new_board[i] = 1
                    value = min(value, self.minmax(
                        new_board, n, a, b, True, depth + 1))
                    if value <= a:
                        break
                    b = min(b, value)
            return value

    def ai_best_move(self):
        """
        Finds the best move for the AI.
        Returns: The best move to make for the AI.
        """
        if sum(self.board) == 0:
            return 1
        best_value = -inf
        best_move = -1
        for i in range(self.n*self.n):
            new_board = self.board.copy()
            if (self.board[i] == 0) and (self.board_map[i] == 1):
                new_board[i] = 10
                new_value = self.minmax(
                    new_board, self.n, -inf, inf, False, 1)
                if new_value > best_value:

                    best_value = new_value
                    best_move = i
                if best_value >= 100000000:
                    return best_move
        return best_move