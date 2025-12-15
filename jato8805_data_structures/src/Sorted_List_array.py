"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-11"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy

class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        i = self._binary_search(key)
        result = True if i != -1 else False
        return result

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        if i < 0:
            i = len(self._values) + i
        result = deepcopy(self._values[i])
        return result

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        result = len(self._values)
        return result

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        lo = 0
        hi = len(self._values) - 1
        found = -1
        # binary search for leftmost match
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._values[mid] == key:
                found = mid
                hi = mid - 1
            elif self._values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        result = found
        return result

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        result = (-n <= i < n)
        return result

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        if not self._values:
            result = None
            return result
        new_values = []
        prev = None
        first = True
        for v in self._values:
            if first or v != prev:
                new_values.append(deepcopy(v))
                prev = v
                first = False
            else:
                prev = v
        self._values = new_values
        result = None
        return result

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        a = source1._values
        b = source2._values
        i = 0
        j = 0
        merged = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(deepcopy(a[i]))
                i += 1
            else:
                merged.append(deepcopy(b[j]))
                j += 1
        while i < len(a):
            merged.append(deepcopy(a[i]))
            i += 1
        while j < len(b):
            merged.append(deepcopy(b[j]))
            j += 1
        source1._values = []
        source2._values = []
        self._values = merged
        result = None
        return result

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        target = Sorted_List()
        target._values = [deepcopy(v) for v in self._values]
        result = target
        return result

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        cnt = 0
        first = self._binary_search(key)
        if first != -1:
            idx = first
            n = len(self._values)
            while idx < n and self._values[idx] == key:
                cnt += 1
                idx += 1
        result = cnt
        return result

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._binary_search(key)
        result = deepcopy(self._values[i]) if i != -1 else None
        return result

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        result = self._binary_search(key)
        return result

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # find insertion index to place after existing equal elements (stable)
        lo = 0
        hi = len(self._values)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._values[mid] <= value:
                lo = mid + 1
            else:
                hi = mid
        self._values[lo:lo] = [deepcopy(value)]
        result = None
        return result

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        a = source1._values
        b = source2._values
        i = 0
        j = 0
        new_values = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                if not new_values or new_values[-1] != a[i]:
                    new_values.append(deepcopy(a[i]))
                i += 1
                j += 1
        self._values = new_values
        result = None
        return result

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        result = len(self._values) == 0
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
            target - a list (Sorted_Lists)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = self._values == target._values
        return equals

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        result = deepcopy(self._values[-1])
        return result

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'
        result = deepcopy(self._values[0])
        return result

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'
        result = deepcopy(self._values[0])
        return result

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"
        if len(args) == 1:
            i = args[0]
            value = self._values.pop(i)
        else:
            value = self._values.pop()
        result = deepcopy(value)
        return result

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        i = self._binary_search(key)
        if i != -1:
            value = deepcopy(self._values.pop(i))
        result = value
        return result

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'
        value = deepcopy(self._values.pop(0))
        result = value
        return result

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        if not self._values:
            result = None
            return result
        first = self._binary_search(key)
        if first == -1:
            result = None
            return result
        i = first
        n = len(self._values)
        while i < n and self._values[i] == key:
            i += 1
        # keep items before first and after the block
        self._values = [deepcopy(v) for v in (self._values[:first] + self._values[i:])]
        result = None
        return result

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        n = len(self._values)
        mid = (n + 1) // 2
        target1 = Sorted_List()
        target2 = Sorted_List()
        target1._values = [deepcopy(v) for v in self._values[:mid]]
        target2._values = [deepcopy(v) for v in self._values[mid:]]
        self._values = []
        result = (target1, target2)
        return result

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for idx, v in enumerate(self._values):
            if idx % 2 == 0:
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
        self._values = []
        result = (target1, target2)
        return result

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for v in self._values:
            if func(v):
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
        self._values = []
        result = (target1, target2)
        return result

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for v in self._values:
            if v < key:
                target1._values.append(deepcopy(v))
            else:
                target2._values.append(deepcopy(v))
        self._values = []
        result = (target1, target2)
        return result

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        a = source1._values
        b = source2._values
        i = 0
        j = 0
        new_values = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if not new_values or new_values[-1] != a[i]:
                    new_values.append(deepcopy(a[i]))
                i += 1
            elif a[i] > b[j]:
                if not new_values or new_values[-1] != b[j]:
                    new_values.append(deepcopy(b[j]))
                j += 1
            else:
                if not new_values or new_values[-1] != a[i]:
                    new_values.append(deepcopy(a[i]))
                i += 1
                j += 1
        while i < len(a):
            if not new_values or new_values[-1] != a[i]:
                new_values.append(deepcopy(a[i]))
            i += 1
        while j < len(b):
            if not new_values or new_values[-1] != b[j]:
                new_values.append(deepcopy(b[j]))
            j += 1
        source1._values = []
        source2._values = []
        self._values = new_values
        result = None
        return result

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
