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

# t01.py
# Quick test harness for List_linked List class
# Put this file in the same folder as your List_linked.py and run it.

import traceback

# Try import from List_linked (common assignment filename)
try:
    from List_linked import List
except Exception:
    # If that fails, try alternative names or assume List defined in same file
    try:
        from list_linked import List
    except Exception:
        raise ImportError("Cannot import List from List_linked.py. Rename module or update import in t01.py.")

def pylist_from_list(lst):
    return [v for v in lst]

def build_list(values):
    l = List()
    for v in values:
        l.append(v)
    return l

def equal_pylist(lst, expected):
    return pylist_from_list(lst) == expected

tests_passed = 0
tests_total = 0

def run_test(name, fn):
    global tests_passed, tests_total
    tests_total += 1
    try:
        ok = fn()
        if ok:
            print(f"[PASS] {name}")
            tests_passed += 1
        else:
            print(f"[FAIL] {name}")
    except Exception:
        print(f"[ERROR] {name} raised an exception:")
        traceback.print_exc()

# Tests

def test_append_prepend_remove_front():
    l = List()
    l.append(1)
    l.append(2)
    l.prepend(0)
    a = pylist_from_list(l)
    if a != [0,1,2]:
        return False
    v = l.remove_front()
    if v != 0:
        return False
    return pylist_from_list(l) == [1,2]

def test_remove_many_and_count():
    l = build_list([1,2,2,3,2,4])
    l.remove_many(2)
    return pylist_from_list(l) == [1,3,4] and l.count(2) == 0 and l.count(3) == 1

def test_clean():
    l = build_list([1,2,1,3,2,4,3])
    l.clean()
    # first occurrence preserved => [1,2,3,4]
    return pylist_from_list(l) == [1,2,3,4]

def test_split_empty_and_single():
    l = List()
    a,b = l.split()
    if not (equal_pylist(a, []) and equal_pylist(b, [])):
        return False
    l2 = List()
    l2.append(99)
    a,b = l2.split()
    return equal_pylist(a, [99]) and equal_pylist(b, []) and l2._front is None

def test_split_even_odd_counts():
    l = build_list([11,22,33,44])
    a,b = l.split()
    # first half should be 2 elements, second half 2 elements
    return equal_pylist(a, [11,22]) and equal_pylist(b, [33,44]) and l._front is None

def test_split_odd_count():
    l = build_list([1,2,3,4,5])
    a,b = l.split()
    # first must have ceil(n/2)=3
    return equal_pylist(a, [1,2,3]) and equal_pylist(b, [4,5]) and l._front is None

def test_split_alt_empty_and_single():
    l = List()
    a,b = l.split_alt()
    if not (equal_pylist(a, []) and equal_pylist(b, [])):
        return False
    l2 = List()
    l2.append(5)
    a,b = l2.split_alt()
    return equal_pylist(a, [5]) and equal_pylist(b, []) and l2._front is None

def test_split_alt_pattern():
    l = build_list([1,2,3,4,5,6])
    a,b = l.split_alt()
    # alternating, a starts with first element
    return equal_pylist(a, [1,3,5]) and equal_pylist(b, [2,4,6]) and l._front is None

def test_combine_both_empty():
    t = List()
    s1 = List()
    s2 = List()
    t.combine(s1, s2)
    return equal_pylist(t, []) and s1._front is None and s2._front is None

def test_combine_one_empty_other_nonempty():
    t = List()
    s1 = build_list([1,3,5])
    s2 = List()
    t.combine(s1, s2)
    # combine should alternate but if second empty, first elements moved in order
    return equal_pylist(t, [1,3,5]) and s1._front is None and s2._front is None

def test_combine_both_nonempty():
    t = List()
    s1 = build_list([11,33])
    s2 = build_list([22,44,66])
    t.combine(s1, s2)
    # expected interlaced: 11,22,33,44,66
    return equal_pylist(t, [11,22,33,44,66]) and s1._front is None and s2._front is None

def test_union_basic():
    t = List()
    s1 = build_list([1,2,3])
    s2 = build_list([3,4,5])
    t.union(s1, s2)
    # union should contain unique values from both. Since union implementation depends on append order,
    # we expect [1,2,3,4,5] (in test implementation appended s1 then s2 skipping existing)
    return equal_pylist(t, [1,2,3,4,5])

def test_intersection_basic():
    t = List()
    s1 = build_list([1,2,3,4])
    s2 = build_list([3,4,5])
    t.intersection(s1, s2)
    # intersection should be values present in both, no repeats, in order encountered from source1
    return equal_pylist(t, [3,4])

# run tests
test_functions = [
    ("append/prepend/remove_front", test_append_prepend_remove_front),
    ("remove_many and count", test_remove_many_and_count),
    ("clean", test_clean),
    ("split empty & single", test_split_empty_and_single),
    ("split even/odd counts", test_split_even_odd_counts),
    ("split odd count", test_split_odd_count),
    ("split_alt empty & single", test_split_alt_empty_and_single),
    ("split_alt pattern", test_split_alt_pattern),
    ("combine both empty", test_combine_both_empty),
    ("combine one empty", test_combine_one_empty_other_nonempty),
    ("combine both nonempty", test_combine_both_nonempty),
    ("union basic", test_union_basic),
    ("intersection basic", test_intersection_basic),
]

for name, fn in test_functions:
    run_test(name, fn)

print()
print(f"RESULT: {tests_passed}/{tests_total} tests passed.")
if tests_passed != tests_total:
    print("Some tests failed — inspect failures and the printed tracebacks for errors.")
else:
    print("All tests passed! 🎉")
