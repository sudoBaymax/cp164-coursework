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
from functions import do_comparisons, comparison_total

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

# Create three BSTs
bst1 = BST()
bst2 = BST()
bst3 = BST()

# Fill BST1 with DATA1 order
for char in DATA1:
    letter = Letter(char)
    bst1.insert(letter)

# Fill BST2 with DATA2 order
for char in DATA2:
    letter = Letter(char)
    bst2.insert(letter)

# Fill BST3 with DATA3 order
for char in DATA3:
    letter = Letter(char)
    bst3.insert(letter)

# Test BST1
file_variable = open("gibbon.txt", "r", encoding="utf-8")
do_comparisons(file_variable, bst1)
file_variable.close()
total1 = comparison_total(bst1)

print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons: {total1:,}")
print("-" * 60)

# Test BST2
file_variable = open("gibbon.txt", "r", encoding="utf-8")
do_comparisons(file_variable, bst2)
file_variable.close()
total2 = comparison_total(bst2)

print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons: {total2:,}")
print("-" * 60)

# Test BST3
file_variable = open("gibbon.txt", "r", encoding="utf-8")
do_comparisons(file_variable, bst3)
file_variable.close()
total3 = comparison_total(bst3)

print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons: {total3:,}")
print("-" * 60)

# Analysis
print()
print("Analysis:")
if total1 < total2 and total1 < total3:
    most_efficient = "DATA1 (alphabetical order)"
elif total2 < total1 and total2 < total3:
    most_efficient = "DATA2 (balanced tree order)"
else:
    most_efficient = "DATA3 (frequency order)"

print(f"{most_efficient} is most efficient.")
print()
print("Explanation:")
print("The frequency-based insertion order (DATA3) is most efficient because")
print("it places the most commonly used letters (E, T, A, O, etc.) higher in")
print("the tree, reducing the average number of comparisons needed to retrieve")
print("letters during text processing. While DATA2 creates a tree of minimum")
print("height, DATA3 optimizes for actual usage patterns in English text.")
print()
print("DATA1 (alphabetical) creates a completely unbalanced tree that degenerates")
print("into a linked list with O(n) search time, making it the least efficient.")
print("DATA2 creates a balanced tree with O(log n) search time for all letters.")
print("DATA3 combines good balance with frequency optimization, placing common")
print("letters near the root for faster average retrieval.")