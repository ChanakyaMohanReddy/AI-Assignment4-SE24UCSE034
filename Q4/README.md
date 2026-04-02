
# Q4 - Cryptarithmetic Puzzle using CSP

## Aim

To solve the cryptarithmetic puzzle using the Constraint Satisfaction Problem (CSP) approach.

## Problem Description

The given puzzle is:

```text
  T W O
+ T W O
-------
F O U R
```

Each letter represents a unique digit from 0 to 9.
The goal is to find a valid assignment of digits such that the addition is correct.

## Constraints

* Each letter must have a unique digit
* No leading digit can be zero (T ≠ 0, F ≠ 0)
* The arithmetic addition must be correct

## Approach

The problem is solved by assigning digits to letters and checking whether the assignment satisfies all constraints.
The solution follows column-wise addition logic and ensures all digits are distinct.

## Output

```text
Solution:
T = 7 W = 3 O = 4
F = 1 U = 6 R = 8
734 + 734 = 1468
```

