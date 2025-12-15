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
from functions import file_analyze

def main():
    with open("note_file_analyze.txt", "r") as fv:
        upp, low, dig, whi, rem = file_analyze(fv)

    print("Uppercase:", upp)
    print("Lowercase:", low)
    print("Digits:", dig)
    print("Whitespace:", whi)
    print("Remaining:", rem)

if __name__ == "__main__":
    main()