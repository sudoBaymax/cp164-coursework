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
from Letter import Letter


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    for node in bst:
        node.comparisons = 0

    for line in file_variable:
        for char in line:
            if char.isalpha():
                upper_char = char.upper()
                key = Letter(upper_char)
                bst.retrieve(key)
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    letters = bst.inorder()
    
    for letter in letters:
        total += letter.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    letters = bst.inorder()
    total_count = 0
    
    for letter in letters:
        total_count += letter.count
    
    print("Letter Count/Percent Table")
    print()
    print(f"Total Count: {total_count:,}")
    print()
    print("Letter  Count       %")
    print("---------------------")
    
    for letter in letters:
        percentage = (letter.count / total_count * 100) if total_count > 0 else 0
        print(f"    {letter.letter}  {letter.count:>7,}  {percentage:>5.2f}%")
    
    print()
    return