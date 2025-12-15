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
from functions import stack_split_alt
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = [8,14,12,9,8,7,5]

array_to_stack(stack, source)

print("source")
print()
for s in stack:
    print(s)
print()

target1, target2 = stack_split_alt(stack)

print("target1")
print()
for x in target1:
    print(x)
print()
print("target2")
print()
for y in target2:
    print(y)