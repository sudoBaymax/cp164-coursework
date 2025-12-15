"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from List_linked import _List_Node

lst = List()
for n in [82, 12, 52, 66, 283]:
    lst.append(n)

List.radix_sort(lst)            # staticmethod call that mutates lst
print([v for v in lst])         # -> [12, 24, 51, 247]