# Q3 - Sudoku Solver using CSP

## Aim
To solve a Sudoku puzzle using the Constraint Satisfaction Problem (CSP) approach.

## Problem Description
A Sudoku puzzle consists of a 9×9 grid. The goal is to fill the grid such that:
- Each row contains digits from 1 to 9 without repetition
- Each column contains digits from 1 to 9 without repetition
- Each 3×3 subgrid contains digits from 1 to 9 without repetition

## Approach
The problem is solved using backtracking.  
Empty cells are filled one by one, ensuring that the assigned number satisfies row, column, and subgrid constraints.  
If a conflict occurs, the algorithm backtracks and tries another number.

## Output
```text
Sudoku Solution:

4 8 3 9 2 1 6 5 7
9 6 7 3 4 5 8 2 1
2 5 1 8 7 6 4 9 3
5 4 8 1 3 2 9 7 6
7 2 9 5 6 4 1 3 8
1 3 6 7 9 8 2 4 5
3 7 2 6 8 9 5 1 4
8 1 4 2 5 3 7 6 9
6 9 5 4 1 7 3 8 2
