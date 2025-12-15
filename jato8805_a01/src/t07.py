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
from functions import matrix_transpose

def main():
    # Sample test
    print(matrix_transpose([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]))
    # Expected: [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]

    # Square matrix
    print(matrix_transpose([[1, 2], [3, 4]]))
    # Expected: [[1, 3], [2, 4]]

    # Single row
    print(matrix_transpose([[1, 2, 3]]))
    # Expected: [[1], [2], [3]]

    # Single column
    print(matrix_transpose([[1], [2], [3]]))
    # Expected: [[1, 2, 3]]

if __name__ == "__main__":
    main()