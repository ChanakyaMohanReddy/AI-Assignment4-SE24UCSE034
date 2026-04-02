# AI Assignment 4

# Q1 - Australia Map Coloring using CSP

## Aim
To solve the Australia Map Coloring problem using Constraint Satisfaction Problem (CSP) with backtracking.

## Problem Description
Each state in Australia must be assigned a color such that no two adjacent states share the same color.

## States
WA, NT, SA, Q, NSW, V, T

## Colors Used
Red, Green, Blue

## Constraints
- Adjacent states must have different colors.
- Tasmania (T) has no neighboring states.

## Approach
The problem is solved using backtracking.  
For each state, a color is assigned only if it does not conflict with its neighboring states.  
If a conflict occurs, the algorithm backtracks and tries another color.

## Output
```
Australia Map Coloring:

WA -> Red
NT -> Green
SA -> Blue
Q -> Red
NSW -> Green
V -> Red
T -> Red
```
