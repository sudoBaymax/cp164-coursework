"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-27"
-------------------------------------------------------
"""
# Imports

from functions import stack_maze

# Sample from prompt (expect ['A','C','E','X'])
maze1 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
         'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}
print(stack_maze(maze1))  # ['A', 'C', 'E', 'X']

# Trivial maze (expect ['X'])
print(stack_maze({'Start': ['X']}))  # ['X']

# Circular maze (expect a valid path, e.g. ['A','C','E','X'])
maze2 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
         'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']}
print(stack_maze(maze2))  # ['A', 'C', 'E', 'X']

# No exit (expect None)
print(stack_maze({'Start': ['A'], 'A': []}))  # None
