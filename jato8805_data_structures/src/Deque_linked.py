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
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, prev_, next_):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, prev_, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            prev_ - another deque node (_Deque_Node)
            next_ - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = prev_
        self._next = next_


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        result = (self._count == 0)
        return result

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        size = self._count
        return size

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = True

        if self._count != getattr(target, "_count", None):
            equals = False
        else:
            cur = self._front
            curt = target._front

            while cur is not None and curt is not None and equals:
                if cur._value != curt._value:
                    equals = False
                cur = cur._next
                curt = curt._next

        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, None)

        if self._front is None:
            # empty deque
            self._front = node
            self._rear = node
        else:
            # link at front
            node._next = self._front
            self._front._prev = node
            self._front = node

        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, None)

        if self._rear is None:
            # empty deque
            self._front = node
            self._rear = node
        else:
            node._prev = self._rear
            self._rear._next = node
            self._rear = node

        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        value = deepcopy(self._front._value)

        if self._front is self._rear:
            # single node
            self._front = None
            self._rear = None
        else:
            # advance front
            new_front = self._front._next
            new_front._prev = None
            self._front._next = None  # detach old front
            self._front = new_front

        self._count -= 1
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        value = deepcopy(self._rear._value)

        if self._front is self._rear:
            # single node
            self._front = None
            self._rear = None
        else:
            # move rear backward
            new_rear = self._rear._prev
            new_rear._next = None
            self._rear._prev = None  # detach old rear
            self._rear = new_rear

        self._count -= 1
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        val = deepcopy(self._front._value)
        return val

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        val = deepcopy(self._rear._value)
        return val

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
    
        # default: do nothing, single exit point at the end
        did_swap = False
    
        # no-op if same node
        if l is r:
            did_swap = True  # treat as done
        else:
            # adjacency cases
            if l._next is r:
                # l before r
                l_prev = l._prev
                r_next = r._next
    
                # link l_prev -> r (or update front)
                if l_prev is not None:
                    l_prev._next = r
                else:
                    self._front = r
    
                # link r_next -> l (or update rear)
                if r_next is not None:
                    r_next._prev = l
                else:
                    self._rear = l
    
                # swap internal pointers between l and r
                r._prev = l_prev
                l._next = r_next
    
                r._next = l
                l._prev = r
    
                did_swap = True
    
            elif r._next is l:
                # r before l (mirror of above)
                r_prev = r._prev
                l_next = l._next
    
                if r_prev is not None:
                    r_prev._next = l
                else:
                    self._front = l
    
                if l_next is not None:
                    l_next._prev = r
                else:
                    self._rear = r
    
                l._prev = r_prev
                r._next = l_next
    
                l._next = r
                r._prev = l
    
                did_swap = True
    
            else:
                # non-adjacent case
                l_prev = l._prev
                l_next = l._next
                r_prev = r._prev
                r_next = r._next
    
                # reconnect neighbors to opposite nodes
                if l_prev is not None:
                    l_prev._next = r
                else:
                    self._front = r
    
                if l_next is not None:
                    l_next._prev = r
                else:
                    self._rear = r
    
                if r_prev is not None:
                    r_prev._next = l
                else:
                    self._front = l
    
                if r_next is not None:
                    r_next._prev = l
                else:
                    self._rear = l
    
                # swap l and r's prev/next pointers
                l._prev, r._prev = r_prev, l_prev
                l._next, r._next = r_next, l_next
    
                did_swap = True
    
        # single exit point; nothing to return (explicit None)
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
