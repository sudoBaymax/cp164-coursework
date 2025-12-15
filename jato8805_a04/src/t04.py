"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

def test_split_key_method():
    """
    Test the split_key method that extends Priority Queue class.
    """
    print("\n" + "=" * 60)
    print("Testing split_key method (extends class, preserves order)")
    print("=" * 60)
    
    # Create and populate source priority queue
    source = Priority_Queue()
    values = [5, 2, 8, 1, 9, 3, 7]
    print(f"Inserting values: {values}")
    for v in values:
        source.insert(v)
    
    key = 5
    print(f"\nSplitting with key = {key}")
    print(f"Values < {key} go to target1 (higher priority)")
    print(f"Values >= {key} go to target2 (lower/equal priority)\n")
    
    # Split the queue
    target1, target2 = source.split_key(key)
    
    print(f"Source is empty: {source.is_empty()}")
    print(f"\nTarget1 (< {key}) internal order preserved:")
    print(f"  _values: {[v for v in target1._values]}")
    print(f"  Removing by priority:")
    while not target1.is_empty():
        print(f"    {target1.remove()}")
    
    print(f"\nTarget2 (>= {key}) internal order preserved:")
    print(f"  _values: {[v for v in target2._values]}")
    print(f"  Removing by priority:")
    while not target2.is_empty():
        print(f"    {target2.remove()}")
        
if __name__ == "__main__":
    test_split_key_method()
    print("\n" + "=" * 60)