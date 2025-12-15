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

# Create a BST for testing
bst = BST()

print("Testing BST Operations")
print("=" * 60)

# Test 1: Insert values
print("\n1. Testing insert:")
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    inserted = bst.insert(value)
    print(f"   Insert {value}: {inserted}")

# Try inserting duplicate
duplicate = bst.insert(50)
print(f"   Insert 50 (duplicate): {duplicate}")

# Test 2: Check if empty and length
print(f"\n2. Is empty: {bst.is_empty()}")
print(f"   Length: {len(bst)}")
print(f"   Count: {bst.count()}")

# Test 3: Retrieve values
print("\n3. Testing retrieve:")
print(f"   Retrieve 40: {bst.retrieve(40)}")
print(f"   Retrieve 100: {bst.retrieve(100)}")

# Test 4: Contains
print("\n4. Testing contains:")
print(f"   40 in bst: {40 in bst}")
print(f"   100 in bst: {100 in bst}")

# Test 5: Min and Max
print("\n5. Testing min/max:")
print(f"   Min (iterative): {bst.min()}")
print(f"   Max (iterative): {bst.max()}")
print(f"   Min (recursive): {bst.min_r()}")
print(f"   Max (recursive): {bst.max_r()}")

# Test 6: Height
print(f"\n6. Height: {bst.height()}")

# Test 7: Node counts
print("\n7. Testing node counts:")
print(f"   Leaf count: {bst.leaf_count()}")
print(f"   One child count: {bst.one_child_count()}")
print(f"   Two child count: {bst.two_child_count()}")
zero, one, two = bst.node_counts()
print(f"   Node counts (zero, one, two): ({zero}, {one}, {two})")

# Test 8: Parent
print("\n8. Testing parent:")
print(f"   Parent of 20: {bst.parent(20)}")
print(f"   Parent of 50: {bst.parent(50)}")
print(f"   Parent of 40 (recursive): {bst.parent_r(40)}")

# Test 9: Traversals
print("\n9. Testing traversals:")
print(f"   Inorder: {bst.inorder()}")
print(f"   Preorder: {bst.preorder()}")
print(f"   Postorder: {bst.postorder()}")
print(f"   Levelorder: {bst.levelorder()}")

# Test 10: Is balanced
print(f"\n10. Is balanced: {bst.is_balanced()}")

# Test 11: Is valid
print(f"\n11. Is valid BST: {bst.is_valid()}")

# Test 12: Remove
print("\n12. Testing remove:")
print(f"    Remove 20 (leaf): {bst.remove(20)}")
print(f"    Remove 30 (one child): {bst.remove(30)}")
print(f"    Remove 50 (two children): {bst.remove(50)}")
print(f"    Remove 100 (not found): {bst.remove(100)}")
print(f"    Length after removes: {len(bst)}")
print(f"    Inorder after removes: {bst.inorder()}")

# Test 13: Equality
print("\n13. Testing equality:")
bst2 = BST()
for value in [40, 60, 70, 80]:
    bst2.insert(value)
print(f"    bst == bst2: {bst == bst2}")

bst3 = BST()
for value in [40, 60, 70, 80]:
    bst3.insert(value)
print(f"    bst2 == bst3: {bst2 == bst3}")

# Test 14: Iterator
print("\n14. Testing iterator:")
print("    Values using iterator:")
for value in bst:
    print(f"       {value}")

print("\n" + "=" * 60)
print("Testing complete")