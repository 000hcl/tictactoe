
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
        self.map = [-1 for _ in range(self.n*self.n)]
        self.turn = 1
        # TEMPORARY:
        if self.n == 4:
            self.x = 4
        elif self.n == 3:
            self.x = 3
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
        self.board[move] = 1

    def print_board(self):
        """
        Prints the game board.
        """
        board = self.board
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
        """
        if sum(self.board) == 1:
            for p in range(self.n*self.n):
                if self.board[p] == 1:
                    s = p
            if s%self.n != 0:
                move = s+1
            else:
                move = s-1
        else:
            pass
        """
        move = self.ai_best_move()
        self.board[move] = 10
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
        while True:
            self.end()
            self.print_board()
            self.turn += 1
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
        if 0 in board:
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
            if result != 0:
                self.wins = wins
                
                return result
        return 0
        
        #return self.find_winner(x, board)

    def find_winner(self, x, board):
        #notes for self:
        # horizintal: 0 - n-x
        for i in range(self.n*self.n):
            if i%self.n <= self.n-x:
                horizontal = self.horizontal_check(i, x, board)
                if horizontal == x:
                    return 1
                elif horizontal == x:
                    return 10
            if i < self.n*self.n - self.n*(x-1):
                vertical = self.vertical_check(i, x, board)
                if vertical == x:
                    return 1
                elif vertical == x:
                    return 10
            if (i < self.n*self.n - self.n*(x-1)) & (i%self.n <= self.n-x):
                rd_diagonal = self.rd_diagonal_check(i, x, board)
                if rd_diagonal == x:
                    return 1
                elif rd_diagonal == x:
                    return 10
            if (i < self.n*self.n - self.n*(x-1)) & (i % self.n >= x-1):
                ld_diagonal = self.ld_diagonal_check(i, x, board)
                if ld_diagonal == x:
                    return 1
                elif ld_diagonal == x:
                    return 10
        return 0

    def vertical_check(self, i,x, board):
        #Currently made for 4x4
        return board[i] + board[i+x] + board[i+2*x] + board[i+3*x] + board[i+4*x]
    
    def horizontal_check(self,i,x,board):
        return sum(board[i:i+x])
    
    def rd_diagonal_check(self,i,x,board):
        sum = 0
        for s in range(x):
            sum += board[i+s*(x+1)]
        return sum
        #return board[i] + board[i+x+1] + board[i+2*(x+1)] + board[i+3*(x+1)] + board[i+4*(x+1)]

    def ld_diagonal_check(self,i,x,board):
        sum = 0
        for s in range(x):
            sum += board[i+s*(x-1)]
        return sum
        #return board[i] + board[i+x-1] + board[i+2*(x-1)] + board[i+3*(x-1)] + board[i+4*(x-1)]
    

    def ai_best_move(self):
        """
        Finds the best move for the AI.
        Returns: The best move to make for the AI.
        """
        if sum(self.board) == 0:
            return 1
        best_value = -100
        best_move = -1
        for i in range(self.n*self.n):
            print(i)
            new_board = self.board.copy()
            if self.board[i] == 0:
                new_board[i] = 10
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
        row_length = self.turn
        if row_length > self.x:
            row_length = self.x
        if self.check_winner(row_length, board) == 10:
            return 10
        if self.check_winner(row_length, board) == 1:
            return -10
        if self.check_tie(board):
            return 0

        if ai_turn:
            value = -100

            for i in range(n*n):
                new_board = board.copy()
                if new_board[i] == 0:
                    new_board[i] = 10
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
                if new_board[i] == 0:
                    new_board[i] = 1
                    value = min(value, self.minmax(new_board, n, a, b, True))
                    if value <= a:
                        break
                    b = min(b, value)
                    # print("min",i,value)
            return value