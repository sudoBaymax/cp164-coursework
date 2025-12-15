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
from functions import shift

def main():
    # Sample test
    print(shift("David", 1))   # Expected: EBWJE

    # Shift by 26 (no change)
    print(shift("David", 26))  # Expected: DAVID

    # Shift with punctuation
    print(shift("Hello, World!", 3))  # Expected: KHOOR, ZRUOG!

    # Empty string
    print(shift("", 5))  # Expected: ""

if __name__ == "__main__":
    main()
