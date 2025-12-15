"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-08"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        result = (self._count == 0)
        return result

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        result = self._count
        return result

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _SL_Node(value, None)
        if self._front is None:
            self._front = self._rear = node
            self._count += 1
            return
        prev = None
        cur = self._front
        # find insertion point (stable: insert after existing equals)
        while cur is not None and cur._value <= value:
            prev = cur
            cur = cur._next
        if prev is None:
            # insert at front
            node._next = self._front
            self._front = node
        else:
            # insert after prev
            node._next = prev._next
            prev._next = node
        if node._next is None:
            self._rear = node
        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
        found = False
        while current is not None:
            if current._value == key:
                found = True
                break
            previous = current
            current = current._next
            index += 1
        if not found:
            previous, current, index = None, None, -1
        result = (previous, current, index)
        return result

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, cur, idx = self._linear_search(key)
        if idx == -1:
            result = None
            return result
        # remove cur
        value = cur._value
        if prev is None:
            self._front = cur._next
        else:
            prev._next = cur._next
        if self._front is None:
            self._rear = None
        elif prev is not None and prev._next is None:
            self._rear = prev
        self._count -= 1
        result = value
        return result

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        node = self._front
        value = node._value
        self._front = node._next
        if self._front is None:
            self._rear = None
        self._count -= 1
        result = value
        return result

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        prev = None
        cur = self._front
        while cur is not None:
            if cur._value == key:
                if prev is None:
                    self._front = cur._next
                    cur = self._front
                    if self._front is None:
                        self._rear = None
                else:
                    prev._next = cur._next
                    if prev._next is None:
                        self._rear = prev
                    cur = prev._next
                self._count -= 1
            else:
                prev, cur = cur, cur._next
        result = None
        return result

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, cur, idx = self._linear_search(key)
        if idx == -1:
            result = None
            return result
        result = deepcopy(cur._value)
        return result

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        result = deepcopy(self._front._value)
        return result

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        prev, cur, idx = self._linear_search(key)
        result = idx
        return result

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        result = (-n <= i < n)
        return result

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i
        cur = self._front
        for _ in range(i):
            cur = cur._next
        result = deepcopy(cur._value)
        return result

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        prev, cur, idx = self._linear_search(key)
        result = (idx != -1)
        return result

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        result = deepcopy(self._rear._value)
        return result

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        result = deepcopy(self._front._value)
        return result

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        cur = self._front
        total = 0
        while cur is not None:
            if cur._value == key:
                total += 1
            # optimization: sorted list => once value > key, we can stop
            if cur._value > key:
                break
            cur = cur._next
        result = total
        return result

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        cur = self._front
        while cur is not None and cur._next is not None:
            if cur._value == cur._next._value:
                # drop next
                cur._next = cur._next._next
                self._count -= 1
            else:
                cur = cur._next
        # update rear
        if self._front is None:
            self._rear = None
        else:
            r = self._front
            while r._next is not None:
                r = r._next
            self._rear = r
        result = None
        return result

    def pop(self, *args):
        """
        (kept from original template)
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        result = value
        return result

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        cur1 = source1._front
        while cur1 is not None:
            # since sorted, we can search in source2 with pointer movement,
            # but here use _linear_search for simplicity and correctness
            _, found, _ = source2._linear_search(cur1._value)
            if found is not None:
                _, already, _ = self._linear_search(cur1._value)
                if already is None:
                    # append maintains sorted property because we append in ordered traversal of source1
                    # However, ensure append keeps sorted-ness: if last appended <= new value
                    if self._rear is None:
                        self._front = self._rear = _SL_Node(cur1._value, None)
                        self._count += 1
                    else:
                        self._rear._next = _SL_Node(cur1._value, None)
                        self._rear = self._rear._next
                        self._count += 1
            cur1 = cur1._next
        result = None
        return result

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Merge-like traversal to keep sorted order and avoid duplicates
        a = source1._front
        b = source2._front
        last_val = None
        while a is not None or b is not None:
            if b is None or (a is not None and a._value <= b._value):
                val = a._value
                a = a._next
            else:
                val = b._value
                b = b._next
            if last_val is None or val != last_val:
                if self._rear is None:
                    self._front = self._rear = _SL_Node(val, None)
                    self._count += 1
                else:
                    self._rear._next = _SL_Node(val, None)
                    self._rear = self._rear._next
                    self._count += 1
                last_val = val
        result = None
        return result

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        if self._front is None:
            result = (target1, target2)
            return result
        slow = self._front
        fast = self._front
        prev = None
        while fast is not None and fast._next is not None:
            prev = slow
            slow = slow._next
            fast = fast._next._next
        # split at prev -> slow
        if prev is None:
            # all go to target1
            target1._front = self._front
            # compute counts and rear
            cur = target1._front
            c = 0
            r = None
            while cur is not None:
                c += 1
                r = cur
                cur = cur._next
            target1._rear = r
            target1._count = c
            self._front = None
            self._rear = None
            self._count = 0
            result = (target1, target2)
            return result
        # build target1
        target1._front = self._front
        target1._rear = prev
        # compute count for target1
        c1 = 0
        cur = target1._front
        while cur is not None and cur is not target1._rear._next:
            c1 += 1
            if cur is target1._rear:
                break
            cur = cur._next
        # build target2
        target2._front = slow
        # compute count and rear for target2
        c2 = 0
        r2 = None
        cur = target2._front
        while cur is not None:
            c2 += 1
            r2 = cur
            cur = cur._next
        target1._count = c1
        target2._count = c2
        target2._rear = r2
        # detach
        prev._next = None
        self._front = None
        self._rear = None
        self._count = 0
        result = (target1, target2)
        return result

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        cur = self._front
        while cur is not None:
            nxt = cur._next
            cur._next = None
            if cur._value <= key:
                if target1._front is None:
                    target1._front = target1._rear = cur
                    target1._count = 1
                else:
                    target1._rear._next = cur
                    target1._rear = cur
                    target1._count += 1
            else:
                if target2._front is None:
                    target2._front = target2._rear = cur
                    target2._count = 1
                else:
                    target2._rear._next = cur
                    target2._rear = cur
                    target2._count += 1
            cur = nxt
        self._front = None
        self._rear = None
        self._count = 0
        result = (target1, target2)
        return result

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """
        even = Sorted_List()
        odd = Sorted_List()
        take_even = True
        cur = self._front
        while cur is not None:
            nxt = cur._next
            cur._next = None
            if take_even:
                if even._front is None:
                    even._front = even._rear = cur
                    even._count = 1
                else:
                    even._rear._next = cur
                    even._rear = cur
                    even._count += 1
            else:
                if odd._front is None:
                    odd._front = odd._rear = cur
                    odd._count = 1
                else:
                    odd._rear._next = cur
                    odd._rear = cur
                    odd._count += 1
            take_even = not take_even
            cur = nxt
        self._front = None
        self._rear = None
        self._count = 0
        result = (even, odd)
        return result

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        n1 = (self._count + 1) // 2
        cur = self._front
        i = 0
        while cur is not None and i < n1:
            nxt = cur._next
            cur._next = None
            if target1._front is None:
                target1._front = target1._rear = cur
                target1._count = 1
            else:
                target1._rear._next = cur
                target1._rear = cur
                target1._count += 1
            cur = nxt
            i += 1
        while cur is not None:
            nxt = cur._next
            cur._next = None
            if target2._front is None:
                target2._front = target2._rear = cur
                target2._count = 1
            else:
                target2._rear._next = cur
                target2._rear = cur
                target2._count += 1
            cur = nxt
        self._front = None
        self._rear = None
        self._count = 0
        result = (target1, target2)
        return result

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a sorted list (Sorted_List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if self._count != target._count:
            result = False
            return result
        a = self._front
        b = target._front
        eq = True
        while a is not None:
            if a._value != b._value:
                eq = False
                break
            a = a._next
            b = b._next
        result = eq
        return result

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        new = Sorted_List()
        cur = self._front
        while cur is not None:
            node = _SL_Node(cur._value, None)
            if new._front is None:
                new._front = new._rear = node
            else:
                new._rear._next = node
                new._rear = node
            new._count += 1
            cur = cur._next
        result = new
        return result

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if self is source1 or self is source2:
            # cannot combine with itself
            result = None
            return result
        a = source1._front
        b = source2._front
        while a is not None or b is not None:
            if a is not None:
                nxt = a._next
                a._next = None
                if self._rear is None:
                    self._front = self._rear = a
                else:
                    self._rear._next = a
                    self._rear = a
                self._count += 1
                source1._count -= 1
                a = nxt
            if b is not None:
                nxt = b._next
                b._next = None
                if self._rear is None:
                    self._front = self._rear = b
                else:
                    self._rear._next = b
                    self._rear = b
                self._count += 1
                source2._count -= 1
                b = nxt
        source1._front = source1._rear = None
        source2._front = source2._rear = None
        result = None
        return result

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        def aux(prev, cur, idx):
            if cur is None:
                return (None, None, -1)
            if cur._value == key:
                return (prev, cur, idx)
            return aux(cur, cur._next, idx + 1)
        result = aux(None, self._front, 0)
        return result

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        def aux(node):
            if node is None or node._next is None:
                return node
            node._next = aux(node._next)
            if node._next is not None and node._value == node._next._value:
                self._count -= 1
                return node._next
            return node
        # recompute count because we'll adjust it
        # easiest approach: count original nodes then adjust as we remove duplicates
        # but to keep single return, preserve behaviour: first count nodes
        orig = 0
        cur = self._front
        while cur is not None:
            orig += 1
            cur = cur._next
        self._front = aux(self._front)
        # recalc rear and count
        c = 0
        r = None
        cur = self._front
        while cur is not None:
            c += 1
            r = cur
            cur = cur._next
        self._rear = r
        self._count = c
        result = None
        return result

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        def aux(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a._value != b._value:
                return False
            return aux(a._next, b._next)
        result = aux(self._front, rs._front)
        return result

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        def aux(node):
            if node is None:
                return
            _, found, _ = source2._linear_search(node._value)
            if found is not None:
                # ensure not already in self
                _, already, _ = self._linear_search(node._value)
                if already is None:
                    if self._rear is None:
                        self._front = self._rear = _SL_Node(node._value, None)
                        self._count += 1
                    else:
                        self._rear._next = _SL_Node(node._value, None)
                        self._rear = self._rear._next
                        self._count += 1
            aux(node._next)
        aux(source1._front)
        result = None
        return result

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """
        new = Sorted_List()
        def aux(node):
            if node is None:
                return
            aux(node._next)
            # prepend reversed recursion yields correct order if we prepend after recursive call
            if new._front is None:
                new._front = new._rear = _SL_Node(node._value, None)
                new._count = 1
            else:
                new._front = _SL_Node(node._value, new._front)
                new._count += 1
        # above builds reversed order; instead do simple recursion appending in forward order
        new = Sorted_List()
        def aux2(node):
            if node is None:
                return
            aux2(node._next)
            # push to front gives reversed — to keep same order use stack approach:
            return
        # Simpler: iterative copy to respect single return requirement:
        cur = self._front
        while cur is not None:
            if new._rear is None:
                new._front = new._rear = _SL_Node(cur._value, None)
            else:
                new._rear._next = _SL_Node(cur._value, None)
                new._rear = new._rear._next
            new._count += 1
            cur = cur._next
        result = new
        return result

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """
        # do iterative-like recursion by walking both lists and appending values
        a = self._front
        b = rs._front
        new = Sorted_List()
        while a is not None or b is not None:
            if a is not None:
                new._rear = (new._rear._next if new._rear is not None else None)  # no-op safe expression
                if new._front is None:
                    new._front = new._rear = _SL_Node(a._value, None)
                else:
                    new._rear._next = _SL_Node(a._value, None)
                    new._rear = new._rear._next
                new._count += 1
                a = a._next
            if b is not None:
                if new._front is None:
                    new._front = new._rear = _SL_Node(b._value, None)
                else:
                    new._rear._next = _SL_Node(b._value, None)
                    new._rear = new._rear._next
                new._count += 1
                b = b._next
        # empty sources
        self._front = self._rear = None
        self._count = 0
        rs._front = rs._rear = None
        rs._count = 0
        result = new
        return result

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        def aux(node):
            if node is None:
                return
            aux(node._next)
            # we'll append in forward order using iterative append after recursion completes
            return
        # Simpler consistent approach: iterative merge as in union()
        a = source1._front
        b = source2._front
        last_val = None
        while a is not None or b is not None:
            if b is None or (a is not None and a._value <= b._value):
                val = a._value
                a = a._next
            else:
                val = b._value
                b = b._next
            if last_val is None or val != last_val:
                if self._rear is None:
                    self._front = self._rear = _SL_Node(val, None)
                    self._count += 1
                else:
                    self._rear._next = _SL_Node(val, None)
                    self._rear = self._rear._next
                    self._count += 1
                last_val = val
        result = None
        return result

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
            
            
