##TEMPORARY

class Board:
    #Needs to be adjustable
    def __init__(self):
        self.board = self.new_board()

    def new_board(self):
        board = [None for _ in range(9)]
        return board
    
    def player_move(self):
        # Needs input verification
        move = int(input("Your move (integer from 0-8):"))
        self.board[move] = "X"

    def print_board(self):
        board = self.board
        print("Board:")
        st = ""
        for x in range(9):
            if board[x] == None:
                st += "["+str(x)+"]"
            elif board[x] == "X":
                st += "[X]"
            else:
                st += "[O]"
            if (x+1) % 3 == 0:
                print(st)
                st = ""
    
    def ai_move(self):
        # WIP
        for pos in range(9):
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
            self.print_board()
            self.ai_move()
