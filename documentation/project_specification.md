# Project Specification

## General information

- Degree programme: Bachelor's in computer science (CS/TKT)
- Documentation language: English
- Programming language: Python

## Algorithms and data structures

I will be using the minimax algorithm with alpha-beta pruning. According to source [1] the time complexity of a minimax algorithm without alpha-beta pruning is O(b^m),
where b is the number of available moves and m is the depth of the tree. With alpha-beta pruning the value m may be halved.

The game board will most likely be a list whose indices represent a position in the game board.

## The problem to be solved: AI opponent

The goal is to implement a working and efficient AI opponent for a variant of the tic tac toe game. The board size will be about 30x30, and the goal is to get 5 marks
 in a row (horizontally, vertically, or diagonally).
 
The minimax algorithm may be a straightforward solution to this kind of problem. For a small game board this algorithm would be enough, but for a larger board more
 tools will be necessary. Alpha-beta pruning can in some cases make the process faster. In the early phases of a 30x30 game it will not be necessary for the AI to
  check every possible move, so some other thing is needed for better efficiency.

## Input

The only input required of the user is the position of the board they want to place their mark on.

## Sources

[1] https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html
