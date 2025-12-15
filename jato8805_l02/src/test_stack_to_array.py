"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-18"
-------------------------------------------------------
"""
# Imports


from Stack_array import Stack
from utilities import stack_to_array

def main():
    stack_test = Stack()
    stack_test.push(2)              # stack top is 2
    target = [2, 4, 6]              # give the list a name

    stack_to_array(stack_test, target)

    # minimal prints:
    print(f"Stack: {list(stack_test)}")  # TOP -> BOTTOM view via your __iter__
    print(f"Target: {target}")
    
if __name__ == "__main__":
    main()
    
    