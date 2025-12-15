"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-01"
-------------------------------------------------------
"""
# Imports

import unittest
from copy import deepcopy
from Priority_Queue_linked import Priority_Queue  


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.empty = Priority_Queue()

        self.pq_small = Priority_Queue()
        for v in [1, 3, 5]:
            self.pq_small.insert(v)

        self.pq_mixed = Priority_Queue()
        for v in [4, 2, 2, 7, 1]:
            self.pq_mixed.insert(v)  # should end up sorted: 1,2,2,4,7

    def test_is_empty_and_len(self):
        self.assertTrue(self.empty.is_empty())
        self.assertEqual(len(self.empty), 0)

        self.pq_small.insert(0)
        self.assertFalse(self.pq_small.is_empty())
        self.assertEqual(len(self.pq_small), 4)

    def test_insert_ordering_and_stability(self):
        pq = Priority_Queue()
        # insert a sequence in arbitrary order
        values = [5, 1, 3, 3, 2]
        for v in values:
            pq.insert(v)
        # ascending order expected, stable for equal values (existing 3s before new 3s)
        self.assertEqual(list(pq), [1, 2, 3, 3, 5])

        # test stability explicitly: insert equal values and ensure relative order preserved
        pq2 = Priority_Queue()
        pq2.insert(("a", 2))  # uses tuple comparators; smaller tuple compares first element then second
        pq2.insert(("b", 2))
        # For simple numeric stability test, use numbers:
        pq3 = Priority_Queue()
        pq3.insert(2)
        pq3.insert(2)
        pq3.insert(2)
        self.assertEqual(list(pq3), [2, 2, 2])

    def test_peek_and_remove(self):
        pq = deepcopy(self.pq_mixed)
        # smallest value should be 1
        self.assertEqual(pq.peek(), 1)
        self.assertEqual(len(pq), 5)

        # remove items in priority order
        removed = [pq.remove() for _ in range(len(pq))]
        self.assertEqual(removed, [1, 2, 2, 4, 7])
        self.assertTrue(pq.is_empty())

        # exceptions on empty
        with self.assertRaises(AssertionError):
            self.empty.peek()
        with self.assertRaises(AssertionError):
            self.empty.remove()

    def test_move_front_to_rear_and_append(self):
        # _move_front_to_rear: move nodes between PQs
        a = Priority_Queue()
        b = Priority_Queue()
        for v in [1, 2, 3]:
            a.insert(v)
        # move front from a to b (b empty)
        b._move_front_to_rear(a)
        self.assertEqual(list(b), [1])
        self.assertEqual(list(a), [2, 3])

        # move two more to b
        b._move_front_to_rear(a)
        b._move_front_to_rear(a)
        self.assertEqual(list(b), [1, 2, 3])
        self.assertTrue(a.is_empty())

        # _append_queue: append whole queue
        x = Priority_Queue()
        y = Priority_Queue()
        for v in [1, 4]:
            x.insert(v)
        for v in [2, 3, 5]:
            y.insert(v)
        x._append_queue(y)
        self.assertEqual(list(x), [1, 2, 3, 4, 5])
        self.assertTrue(y.is_empty())

    def test_split_alt(self):
        s = Priority_Queue()
        for v in [0, 1, 2, 3, 4]:
            s.insert(v)
        a, b = s.split_alt()
        self.assertTrue(s.is_empty())
        self.assertEqual(list(a), [0, 2, 4])
        self.assertEqual(list(b), [1, 3])

        # single element
        s2 = Priority_Queue()
        s2.insert(10)
        a2, b2 = s2.split_alt()
        self.assertEqual(list(a2), [10])
        self.assertTrue(b2.is_empty())

    def test_split_key(self):
        s = Priority_Queue()
        for v in [5, 1, 3, 4, 2]:
            s.insert(v)  # sorted: 1,2,3,4,5
        # key = 3 -> target1 gets values <3 => [1,2], target2 gets >=3 => [3,4,5]
        t1, t2 = s.split_key(3)
        self.assertTrue(s.is_empty())
        self.assertEqual(list(t1), [1, 2])
        self.assertEqual(list(t2), [3, 4, 5])

        # key smaller than all -> t1 empty, t2 all
        s2 = Priority_Queue()
        for v in [4, 6, 7]:
            s2.insert(v)
        a, b = s2.split_key(1)
        self.assertTrue(a.is_empty())
        self.assertEqual(list(b), [4, 6, 7])

    def test_combine(self):
        s1 = Priority_Queue()
        s2 = Priority_Queue()
        for v in [1, 4, 6]:
            s1.insert(v)
        for v in [2, 4, 5, 7]:
            s2.insert(v)
        t = Priority_Queue()
        t.combine(s1, s2)
        # merge should preserve ascending order, source1 wins ties -> 1,2,4(from s1),4(from s2),5,6,7
        self.assertEqual(list(t), [1, 2, 4, 4, 5, 6, 7])
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.is_empty())

    def test_deepcopy_node_semantics(self):
        v = [1, 2]
        pq = Priority_Queue()
        pq.insert(v)
        v.append(3)  # modifying original should not change stored copy
        stored = list(pq)[0]
        self.assertEqual(stored, [1, 2])

    def test_iter_and_len_after_ops(self):
        pq = Priority_Queue()
        pq.insert(3)
        pq.insert(1)
        self.assertEqual(list(pq), [1, 3])
        self.assertEqual(len(pq), 2)
        pq.remove()
        self.assertEqual(list(pq), [3])
        self.assertEqual(len(pq), 1)


if __name__ == "__main__":
    unittest.main()