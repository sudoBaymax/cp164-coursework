"""
-------------------------------------------------------
Array version of the list ADT.
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-11"
-------------------------------------------------------
"""
from copy import deepcopy


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: target = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        # normalize negative index like Python
        if i < 0:
            i = len(self._values) + i

        return deepcopy(self._values[i])

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # underlying Python list length is the number of items
        return len(self._values)

    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of list contains a copy of value. The existing
        value at i is overwritten.
        Use: source[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        if i < 0:
            i = len(self._values) + i

        self._values[i] = deepcopy(value)

        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(key)

        return i > -1

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
        n = len(self._values)
        # valid: -n <= i < n  (matching Python get/set semantics)
        return -n <= i < n

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        i = 0
        while i < len(self._values) and self._values[i] != key:
            i += 1

        return i if i < len(self._values) else -1

    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        The element originally at position i is now at position j,
        and visa versa.
        Private helper operations called only from within class.
        Use: self._swap(i, j)
        -------------------------------------------------------
        Parameters:
            i - index of one element to switch (int, 0 <= i < len(self._values))
            j - index of other element to switch (int, 0 <= j < len(self._values))
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index i'
        assert self._is_valid_index(j), 'Invalid index j'

        # normalize negative indices
        if i < 0:
            i = len(self._values) + i
        if j < 0:
            j = len(self._values) + j

        self._values[i], self._values[j] = self._values[j], self._values[i]

        return

    def append(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # store a deep copy to preserve ADT copy semantics
        self._values += [deepcopy(value)]
        return

    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external function to every value in list.
        Use: source.apply(func)
        -------------------------------------------------------
        Parameters:
          func - a function that takes a single value as a parameter
              and returns a value (function)
        Returns:
            None
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            self._values[i] = deepcopy(func(self._values[i]))

        return

    def clean(self):
        """
        ---------------------------------------------------------
        The list contains one and only one of each value formerly present
        in the list. The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        new_values = []
        for v in self._values:
            found = False
            for u in new_values:
                if u == v:
                    found = True
                    break
            if not found:
                new_values.append(v)

        # preserve copy-semantics
        self._values = [deepcopy(v) for v in new_values]
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        """
        # Interleave popping from front of sources (preserves order)
        while len(source1._values) > 0 or len(source2._values) > 0:
            if len(source1._values) > 0:
                val = source1._values.pop(0)
                self._values.append(deepcopy(val))
            if len(source2._values) > 0:
                val = source2._values.pop(0)
                self._values.append(deepcopy(val))
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
        target = List()
        target._values = [deepcopy(v) for v in self._values]
        return target

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        cnt = 0
        for v in self._values:
            if v == key:
                cnt += 1
        return cnt

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return deepcopy(self._values[i]) if i != -1 else None

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """
        return self._linear_search(key)

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is
        prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        """
        # Python list.insert handles out-of-range indexes in a sensible way.
        self._values.insert(i, deepcopy(value))
        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        """
        self._values = []
        for v in source1._values:
            # check membership in source2
            found_in_s2 = False
            for u in source2._values:
                if u == v:
                    found_in_s2 = True
                    break
            if found_in_s2:
                # ensure not already added
                already = False
                for t in self._values:
                    if t == v:
                        already = True
                        break
                if not already:
                    self._values.append(deepcopy(v))
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        """
        result = False  
        if isinstance(target, List):
            result = self._values == target._values
        return result

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        max_value = self._values[0]
        for v in self._values:
            if v > max_value:
                max_value = v
        return deepcopy(max_value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        min_value = self._values[0]
        for v in self._values:
            if v < min_value:
                min_value = v
        return deepcopy(min_value)

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        return deepcopy(self._values[0])

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        # return a deepcopy to preserve ADT semantics
        return deepcopy(value)

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: source.prepend(value)
        -------------------------------------------------------
        """
        self._values.insert(0, deepcopy(value))
        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        """
        value = None
        i = self._linear_search(key)
        if i != -1:
            value = deepcopy(self._values.pop(i))
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        return deepcopy(self._values.pop(0))

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: source.remove_many(key)
        -------------------------------------------------------
        """
        # rebuild list without the matching key (keeps first/others)
        self._values = [v for v in self._values if v != key]
        return

    def reverse(self):
        """
        -------------------------------------------------------
        The contents of list are reversed in order with respect
        to their order before the operation was called.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        left = 0
        right = len(self._values) - 1
        while left < right:
            self._values[left], self._values[right] = self._values[right], self._values[left]
            left += 1
            right -= 1
        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        n = len(self._values)
        mid = (n + 1) // 2  # ensure target1 has >= 50% when odd
        target1 = List()
        target2 = List()
        target1._values = [deepcopy(v) for v in self._values[:mid]]
        target2._values = [deepcopy(v) for v in self._values[mid:]]
        # empty the source
        self._values = []
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        toggle = True
        for v in self._values:
            if toggle:
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
            toggle = not toggle
        self._values = []
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        for v in self._values:
            if func(v):
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
        self._values = []
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key. source is empty
        at end.
        Use: target1, target2 = source.split_key()
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        for v in self._values:
            if v < key:
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
        self._values = []
        return target1, target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        """
        self._values = []
        # add from source1 preserving order
        for v in source1._values:
            already = False
            for t in self._values:
                if t == v:
                    already = True
                    break
            if not already:
                self._values.append(deepcopy(v))
        # add from source2 preserving order (only new ones)
        for v in source2._values:
            already = False
            for t in self._values:
                if t == v:
                    already = True
                    break
            if not already:
                self._values.append(deepcopy(v))
        # empty sources (common ADT convention for union/combine in this assignment)
        source1._values = []
        source2._values = []
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
