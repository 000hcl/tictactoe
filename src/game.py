##TEMPORARY
from math import sqrt

class Board:
    def __init__(self, n):
        """
        n = length of one side of the board
        """
        self.n = n
        self.board = self.new_board(self.n)
        #TEMPORARY:
        if self.n < 30:
            self.x = 3
        else:
            self.x = 5

    def new_board(self, n):
        board = [None for _ in range(n*n)]
        return board
    
    def player_move(self):
        #TODO: Needs input verification
        move = int(input("Your move:"))
        self.board[move] = "X"

    def print_board(self):
        board = self.board
        print("Board:")
        st = ""
        for x in range(self.n*self.n):
            if board[x] == None:
                if len(str(x)) == 1:
                    st += "[ " +str(x)+" ]"
                elif len(str(x)) == 2:
                    st += "[" +str(x)+" ]"
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
        for pos in range(self.n*self.n):
            if self.board[pos] == None:
                self.board[pos] = "O"
                return
            
    def end(self):
        if self.check_winner(self.x):
            print("WINNER")
            exit()
        if self.check_tie():
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
    
    #Winning moves:
    # Diagonals: x indices are exactly n-1 or n+1 apart. First index can't be must be from 1 to n-x (on its row).
    # Verticals: x indices are exactly n apart. [DONE]
    # Horizontals: x indices are exactly 1 apart and last index i+1 % n == 0 (or earlier). [DONE]

    def check_tie(self):
        if None in self.board:
            return False
        return True

    def check_winner(self, x):
        #TODO: Return which one wins?
        return self.check_verticals(x) | self.check_horizontal(x) | self.check_diagonal_rd(x)
    
    def check_verticals(self, x):
        for i in range(self.n):
            count = 1
            for j in range(self.n,self.n*self.n,self.n):
                if self.board[i+j] != None:
                    if self.board[i+j] == self.board[i+j-self.n]:
                        count += 1
                        if count == x:
                            return True
        return False

    def check_horizontal(self,x):
        for i in range(0,self.n*self.n,self.n):
            count = 1
            for j in range(1,self.n):
                if self.board[i+j] != None:
                    if self.board[i+j] == self.board[i+j-1]:
                        count += 1
                        if count == x:
                            return True
        return False
    
    def check_diagonal_rd(self,x):
        for i in range(0,self.n-x+1):
            count = 1
            for j in range(0,self.n*self.n-i,self.n+1):
                #self.board[i+j] = "a"
                if self.board[i+j] != None:
                    if self.board[i+j] == self.board[i+j-(self.n+1)]:
                        count += 1
                        if count == x:
                            #pass
                            return True
                if (i+j+1) % self.n == 0:
                    break
        for i in range(self.n,self.n*(self.n-x)+1,self.n):
            for j in range(0,self.n*self.n-i,self.n+1):
                #self.board[i+j] = "X"
                if self.board[i+j] != None:
                    if self.board[i+j] == self.board[i+j-(self.n+1)]:
                        count += 1
                        if count == x:
                            #pass
                            return True

        return False
    """
    def check_diagonal_ld(self,x):
        for i in range(self.n):
            count = 1
            for j in range(1,self.n*self.n,self.n-1):
                if self.board[i+j] != None:
                    if self.board[i+j] == self.board[i+j-1]:
                        count += 1
                        if count == x:
                            return True
        return False

"""