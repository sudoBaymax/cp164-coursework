"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-15"
-------------------------------------------------------
"""
# Imports

"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

# Use DATA3 (frequency order) as it was the most efficient
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

# Create BST
bst = BST()

# Fill BST with Letter objects in frequency order
for char in DATA3:
    letter = Letter(char)
    bst.insert(letter)

# Process the gibbon.txt file
file_variable = open("gibbon.txt", "r", encoding="utf-8")
do_comparisons(file_variable, bst)
file_variable.close()

# Display the letter count table
letter_table(bst)