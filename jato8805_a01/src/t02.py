"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-13"
-------------------------------------------------------
"""
# Imports

from functions import list_subtraction

def main():

    # Test 1
    data = [5, 5, 4, 5]
    print("Before:", data)
    list_subtraction(data, [5])
    print("After: ", data)   # should be [4]
    
    # Test 2
    data = [1, 2, 3, 4, 5]
    list_subtraction(data, [2, 4])
    print("Test 2:", data)   # should be [1, 3, 5]
    
    # Test 3
    data = []
    list_subtraction(data, [1, 2])
    print("Test 3:", data)   # should be []
    
    # Test 4
    data = [1, 1, 1]
    list_subtraction(data, [1])
    print("Test 4:", data)   # should be []
    
if __name__ == "__main__":
    main()