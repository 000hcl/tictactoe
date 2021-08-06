# Week 3 report

## What did I do this week?

This week I changed the list into a list of integers and tried to come up with a way to find winning rows only by having to iterate over the board list once.
I also added alpha-beta pruning.

## How has the project progressed?

The 3x3 worked fine and seemingly fast enough, so I am experimenting with a 4x4 board. It's still incredibly slow in the game's earliest stages, but somewhat playable. I did not come very far
in improving the efficiency.

The tests still need to get updated and won't pass at this stage.

## What did I learn?

This is much harder than I initially thought.

## Problems?

I've not found much info about the efficiency of different data structures that I could use instead of the list. I tried to do small experiments with numpy's array
 but it seems that going through each element takes much longer than with a regular list.

Although I made a check_winner() version that only iterates through the list once, I have not noticed noticable improvement in efficiency yet.


## What next?

Checking for situations in which either party can definitely win. Trying to figure out how to make the thing faster.

Hours used:


5.8: 4h Converting list elements to integers, trying to find out if arrays are better or not.
6.8: 4h --||-- + finding bugs, new check_winner() version

total: 8h
