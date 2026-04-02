# Q2 - Telangana Map Coloring using CSP

## Aim
To solve the Telangana Map Coloring problem using Constraint Satisfaction Problem (CSP) with backtracking.

## Problem Description
Each district in Telangana must be assigned a color such that no two adjacent districts have the same color.

## Colors Used
- Red
- Green
- Blue
- Yellow

## Constraints
- Adjacent districts must have different colors.
- Each district must be assigned only one color.

## Approach
This problem is solved using backtracking.  
Each district is treated as a variable, and colors are assigned one by one.  
Before assigning a color, the program checks whether any neighboring district already has the same color.  
If a conflict occurs, the algorithm backtracks and tries another color.

## Conclusion
The Telangana Map Coloring problem was successfully solved using the Constraint Satisfaction Problem (CSP) approach with backtracking.

All districts were assigned colors such that no two adjacent districts share the same color, satisfying the given constraints.

This demonstrates how CSP techniques can be effectively applied to solve real-world problems like map coloring.

## Output
```text
Telangana Map Coloring:

Adilabad -> Red
Bhadradri Kothagudem -> Red
Hanamkonda -> Red
Hyderabad -> Red
Jagtial -> Red
Jangaon -> Green
Jayashankar Bhupalpally -> Blue
Jogulamba Gadwal -> Red
Kamareddy -> Red
Karimnagar -> Green
Khammam -> Green
Kumuram Bheem Asifabad -> Green
Mahabubabad -> Blue
Mahabubnagar -> Red
Mancherial -> Blue
Medak -> Green
Medchal Malkajgiri -> Blue
Mulugu -> Green
Nagarkurnool -> Green
Nalgonda -> Blue
Narayanpet -> Green
Nirmal -> Yellow
Nizamabad -> Green
Peddapalli -> Yellow
Rajanna Sircilla -> Blue
Ranga Reddy -> Green
Sangareddy -> Yellow
Siddipet -> Yellow
Suryapet -> Yellow
Vikarabad -> Blue
Wanaparthy -> Blue
Warangal -> Yellow
Yadadri Bhuvanagiri -> Red
