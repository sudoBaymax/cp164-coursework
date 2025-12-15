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
from Stack_array import Stack
from utilities import array_to_stack
# Constants

stack = Stack()

source = [1,2,3,4,5,6,7]

array_to_stack(stack, source)

print("stack")
print()
for s in stack:
    print(s)
print()

stack.reverse()

print()

print("Reverse stack")
print()
for s in stack:
    print(s)
print()