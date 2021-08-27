
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
        """
        self.n = n
        self.board = self.__new_board(self.n)
        self.map = self.__new_board(self.n)
        self.turn = 1
        self.player_starts = True
        # TEMPORARY:
        if self.n == 4:
            self.x = 4
        elif self.n == 3:
            self.x = 3
        else:
            self.x = 5

    def remap(self):
        """
        Updates the map.
        """
        for i in range(self.n*(self.n-1)):
            if ((i+1) % self.n != 0):
                scan = self.scan(i)
                if scan:
                    if self.map[i] == 0:
                        self.map[i] = 1
                    if self.map[i+1] == 0:
                        self.map[i+1] = 1
                    if self.map[i+self.n] == 0:
                        self.map[i+self.n] = 1
                    if self.map[i+self.n+1] == 0:
                        self.map[i+self.n+1] = 1

    def get_depth(self):
        """
        Finds the max depth of the game tree.

        Returns: the depth of the tree.
        """
        sum = 0
        for x in self.map:
            if x == 1:
                sum += 1
        # print("depth",sum)
        return sum

    def scan(self, i):
        """
        Finds out if i is adjacent to a placed token on the map.

        Args:
            i = index of the top-left corner of the area to be scanned.

        Returns:
            True if the given spot is "adjacent" to a placed token.
            False if the given spot is not "adjacent" to a placed token.
        """

        if (self.horizontal_check(i, 2, self.map) >= 100) | (self.vertical_check(i, 2, self.map) >= 100) | (self.rd_diagonal_check(i, 2, self.map) >= 100) | (self.map[i] >= 100):

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
        # TODO: Needs input verification
        """
        Places the player's token on the board by asking for input.
        """
        move = int(input("Your move:"))
        if move == -1:
            return
        self.map[move] = 100
        self.board[move] = 1

    def print_board(self, board):
        """
        Prints the game board.
        """
        print("Board:")
        st = ""
        for x in range(self.n*self.n):
            if board[x] == 0:
                if len(str(x)) == 1:
                    st += "[ " + str(x)+" ]"
                elif len(str(x)) == 2:
                    st += "[" + str(x)+" ]"
                else:
                    st += "["+str(x)+"]"
            elif board[x] == 1:
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
        depth = self.get_depth()
        if sum(self.map) == 0:
            move = 404
        else:
            move = self.ai_best_move()
        self.board[move] = 10
        self.map[move] = 100
        print("AI moves to", move)

    def end(self):
        #TODO: WIP
        """
        Checks if the game has ended and exits if it has.
        """
        winner = self.check_winner(self.x, self.board)
        if winner != 0:
            print("WINNER:", winner)
            #print(self.board, self.wins)
            exit()
        if self.check_tie(self.board):
            print("GAME ENDED IN TIE")
            print(self.board)
            exit()

    def start_game(self):
        """
        Starts the game.
        """
        self.player_starts = False
        while True:

            self.turn += 1
            self.ai_move()
            self.print_board(self.board)
            #print(self.board)
            self.end()
            self.remap()
            self.player_move()
            self.end()
            self.remap()
    
    def start_game_alt(self):
        """
        Starts the game, player starts.
        """
        while True:

            self.turn += 1
            self.print_board(self.board)
            self.player_move()
            self.remap()
            self.end()
            self.ai_move()
            self.remap()
            self.end()
            #print(self.board)
            
            

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
            1: If the player has won.
            10: If the AI has won.
            None: If there is no winner.
        """
        return self.find_winner(x, x, board, True)


    def find_winner(self, x, value, board, real):
        """
        Checks if there is a "winner" on the board.

        Args:
            x = the "range"
            value = The desired amount of matches in a range.
                (example: x=5, value=4 means 4 tokens in a line
                 with the length of 5 is a "win")
            board = the board to inspect
            real = 
                True if a game ending win is desired
                False if a guaranteed future win is also acceptable.

        Returns:
            1 if the player is a winner.
            10 if the AI is a winner.
        """
        x_value = 0
        o_value = 0
        for i in range(self.n*self.n):
            if i % self.n <= self.n-x:
                horizontal = self.horizontal_check(i, x, board)
                if horizontal == value:
                    x_value += 1
                elif horizontal == value*10:
                    o_value += 1
                if (real == False) & (i % self.n <= self.n-x-1):
                    if (horizontal == value-1) & (board[i] == 0) & (board[i+x] == 0):
                        x_value += 1
                    if (horizontal == (value*10)-10) & (board[i] == 0) & (board[i+x] == 0):
                        o_value += 1
                if (real == False):
                    if horizontal == value-1:
                        x_value += 0.5
                    if horizontal == value*10 - 10:
                        o_value += 0.5

            if i < self.n*self.n - self.n*(x-1):
                vertical = self.vertical_check(i, x, board)
                if vertical == value:
                    x_value += 1
                elif vertical == value*10:
                    o_value += 1

                if (real == False) & (i < self.n*self.n - self.n*(x)):
                    if (vertical == value-1) & (board[i] == 0) & (board[i+(self.n*x)] == 0):
                        x_value += 1
                    if (vertical == (value*10)-10) & (board[i] == 0) & (board[i+(self.n*x)] == 0):
                        o_value += 1
                if (real == False):
                    if vertical == value-1:
                        x_value += 0.5
                    if vertical == value*10 - 10:
                        o_value += 0.5

            if (i < self.n*self.n - self.n*(x-1)) & (i % self.n <= self.n-x):
                rd_diagonal = self.rd_diagonal_check(i, x, board)
                if rd_diagonal == value:
                    x_value += 1
                elif rd_diagonal == value*10:
                    o_value += 1

                if (real == False) & (i < self.n*self.n - self.n*(x)) & (i % self.n <= self.n-x-1):
                    if (rd_diagonal == value-1) & (board[i] == 0) & (board[i+x*(self.n+1)] == 0):
                        x_value += 1
                    if (rd_diagonal == 10*value-10) & (board[i] == 0) & (board[i+x*(self.n+1)] == 0):
                        o_value += 1

                if (real == False):
                    if rd_diagonal == value-1:
                        x_value += 0.5
                    if rd_diagonal == value*10 - 10:
                        o_value += 0.5

            if (i < self.n*self.n - self.n*(x-1)) & (i % self.n >= x-1):
                ld_diagonal = self.ld_diagonal_check(i, x, board)
                if ld_diagonal == value:
                    x_value += 1
                elif ld_diagonal == value*10:
                    o_value += 1

                if (real == False) & (i < self.n*self.n - self.n*(x)) & (i % self.n >= x):
                    
                    if (ld_diagonal == value-1) & (board[i] == 0) & (board[i+x*(self.n-1)] == 0):
                        x_value += 1
                    if (ld_diagonal == 10*value-10) & (board[i] == 0) & (board[i+x*(self.n-1) == 0]):
                        o_value += 1
                if (real == False):
                    if ld_diagonal == value-1:
                        x_value += 0.5
                    if ld_diagonal == value*10 - 10:
                        o_value += 0.5
        
        if self.player_starts:
            if x_value >= 1:
                return 1
            if o_value >= 1:
                return 10
        else:
            if o_value >= 1:
                return 10
            if x_value >= 1:
                return 1
        
        
        

        return 0

    def vertical_check(self, i, x, board):
        """
        Finds the sum of a x length vertical line, starting at i.

        Args:
            i = Starting index
            x = length of line
            board = the board to inspect

        Retrns: sum of the given line

        """
        sum = 0
        for s in range(x):
            sum += board[i+(s*self.n)]
        # return board[i] + board[i+x] + board[i+2*x] + board[i+3*x] + board[i+4*x]
        return sum

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
        sum = 0
        for s in range(x):
            sum += board[i+s*(self.n+1)]
        return sum

    def ld_diagonal_check(self, i, x, board):
        """
        Finds the sum of an x length left-down diagonal at i.

        Args:
            i = Starting index
            x = length of diagonal
            board = the board to inspect

        Returns: sum of the given diagonal
        """
        sum = 0
        for s in range(x):
            sum += board[i+s*(self.n-1)]
        return sum

    def ai_best_move(self):
        """
        Finds the best move for the AI.
        Returns: The best move to make for the AI.
        """
        if sum(self.board) == 0:
            return 1
        best_value = -100
        best_move = -1
        self.depth = self.get_depth()
        for i in range(self.n*self.n):
            # print(i)

            new_board = self.board.copy()
            if (self.board[i] == 0) & (self.map[i] == 1):
                new_board[i] = 10
                new_value = self.minmax(new_board, self.n, -100, 100, False, 1)
                print(i, new_value)
                if new_value > best_value:

                    best_value = new_value
                    best_move = i
                #print(i, best_value)
                if best_value == 10:
                    return best_move
        return best_move

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
        """
        winner_true = self.find_winner(5, 5, board, True)

        if (winner_true == 1):
            return -10
        if (winner_true == 10):
            return 10
        


        
        

        if (depth > 1):
            winner_5 = self.find_winner(5, 5, board, False)
            if (winner_5 == 1):
                return -9
            if (winner_5 == 10):
                return 9

            winner_4 = self.find_winner(5, 4, board, False)

            if (winner_4 == 1):
                return -8
            if (winner_4 == 10):
                return 8
            
            winner_3 = self.find_winner(5, 3, board, False)

            if (winner_3 == 1):
                return -6
            if (winner_3 == 10):
                return 6

        
            
            """
            winner_2 = self.find_winner(5, 2, board, False)
            
            if (winner_2 == 1):
                return -4
            if (winner_2 == 10):
                return 4
            
            """
            #if self.check_tie(board) | (depth >= self.depth):
            #    return 0
            return 0

        if ai_turn:
            value = -100

            for i in range(n*n):
                new_board = board.copy()
                if (new_board[i] == 0) & (self.map[i] == 1):
                    new_board[i] = 10
                    value = max(value, self.minmax(
                        new_board, n, a, b, False, depth + 1))

                    if value >= b:
                        break
                    a = max(a, value)
                    # print("max",i,value)
            return value
        else:
            value = 100
            for i in range(n*n):
                new_board = board.copy()
                if (new_board[i] == 0) & (self.map[i] == 1):
                    new_board[i] = 1
                    value = min(value, self.minmax(
                        new_board, n, a, b, True, depth + 1))
                    if value <= a:
                        break
                    b = min(b, value)
                    # print("min",i,value)
            return value