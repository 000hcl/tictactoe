# Implementation

## How it works

The AI uses minimax algorithm which checks the following things:
1. Is there a winner on the board if the AI places its token on a square?
2. If there is not a winner, could there potentially be a winner?
3. If there are no potential wins, are there any other strong positions?

Steps 2-3 are checked if the game tree is at a depth of >1.

## Complexity

After the first move the AI must check 8 spaces. If a square is 2 spaces away from another, those two squares are considered independent. Each independent square
 increases the total amount of squares to check by 8. An adjacent square that is not diagonal increases the amount by 3 at most. A diagonally placed square can
  increase the amount by 5 at most.

As the AI generates a game tree that has a height of <= 2, it checks about n*n situations, where n is the number of squares that are 1 space away from any placed
 token.

## What could be improved

Currently the AI checks an unnecessary amount of squares when a winner is searched for. Limiting its range further would make it much faster, however it would be
 difficult to implement in a hurry.
