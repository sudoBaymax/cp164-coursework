"""
-------------------------------------------------------
Testing BST Methods: node_counts, __contains__, parent, parent_r
-------------------------------------------------------
Author: Joseph Jatou
ID: 169088805
Email: jato8805@mylaurier.ca
__updated__ = "2025-11-22"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

def test_node_counts():
    """
    Test the node_counts method with various tree configurations.
    """
    print("=" * 70)
    print("Testing node_counts()")
    print("=" * 70)
    
    # Test 1: Empty tree
    print("\nTest 1: Empty Tree")
    bst = BST()
    zero, one, two = bst.node_counts()
    print(f"Zero children: {zero}, One child: {one}, Two children: {two}")
    print(f"Expected: Zero=0, One=0, Two=0")
    
    # Test 2: Single node (root only)
    print("\nTest 2: Single Node Tree")
    bst = BST()
    bst.insert(50)
    zero, one, two = bst.node_counts()
    print(f"Tree: [50]")
    print(f"Zero children: {zero}, One child: {one}, Two children: {two}")
    print(f"Expected: Zero=1, One=0, Two=0")
    
    # Test 3: Balanced tree
    print("\nTest 3: Balanced Tree")
    bst = BST()
    values = [50, 25, 75, 10, 30, 60, 80]
    for v in values:
        bst.insert(v)
    zero, one, two = bst.node_counts()
    print(f"Tree values: {values}")
    print(f"         50")
    print(f"        /  \\")
    print(f"      25    75")
    print(f"     / \\   / \\")
    print(f"   10  30 60  80")
    print(f"Zero children: {zero}, One child: {one}, Two children: {two}")
    print(f"Expected: Zero=4 (leaves: 10,30,60,80), One=0, Two=3 (nodes: 50,25,75)")
    
    # Test 4: Unbalanced tree (right skewed)
    print("\nTest 4: Right-Skewed Tree")
    bst = BST()
    values = [10, 20, 30, 40, 50]
    for v in values:
        bst.insert(v)
    zero, one, two = bst.node_counts()
    print(f"Tree values: {values}")
    print(f"10")
    print(f" \\")
    print(f"  20")
    print(f"   \\")
    print(f"    30")
    print(f"     \\")
    print(f"      40")
    print(f"       \\")
    print(f"        50")
    print(f"Zero children: {zero}, One child: {one}, Two children: {two}")
    print(f"Expected: Zero=1 (leaf: 50), One=4 (nodes: 10,20,30,40), Two=0")
    
    # Test 5: Mixed tree
    print("\nTest 5: Mixed Tree")
    bst = BST()
    values = [50, 25, 75, 10, 60, 80, 5]
    for v in values:
        bst.insert(v)
    zero, one, two = bst.node_counts()
    print(f"Tree values: {values}")
    print(f"         50")
    print(f"        /  \\")
    print(f"      25    75")
    print(f"     /     / \\")
    print(f"   10    60  80")
    print(f"  /")
    print(f" 5")
    print(f"Zero children: {zero}, One child: {one}, Two children: {two}")
    print(f"Expected: Zero=3 (leaves: 5,60,80), One=2 (nodes: 25,10), Two=2 (nodes: 50,75)")

def test_contains():
    """
    Test the __contains__ method (in operator).
    """
    print("\n" + "=" * 70)
    print("Testing __contains__ (in operator)")
    print("=" * 70)
    
    # Build a test tree
    bst = BST()
    values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35]
    for v in values:
        bst.insert(v)
    
    print(f"\nTree contains: {sorted(values)}")
    
    # Test existing values
    print("\nTest 1: Values that EXIST in tree")
    test_values = [50, 25, 10, 80, 35, 5]
    for val in test_values:
        result = val in bst
        print(f"{val} in bst: {result} (Expected: True)")
    
    # Test non-existing values
    print("\nTest 2: Values that DO NOT EXIST in tree")
    test_values = [100, 1, 40, 70, 90, 0]
    for val in test_values:
        result = val in bst
        print(f"{val} in bst: {result} (Expected: False)")
    
    # Test empty tree
    print("\nTest 3: Empty Tree")
    empty_bst = BST()
    result = 50 in empty_bst
    print(f"50 in empty_bst: {result} (Expected: False)")

def test_parent_iterative():
    """
    Test the parent method (iterative version).
    """
    print("\n" + "=" * 70)
    print("Testing parent() - Iterative")
    print("=" * 70)
    
    # Build a test tree
    bst = BST()
    values = [50, 25, 75, 10, 30, 60, 80, 5, 15]
    for v in values:
        bst.insert(v)
    
    print(f"\nTree structure:")
    print(f"         50")
    print(f"        /  \\")
    print(f"      25    75")
    print(f"     / \\   / \\")
    print(f"   10  30 60  80")
    print(f"  / \\")
    print(f" 5  15")
    
    # Test various nodes
    print("\nTest Cases:")
    test_cases = [
        (50, None, "Root has no parent"),
        (25, 50, "Left child of root"),
        (75, 50, "Right child of root"),
        (10, 25, "Left grandchild"),
        (30, 25, "Right grandchild"),
        (60, 75, "Left child of 75"),
        (80, 75, "Right child of 75"),
        (5, 10, "Left great-grandchild"),
        (15, 10, "Right great-grandchild"),
    ]
    
    for key, expected, description in test_cases:
        result = bst.parent(key)
        print(f"parent({key}): {result} | Expected: {expected} | {description}")
    
    # Test non-existing key
    print("\nTest with non-existing key:")
    result = bst.parent(100)
    print(f"parent(100): {result} (Expected: None - key not found)")

def test_parent_recursive():
    """
    Test the parent_r method (recursive version).
    """
    print("\n" + "=" * 70)
    print("Testing parent_r() - Recursive")
    print("=" * 70)
    
    # Build the same test tree
    bst = BST()
    values = [50, 25, 75, 10, 30, 60, 80, 5, 15]
    for v in values:
        bst.insert(v)
    
    print(f"\nTree structure:")
    print(f"         50")
    print(f"        /  \\")
    print(f"      25    75")
    print(f"     / \\   / \\")
    print(f"   10  30 60  80")
    print(f"  / \\")
    print(f" 5  15")
    
    # Test various nodes
    print("\nTest Cases:")
    test_cases = [
        (50, None, "Root has no parent"),
        (25, 50, "Left child of root"),
        (75, 50, "Right child of root"),
        (10, 25, "Left grandchild"),
        (30, 25, "Right grandchild"),
        (60, 75, "Left child of 75"),
        (80, 75, "Right child of 75"),
        (5, 10, "Left great-grandchild"),
        (15, 10, "Right great-grandchild"),
    ]
    
    for key, expected, description in test_cases:
        result = bst.parent_r(key)
        print(f"parent_r({key}): {result} | Expected: {expected} | {description}")
    
    # Test non-existing key
    print("\nTest with non-existing key:")
    result = bst.parent_r(100)
    print(f"parent_r(100): {result} (Expected: None - key not found)")

def compare_parent_methods():
    """
    Compare iterative and recursive parent methods to ensure they produce
    identical results.
    """
    print("\n" + "=" * 70)
    print("Comparing parent() vs parent_r()")
    print("=" * 70)
    
    bst = BST()
    values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35, 55, 65]
    for v in values:
        bst.insert(v)
    
    print(f"\nTree contains: {sorted(values)}")
    print("\nComparing results for all values:")
    
    all_match = True
    for val in values:
        iter_result = bst.parent(val)
        rec_result = bst.parent_r(val)
        match = iter_result == rec_result
        if not match:
            all_match = False
        status = "✓" if match else "✗"
        print(f"{status} Key {val:3d}: parent()={iter_result}, parent_r()={rec_result}")
    
    print(f"\nAll results match: {all_match}")

# Main execution
if __name__ == "__main__":
    print("BST METHODS TESTING")
    print("=" * 70)
    
    test_node_counts()
    test_contains()
    test_parent_iterative()
    test_parent_recursive()
    compare_parent_methods()
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE")
    print("=" * 70)