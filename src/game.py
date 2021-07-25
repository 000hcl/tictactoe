##TEMPORARY

class Board:
    def __init__(self, n):
        """
        n = length of one side of the board
        """
        self.n = n
        self.board = self.new_board(self.n)

    def new_board(self, n):
        board = [None for _ in range(n*n)]
        return board
    
    def player_move(self):
        # Needs input verification
        move = int(input("Your move (integer from 0-8):"))
        self.board[move] = "X"

    def print_board(self):
        board = self.board
        print("Board:")
        st = ""
        for x in range(self.n*self.n):
            if board[x] == None:
                st += "["+str(x)+"]"
            elif board[x] == "X":
                st += "[X]"
            else:
                st += "[O]"
            if (x+1) % self.n == 0:
                print(st)
                st = ""
    
    def ai_move(self):
        # WIP
        for pos in range(self.n*self.n):
            if self.board[pos] == None:
                self.board[pos] = "O"
                return
        self.end()
            
    def end(self):
        print("GAME ENDED")
    
    def start_game(self):
        while True:
            self.print_board()
            self.player_move()
            self.ai_move()
