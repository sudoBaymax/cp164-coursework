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

from functions import postfix
# Constants

string = '4 5 + 12 * 2 3 * -'

answer = postfix(string)

print(answer)