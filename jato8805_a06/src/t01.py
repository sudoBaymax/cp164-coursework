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

# Update this import if your queue module has a different filename.
# e.g., from my_queue_file import Queue
from Queue_linked import Queue, _Queue_Node  # change queue_linked -> your filename if needed


class TestQueueLinked(unittest.TestCase):
    def setUp(self):
        # common queues used across tests
        self.q_empty = Queue()

        self.q_1 = Queue()
        for v in [1, 2, 3]:
            self.q_1.insert(v)

        self.q_2 = Queue()
        for v in ["a", "b", "c", "d"]:
            self.q_2.insert(v)

    def test_insert_and_len_and_iter(self):
        q = Queue()
        self.assertEqual(len(q), 0)
        q.insert(10)
        q.insert(20)
        q.insert(30)
        self.assertEqual(len(q), 3)

        # iteration should yield 10,20,30 in that order
        self.assertEqual(list(q), [10, 20, 30])

    def test_peek(self):
        q = deepcopy(self.q_1)
        # front should be 1
        self.assertEqual(q.peek(), 1)
        # peek doesn't remove
        self.assertEqual(len(q), 3)

        # empty peek -> assertion error
        with self.assertRaises(AssertionError):
            self.q_empty.peek()

    def test_remove(self):
        q = deepcopy(self.q_1)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertTrue(q.is_empty())

        with self.assertRaises(AssertionError):
            q.remove()  # removing from empty queue should assert

    def test_move_front_to_rear(self):
        # target empty, source non-empty
        target = Queue()
        source = Queue()
        for v in [7, 8, 9]:
            source.insert(v)

        target._move_front_to_rear(source)
        # target should now contain [7], source [8,9]
        self.assertEqual(list(target), [7])
        self.assertEqual(list(source), [8, 9])
        self.assertEqual(target._count, 1)
        self.assertEqual(source._count, 2)

        # move remaining
        target._move_front_to_rear(source)
        target._move_front_to_rear(source)
        self.assertEqual(list(target), [7, 8, 9])
        self.assertTrue(source.is_empty())

    def test_append_queue(self):
        t = Queue()
        s = Queue()
        for v in [1, 2]:
            t.insert(v)
        for v in [3, 4, 5]:
            s.insert(v)

        t._append_queue(s)
        # t should be [1,2,3,4,5], s empty
        self.assertEqual(list(t), [1, 2, 3, 4, 5])
        self.assertTrue(s.is_empty())
        self.assertEqual(t._count, 5)

        # appending onto empty target should transfer wholesale
        t2 = Queue()
        s2 = Queue()
        for v in [9, 10]:
            s2.insert(v)
        t2._append_queue(s2)
        self.assertEqual(list(t2), [9, 10])
        self.assertTrue(s2.is_empty())

    def test_combine(self):
        target = Queue()
        s1 = Queue()
        s2 = Queue()
        for v in [1, 3, 5]:
            s1.insert(v)
        for v in [2, 4, 6, 8]:
            s2.insert(v)

        target.combine(s1, s2)
        # starts with s1 first then s2 interlaced
        self.assertEqual(list(target), [1, 2, 3, 4, 5, 6, 8])
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.is_empty())
        self.assertEqual(target._count, 7)

        # combine when one source is empty
        t2 = Queue()
        s3 = Queue()
        s4 = Queue()
        for v in [10, 11]:
            s3.insert(v)
        # s4 empty
        t2.combine(s3, s4)
        self.assertEqual(list(t2), [10, 11])
        self.assertTrue(s3.is_empty())

    def test_split_alt(self):
        s = Queue()
        for v in [0, 1, 2, 3, 4]:
            s.insert(v)

        a, b = s.split_alt()
        # s should be empty
        self.assertTrue(s.is_empty())
        # a should get 0,2,4 ; b should get 1,3
        self.assertEqual(list(a), [0, 2, 4])
        self.assertEqual(list(b), [1, 3])

        # split on single element
        s2 = Queue()
        s2.insert("only")
        a2, b2 = s2.split_alt()
        self.assertEqual(list(a2), ["only"])
        self.assertTrue(b2.is_empty())

    def test_eq_and_count_edgecases(self):
        a = Queue()
        b = Queue()
        for v in [1, 2, 3]:
            a.insert(v)
            b.insert(v)
        self.assertTrue(a == b)

        # different lengths
        b.insert(4)
        self.assertFalse(a == b)

        # different values same length
        c = Queue()
        for v in [1, 9, 3]:
            c.insert(v)
        self.assertFalse(a == c)

        # equality with falsy values inside nodes
        x = Queue()
        y = Queue()
        for v in [0, "", False]:
            x.insert(v)
            y.insert(v)
        self.assertTrue(x == y)

        # iterator yields the same sequence as equality expects
        self.assertEqual(list(a), [1, 2, 3])

    def test_iter_and_len_after_operations(self):
        q = Queue()
        q.insert(1)
        q.insert(2)
        self.assertEqual(len(q), 2)
        q.remove()
        self.assertEqual(len(q), 1)
        q.insert(3)
        self.assertEqual(list(q), [2, 3])

    def test_internal_node_independence(self):
        # ensure node deepcopy semantics: modifying original value won't change stored node
        v = [1, 2]
        q = Queue()
        q.insert(v)
        v.append(3)
        # queue stored a deepcopy, so list in queue shouldn't have 3
        stored = list(q)[0]
        self.assertEqual(stored, [1, 2])

    def test_exceptions(self):
        q = Queue()
        with self.assertRaises(AssertionError):
            q.remove()
        with self.assertRaises(AssertionError):
            q.peek()


if __name__ == "__main__":
    unittest.main()
