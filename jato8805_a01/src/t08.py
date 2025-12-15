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

from functions import matrixes_multiply

def main():
    # Sample test
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    print(matrixes_multiply(a, b))  
    # Expected: [[58, 64], [139, 154]]

    # Identity test
    i = [[1, 0], [0, 1]]
    m = [[5, 6], [7, 8]]
    print(matrixes_multiply(m, i))  
    # Expected: [[5, 6], [7, 8]]

    # Non-square test
    x = [[2, 4, 6]]
    y = [[1], [3], [5]]
    print(matrixes_multiply(x, y))  
    # Expected: [[44]]

if __name__ == "__main__":
    main()