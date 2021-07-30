from board import Board

# debug stuff, TEMPORARY:
board = Board(3)

x1 = [None for _ in range(9)]
x1[4] = "X"
x1[0] = "O"
print(x1)
x2 = ["O","X","O","O","O","X","X",None,"X"]
x3 = [None,"O","X","O","X","X","O","X","O"]
x4 = ["O","O","X","X","X","O",None,None,"X"]
x5 = ["O","O",None,"X","O",None,"X","X","O"]

#print(board.minmax(x1,3,True,""))
y = x5

#print(board.check_verticals(3,y))
#print(board.check_horizontal(3,y))
#print(board.check_diagonal_rd(3,y))
#print(board.check_diagonal_ld(3,y))
#print(board.check_winner(3,x4))


#print(board.check_diagonal_rd(3,board.board))
#board.print_board()
board.start_game()
