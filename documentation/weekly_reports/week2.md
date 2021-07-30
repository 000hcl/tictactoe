# Week 2 report

## What did I do this week?

This week I tried to implement a working, adjustable game board for tic tac toe, and a basic minimax algorithm for it as well.

## How has the project progressed?

The project seems to be progressing, and all new features seem to be working. Currently it is a playable 3x3 game with a basic minimax algorithm. However it quits as soon the game has been won by either player or AI, or when the game ends in a tie. This will be changed later.

## What did I learn?

I tried out the pure minimax algorithm with a 4x4 board and it is clearly too inefficient on its own. There is a clear wait time, even on the 3x3 board.

Testing is something I've neglected to do earlier. Thanks to it I've found the cause of an issue I've had with the algorithm. It seems to work okay now.

## Problems?

I've had a lot of bugs to fix, and at times I did not know if the problems came from small mistakes or from a lack of understanding of the algorithm. After
 some bug hunting I think the minimax algorithm works correctly now.

Structuring the project is something I'm a bit unsure of how to do. 

## What next?

Adding alpha-beta pruning, trying to figure out how to make it work efficiently on a large game board. 

Hours used:


25.7: 

3 h: game board
      
26.7: 

45 min: finishing the adjustable, "playable" game board
      
30 min: try to implement minimax
      
27.7:

3 h: working? minimax algorithm
      
3 h: trying to find issues, bug fixing

28.7:

1 h: Setting up poetry

29.7:

3 h: Documenting the code, making and undoing a lot of mistakes.

30.7:

4 h: Bug-hunting, tests

total: 18 h 15 min
