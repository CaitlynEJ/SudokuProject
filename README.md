# CS325 Project
*created by Caitlyn Jameson*

A playable Sudoku Game


## Description of Sudoku
Sudoku is a game of logic. The aim of Sudoku is to complete a puzzle using a sequence of numbers. The puzzle takes place on a grid, in this case, a 9x9 grid. There are 9 columns, 9 rows and 9 3x3 sections. At the start of the game, each section contains a combination of empty squares and printed squares. The numbers provided are part of the solution, and you the player must fill in the rest by figuring out which number (from 1-9) belongs in that square. 

Sudoku is considered to be NP-Complete. This means that given a solution, it should be verified in polynomial time. 

## The Rules 
Every row, every column, and every 3x3 section must contain the numbers 1 to 9, with no duplications. The game is complete when the board is completely filled in. A winning solution has no repeating numbers in a row, column, or 3x3 section.

## About This Program
This program was created to run via the command line using Python 3. 
It has a hard coded board instance where some numbers are given to you.
To run the program, use the command: `python3 sudoku.py`
The program includes a `main()` function that allows it to be run as a script.

The program will begin by giving you a breif set of instructions. You will then
be asked to input `yes` if you are ready. If you hit `enter`, or type something else,
the game will exit. So please be careful.

Once you begin, you will be asked to insert a Column value, a row value, and a number.
Again, be careful about accidently hitting enter, or not putting in a valid value.
I have tried to check for non letters, or numbers, but I will not likely catch everything.

Once you have completely filled in the board with your input, the program will automatically
check your input is a correct solution, or if it is incorrect. Unfortunely, it will
not tell you where the error has occurred. Only if the inputted solution is correct or not.


## Solution
For your convenience, the solution to the puzzle is below:


* Row 1: 784 | 659 | 213
* Row 2: 625 | 143 | 798
* Row 3: 913 | 728 | 456

* Row 4: 142 | 567 | 389
* Row 5: 568 | 394 | 172
* Row 6: 397 | 812 | 645

* Row 7: 851 | 276 | 934
* Row 8: 476 | 935 | 821
* Row 9: 239 | 481 | 567
