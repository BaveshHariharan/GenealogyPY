# GenealogyPY
Python implementation of a genealogy system that supports adding family members, primogeniture order, seniority order, and cousin distance calculations.

Implemented a Genealogy system in Python using OOP principles.
The program stores family data using dictionaries and lists, supports adding children, and generates primogeniture (DFS) and seniority (BFS) succession orders.
It also determines cousin relationships by computing ancestor distances and finding the Most Recent Common Ancestor.

> Work with Object-Oriented Programming
Created a class (Genealogy)
Used instance attributes
Designed methods that operate on internal data structures

> Use Data Structures in Python
Dictionaries to store parent → children relationships
Lists to maintain birth order and queue operations
Recursive function for depth-first search
Queue-based breadth-first traversal

> Implement Tree Traversal Algorithms
Depth-First Search for primogeniture succession
Breadth-First Search for seniority

> Work with Ancestor Tracking / Relationship Logic
Built ancestor lists for both individuals
Computed Most Recent Common Ancestor (MRCA)
Calculated cousin degree and removal

> Algorithmic Thinking
Designed logical steps to:
add family members,
traverse generations,
compute how closely two members are related.
