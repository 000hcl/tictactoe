from board import Board

board = Board(3)

#TEMPORARY:

"""

x1 = [None for _ in range(9)]
x1[4] = "X"
x1[0] = "O"
print(x1)
x2 = ["O","X","O","O","O","X","X",None,"X"]
x3 = [None,"O","X","O","X","X","O","X","O"]
x4 = ["O","O","X","X","X","O",None,None,"X"]
x5 = ["O","O",None,"X","O",None,"X","X","O"]

y1 = [0,0,0,1,1,1,0,0,0]
y2 = [10,0,0,10,1,1,10,1,1]
y3 = [0 for _ in range(16)]
y4 = [10,1,1,0,10,0,1,1,10]
y5 = [1, 10, 10, 10, 1, 10, 1, 1, 1]

#print(board.minmax(x1,3,True,""))
y = y5

#print(board.check_verticals(3,y))
#print(board.check_horizontal(3,y))
#print(board.check_diagonal_rd(3,y))
#print(board.check_diagonal_ld(3,y))
print(board.check_winner(3,y))




#print(board.check_horizontal(3,board.board))
#print(board.check_verticals(3,board.board))
print(board.check_diagonal_rd(4,board.board))
#print(board.check_diagonal_ld(4,board.board))

#board.print_board()
"""
#print(board.check_diagonal_ld(4,board.board))
#board.print_board()
board.start_game()
