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
from functions import find_subs

def main():
    print(find_subs("It was a really, really, big assignment.", "real"))
    print(find_subs("aaaa", "aa"))
    print(find_subs("banana", "na"))
    print(find_subs("hello world", "test"))

if __name__ == "__main__":
    main()