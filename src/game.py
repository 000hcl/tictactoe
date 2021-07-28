# TEMPORARY
from math import sqrt


class Board:
    def __init__(self, n):
        """
        n = length of one side of the board
        """
        self.n = n
        self.board = self.new_board(self.n)
        # TEMPORARY:
        if self.n < 30:
            self.x = 3
        else:
            self.x = 5

    def new_board(self, n):
        board = [None for _ in range(n*n)]
        return board

    def player_move(self):
        # TODO: Needs input verification
        move = int(input("Your move:"))
        if move == -1:
            return
        self.board[move] = "X"

    def print_board(self):
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
        # WIP
        """
        for pos in range(self.n*self.n):
            if self.board[pos] == None:
                self.board[pos] = "O"
                return

        """
        move = self.ai_best_move()
        self.board[move] = "O"
        print("AI moves to", move)

    def end(self):
        if self.check_winner(self.x, self.board) != None:
            print("WINNER:", self.check_winner(self.x, self.board))
            print(self.board, self.wins)
            exit()
        if self.check_tie(self.board):
            print("GAME ENDED IN TIE")
            exit()

    def start_game(self):
        while True:
            self.end()
            self.print_board()
            self.player_move()
            self.end()
            self.ai_move()
            self.end()

    def check_tie(self, board):
        if None in board:
            return False
        return True

    def check_winner(self, x, board):
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
        for i in range(self.n):
            count = 1
            for j in range(self.n, self.n*self.n, self.n):
                if board[i+j] != None:
                    if board[i+j] == board[i+j-self.n]:
                        count += 1
                        if count == x:
                            return board[i+j]
        return None

    def check_horizontal(self, x, board):
        for i in range(0, self.n*self.n, self.n):
            count = 1
            for j in range(1, self.n):
                if board[i+j] != None:
                    if board[i+j] == board[i+j-1]:
                        count += 1
                        if count == x:
                            return board[i+j]
        return None

    def check_diagonal_rd(self, x, board):
        for i in range(0, self.n-x+1):
            count = 1
            for j in range(0, self.n*self.n-i-1, self.n+1):

                #self.board[i+j] = "a"
                if board[i+j] != None:
                    if board[i+j] == board[i+j+(self.n+1)]:
                        count += 1
                        if count == x:
                            # pass
                            return self.board[i+j]
                if (i+j+2) % self.n == 0:
                    break

        for i in range(2*self.n+1, self.n*(self.n-x)+1, self.n):
            count = 1
            for j in range(0, self.n*self.n-i, self.n+1):
                #board[i+j] = "X"
                if board[i+j] != None:
                    if board[i+j] == board[i+j-(self.n+1)]:
                        count += 1
                        if count == x:
                            # pass
                            return board[i+j]
        return None

    def check_diagonal_ld(self, x, board):
        # seems fine??
        for i in range(x-1, self.n):
            count = 1
            for j in range(0, self.n*(self.n-2), self.n-1):
                if (i+j) % self.n == 0:
                    break
                #self.board[i+j] = "a"

                if board[i+j] != None:
                    if board[i+j] == board[i+j+(self.n-1)]:
                        count += 1
                        if count == x:
                            return board[i+j]
                            # pass

        # check for bugs
        for i in range(3*self.n-2, self.n*(self.n-x+2), self.n):
            count = 1
            for j in range(0, self.n*self.n-i, self.n-1):
                #board[i+j] = "X"
                if board[i+j] != None:
                    if board[i+j] == board[i+j-(self.n-1)]:
                        count += 1
                        if count == x:
                            return board[i+j]
                            # pass

        return None

    def ai_best_move(self):
        best_value = -100
        best_move = -1
        for i in range(self.n*self.n):
            new_board = self.board.copy()
            if self.board[i] == None:
                new_board[i] = "O"
                new_value = self.minmax(new_board, self.n, False)
                # print(i,new_value)
                if new_value > best_value:

                    best_value = new_value
                    best_move = i
        return best_move

    def minmax(self, board, n, ai_turn):
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
                    value = max(value, self.minmax(new_board, n, False))
                    # print("max",i,value)
            return value
        else:
            value = 100
            for i in range(n*n):
                new_board = board.copy()
                if new_board[i] == None:
                    new_board[i] = "X"
                    value = min(value, self.minmax(new_board, n, True))
                    # print("min",i,value)
            return value
