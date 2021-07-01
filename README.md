# Tic Tac Toe Permutations Counter
A recursive loop search of tic tac toe game permutations in a tiny Python module.
> tic-tac-toe-permutations-counter.py

Execution Result
----------------
total games: 255168<br />
first player wins: 131184<br />
second player wins: 77904<br />
draw: 46080

The Algorithm Explained
-----------------------
1. Create First Game
2. Get Result
3. Decide Next Action For In Progress Game<br />
    3.1. Get All Moves Left<br />
    3.2. Get Next Player<br />
    3.3. Make Available Moves<br />
    3.4. Get Result<br />
4. Log Ended Game
5. Count Permutation

Frames and Slots
----------------
```
Game Board Positions
    top left: 0
    top middle: 1
    top right: 2
    middle left: 3
    middle middle: 4
    middle right: 5
    bottom left: 6
    bottom middle: 7
    bottom right: 8
Result
    - X Wins
    - O Wins
    - Draw
    - In Progress
Win
    top horisontal: 0,1,2
    diagonal down: 0,3,6
    left vertical: 0,4,8
    middle vertical: 1,4,7
    diagonal up: 2,4,6
    right vertical: 2,5,8
    middel horisontal: 3,4,5
    bottom horisontal: 6,7,8
Permutation
```
