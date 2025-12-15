"""
-------------------------------------------------------
Test file for pq_split_key function and split_key method
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key


def test_pq_split_key():
    """
    Test the pq_split_key function that uses Priority Queue interface.
    """
    print("=" * 60)
    print("Testing pq_split_key function (uses interface methods)")
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
    target1, target2 = pq_split_key(source, key)
    
    print(f"Source is empty: {source.is_empty()}")
    print(f"\nTarget1 (< {key}) contains:")
    while not target1.is_empty():
        print(f"  {target1.remove()}")
    
    print(f"\nTarget2 (>= {key}) contains:")
    while not target2.is_empty():
        print(f"  {target2.remove()}")


# def test_comparison():
#     """
#     Show the key difference between the two implementations.
#     """
#     print("\n" + "=" * 60)
#     print("KEY DIFFERENCE: Order Preservation")
#     print("=" * 60)
#
#     # Test function version
#     source1 = Priority_Queue()
#     values = [5, 2, 8, 1, 9, 3, 7]
#     for v in values:
#         source1.insert(v)
#
#     t1_func, t2_func = pq_split_key(source1, 5)
#
#     # Test method version
#     source2 = Priority_Queue()
#     for v in values:
#         source2.insert(v)
#
#     t1_method, t2_method = source2.split_key(5)
#
#     print("\nFunction version (uses remove/insert):")
#     print(f"  Target1 _values order: {[v for v in t1_func._values]}")
#     print(f"  (Order determined by insert operations)")
#
#     print("\nMethod version (preserves original order):")
#     print(f"  Target1 _values order: {[v for v in t1_method._values]}")
#     print(f"  (Order matches original insertion: {[v for v in values if v < 5]})")


if __name__ == "__main__":
    test_pq_split_key()
    print("\n" + "=" * 60)