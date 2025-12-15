"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-26"
-------------------------------------------------------
"""
# Imports

from utilities import array_to_queue
from Queue_array import Queue

def expect_equal(name, got, expected):
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {name}: got={got!r}, expected={expected!r}")

def main():
    # Arrange
    q = Queue()
    src = [1, 5, 2]
    expected_order = [1, 5, 2]  # first in list should be at FRONT of queue

    # Act
    result = array_to_queue(q, src)  # should return None
    # Assert return is None (void-style function)
    expect_equal("array_to_queue returns None", result, None)

    # 1) Source should be emptied
    expect_equal("source emptied", src, [])

    # 2) Queue should contain items in same order (front→rear)
    #    Your Queue.__iter__ yields front→rear for testing.
    got_iter_order = list(q)
    expect_equal("queue order via __iter__", got_iter_order, expected_order)

    # 3) peek() should show the first element
    try:
        got_peek = q.peek()
        expect_equal("peek() is first element", got_peek, expected_order[0])
    except Exception as e:
        print(f"[FAIL] peek() raised unexpectedly: {type(e).__name__}: {e}")

    # 4) Removing all should yield FIFO
    removed = []
    try:
        while not q.is_empty():
            removed.append(q.remove())
        expect_equal("remove() FIFO order", removed, expected_order)
    except Exception as e:
        print(f"[FAIL] remove() raised unexpectedly: {type(e).__name__}: {e}")

    # Queue should now be empty
    expect_equal("queue empty after removals", q.is_empty(), True)

if __name__ == '__main__':
    main()