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

# t01_deque.py
import unittest
from copy import deepcopy
from Deque_linked import Deque, _Deque_Node


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.empty = Deque()

        # deque with values 1..5 (front -> rear)
        self.d = Deque()
        for v in [1, 2, 3, 4, 5]:
            self.d.insert_rear(v)

    def nodes_list(self, d):
        """Helper: return list of node objects in order (front -> rear)."""
        cur = d._front
        nodes = []
        while cur is not None:
            nodes.append(cur)
            cur = cur._next
        return nodes

    def values(self, d):
        """Helper: return list of values front->rear."""
        return list(d)

    def test_basic_ops_and_deepcopy(self):
        d = Deque()
        self.assertTrue(d.is_empty())
        self.assertEqual(len(d), 0)

        d.insert_front(10)
        d.insert_rear(20)
        d.insert_front(5)
        self.assertEqual(self.values(d), [5, 10, 20])
        self.assertFalse(d.is_empty())
        self.assertEqual(len(d), 3)

        # deepcopy semantics: modifying original inserted object doesn't change stored copy
        lst = [1, 2]
        d2 = Deque()
        d2.insert_rear(lst)
        lst.append(3)
        self.assertEqual(self.values(d2)[0], [1, 2])

        # peek and remove
        self.assertEqual(d.peek_front(), 5)
        self.assertEqual(d.peek_rear(), 20)
        self.assertEqual(d.remove_front(), 5)
        self.assertEqual(d.remove_rear(), 20)
        self.assertEqual(self.values(d), [10])

    def test_eq_and_iteration(self):
        a = Deque()
        b = Deque()
        for v in [0, 0, 1]:
            a.insert_rear(v)
            b.insert_rear(v)
        self.assertTrue(a == b)
        b.remove_rear()
        self.assertFalse(a == b)

    def test_swap_noop_same_node(self):
        d = deepcopy(self.d)
        nodes = self.nodes_list(d)
        # swap node with itself (3rd element)
        n = nodes[2]
        d._swap(n, n)
        self.assertEqual(self.values(d), [1, 2, 3, 4, 5])
        # check pointers intact
        nodes_after = self.nodes_list(d)
        for i in range(len(nodes_after)):
            val = nodes_after[i]._value
            self.assertEqual(val, i + 1)

    def test_swap_adjacent_l_before_r(self):
        d = deepcopy(self.d)
        # nodes: [1,2,3,4,5]
        nodes = self.nodes_list(d)
        l, r = nodes[1], nodes[2]  # 2 and 3 (adjacent)
        d._swap(l, r)
        # expected order: [1,3,2,4,5]
        self.assertEqual(self.values(d), [1, 3, 2, 4, 5])

        # Check prev/next pointers correctness
        nodes_after = self.nodes_list(d)
        for i in range(len(nodes_after)):
            cur = nodes_after[i]
            if i > 0:
                self.assertIs(cur._prev, nodes_after[i - 1])
            else:
                self.assertIsNone(cur._prev)
            if i < len(nodes_after) - 1:
                self.assertIs(cur._next, nodes_after[i + 1])
            else:
                self.assertIsNone(cur._next)

    def test_swap_adjacent_r_before_l(self):
        d = deepcopy(self.d)
        nodes = self.nodes_list(d)
        r, l = nodes[0], nodes[1]  # r before l (1 and 2), we'll call swap with (l,r) reversed form
        # Call with (l=nodes[1], r=nodes[0]) to hit the r._next is l branch
        d._swap(nodes[1], nodes[0])
        # expected: [2,1,3,4,5]
        self.assertEqual(self.values(d), [2, 1, 3, 4, 5])

    def test_swap_front_and_rear(self):
        d = deepcopy(self.d)
        nodes = self.nodes_list(d)
        front_node = nodes[0]
        rear_node = nodes[-1]
        d._swap(front_node, rear_node)
        # expected: [5,2,3,4,1]
        self.assertEqual(self.values(d), [5, 2, 3, 4, 1])

        # verify front/rear references
        self.assertEqual(d._front._value, 5)
        self.assertEqual(d._rear._value, 1)

    def test_swap_non_adjacent_middle(self):
        d = deepcopy(self.d)
        nodes = self.nodes_list(d)
        # swap 2 and 5 (non-adjacent)
        n2 = nodes[1]
        n5 = nodes[4]
        d._swap(n2, n5)
        # expected order: [1,5,3,4,2]
        self.assertEqual(self.values(d), [1, 5, 3, 4, 2])

        # check pointer correctness
        nodes_after = self.nodes_list(d)
        for i in range(len(nodes_after)):
            cur = nodes_after[i]
            if i > 0:
                self.assertIs(cur._prev, nodes_after[i - 1])
            else:
                self.assertIsNone(cur._prev)
            if i < len(nodes_after) - 1:
                self.assertIs(cur._next, nodes_after[i + 1])
            else:
                self.assertIsNone(cur._next)

    def test_swap_with_duplicate_values(self):
        # build deque with duplicates [1,2,2,3]
        d = Deque()
        for v in [1, 2, 2, 3]:
            d.insert_rear(v)
        nodes = self.nodes_list(d)
        # swap the two middle '2' nodes
        n_a = nodes[1]
        n_b = nodes[2]
        d._swap(n_a, n_b)
        # swapping identical values should still rearrange nodes, resulting in same multiset but positions swapped
        self.assertEqual(sorted(self.values(d)), [1, 2, 2, 3])
        # after swapping adjacent duplicates their order may flip but values list still same length
        self.assertEqual(len(self.values(d)), 4)

    def test_remove_until_empty_and_exceptions(self):
        d = Deque()
        d.insert_rear(1)
        self.assertEqual(d.remove_front(), 1)
        self.assertTrue(d.is_empty())
        # removing again should assert
        with self.assertRaises(AssertionError):
            d.remove_rear()
        with self.assertRaises(AssertionError):
            d.peek_front()
        with self.assertRaises(AssertionError):
            d.peek_rear()

    def test_invariants_after_many_ops(self):
        d = Deque()
        # create sequence
        for i in range(10):
            if i % 2 == 0:
                d.insert_front(i)
            else:
                d.insert_rear(i)
        # iterate a bit and swap some nodes
        nodes = self.nodes_list(d)
        if len(nodes) >= 4:
            d._swap(nodes[0], nodes[3])
            # validate link invariants
            cur = d._front
            prev = None
            count = 0
            while cur is not None:
                self.assertIs(cur._prev, prev)
                prev = cur
                cur = cur._next
                count += 1
            self.assertEqual(count, len(d))

if __name__ == "__main__":
    unittest.main()
