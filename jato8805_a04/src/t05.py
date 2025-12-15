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
from Queue_circular import Queue


def test_initialization():
    """Test queue initialization."""
    print("=" * 60)
    print("Test 1: Initialization")
    print("=" * 60)
    
    q1 = Queue()
    print(f"Default capacity queue created")
    print(f"  Capacity: {q1._capacity}")
    print(f"  Is empty: {q1.is_empty()}")
    print(f"  Is full: {q1.is_full()}")
    print(f"  Length: {len(q1)}")
    
    q2 = Queue(5)
    print(f"\nCustom capacity queue created (capacity=5)")
    print(f"  Capacity: {q2._capacity}")
    print(f"  Is empty: {q2.is_empty()}")
    print()


def test_insert_remove():
    """Test basic insert and remove operations."""
    print("=" * 60)
    print("Test 2: Insert and Remove")
    print("=" * 60)
    
    q = Queue(5)
    values = [10, 20, 30]
    
    print("Inserting values:", values)
    for v in values:
        q.insert(v)
        print(f"  Inserted {v}: front={q._front}, rear={q._rear}, count={q._count}")
    
    print(f"\nQueue contents: {list(q)}")
    print(f"Is empty: {q.is_empty()}")
    print(f"Is full: {q.is_full()}")
    print(f"Length: {len(q)}")
    
    print("\nRemoving values:")
    while not q.is_empty():
        v = q.remove()
        print(f"  Removed {v}: front={q._front}, rear={q._rear}, count={q._count}")
    
    print(f"\nIs empty: {q.is_empty()}")
    print()


def test_circular_behavior():
    """Test circular array behavior."""
    print("=" * 60)
    print("Test 3: Circular Behavior")
    print("=" * 60)
    
    q = Queue(5)
    
    print("Insert 5 values to fill the queue:")
    for i in range(1, 6):
        q.insert(i)
    print(f"  Queue: {list(q)}")
    print(f"  _values: {q._values}")
    print(f"  front={q._front}, rear={q._rear}, full={q.is_full()}")
    
    print("\nRemove 3 values:")
    for _ in range(3):
        v = q.remove()
        print(f"  Removed {v}")
    print(f"  Queue: {list(q)}")
    print(f"  _values: {q._values}")
    print(f"  front={q._front}, rear={q._rear}")
    
    print("\nInsert 3 more values (demonstrating wrap-around):")
    for i in range(6, 9):
        q.insert(i)
        print(f"  Inserted {i}")
        print(f"    _values: {q._values}")
        print(f"    front={q._front}, rear={q._rear}")
    
    print(f"\nFinal queue: {list(q)}")
    print(f"Full: {q.is_full()}")
    print()


def test_peek():
    """Test peek operation."""
    print("=" * 60)
    print("Test 4: Peek")
    print("=" * 60)
    
    q = Queue(5)
    values = [100, 200, 300]
    
    for v in values:
        q.insert(v)
    
    print(f"Queue: {list(q)}")
    peeked = q.peek()
    print(f"Peeked value: {peeked}")
    print(f"Queue after peek: {list(q)}")
    print(f"Length unchanged: {len(q)}")
    print()


def test_equality():
    """Test __eq__ method with different configurations."""
    print("=" * 60)
    print("Test 5: Equality (__eq__)")
    print("=" * 60)
    
    # Test 1: Two identical queues
    q1 = Queue(8)
    q2 = Queue(8)
    values = [1, 2, 7, 9]
    
    for v in values:
        q1.insert(v)
        q2.insert(v)
    
    print("Queue 1:")
    print(f"  Values: {list(q1)}")
    print(f"  _values: {q1._values}")
    print(f"  front={q1._front}, rear={q1._rear}")
    
    print("\nQueue 2:")
    print(f"  Values: {list(q2)}")
    print(f"  _values: {q2._values}")
    print(f"  front={q2._front}, rear={q2._rear}")
    
    print(f"\nq1 == q2: {q1 == q2}")
    
    # Test 2: Same values, different positions (circular)
    print("\n" + "-" * 60)
    q3 = Queue(8)
    
    # Fill and remove to shift positions
    for i in range(4):
        q3.insert(i)
    for _ in range(4):
        q3.remove()
    
    # Now insert the same values as q1
    for v in values:
        q3.insert(v)
    
    print("\nQueue 3 (same values, different internal positions):")
    print(f"  Values: {list(q3)}")
    print(f"  _values: {q3._values}")
    print(f"  front={q3._front}, rear={q3._rear}")
    
    print(f"\nq1 == q3: {q1 == q3}")
    
    # Test 3: Different values
    print("\n" + "-" * 60)
    q4 = Queue(8)
    for v in [1, 2, 7, 8]:  # Last value different
        q4.insert(v)
    
    print("\nQueue 4 (different values):")
    print(f"  Values: {list(q4)}")
    print(f"\nq1 == q4: {q1 == q4}")
    
    # Test 4: Different lengths
    print("\n" + "-" * 60)
    q5 = Queue(8)
    for v in [1, 2, 7]:  # One less value
        q5.insert(v)
    
    print("\nQueue 5 (different length):")
    print(f"  Values: {list(q5)}")
    print(f"\nq1 == q5: {q1 == q5}")
    print()


def test_full_queue():
    """Test operations on a full queue."""
    print("=" * 60)
    print("Test 6: Full Queue")
    print("=" * 60)
    
    q = Queue(3)
    
    print("Filling queue (capacity=3):")
    for i in range(1, 4):
        q.insert(i)
        print(f"  Inserted {i}: full={q.is_full()}, rear={q._rear}")
    
    print(f"\nQueue: {list(q)}")
    print(f"Is full: {q.is_full()}")
    print(f"Rear is None: {q._rear is None}")
    
    print("\nTrying to insert when full (should cause assertion error):")
    try:
        q.insert(99)
        print("  ERROR: Should not be able to insert!")
    except AssertionError as e:
        print(f"  Correctly prevented: {e}")
    print()


def test_empty_queue():
    """Test operations on an empty queue."""
    print("=" * 60)
    print("Test 7: Empty Queue")
    print("=" * 60)
    
    q = Queue(5)
    
    print(f"Empty queue: {q.is_empty()}")
    
    print("\nTrying to remove from empty queue:")
    try:
        q.remove()
        print("  ERROR: Should not be able to remove!")
    except AssertionError as e:
        print(f"  Correctly prevented: {e}")
    
    print("\nTrying to peek at empty queue:")
    try:
        q.peek()
        print("  ERROR: Should not be able to peek!")
    except AssertionError as e:
        print(f"  Correctly prevented: {e}")
    print()


def comprehensive_test():
    """Run all tests."""
    test_initialization()
    test_insert_remove()
    test_circular_behavior()
    test_peek()
    test_equality()
    test_full_queue()
    test_empty_queue()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    comprehensive_test()