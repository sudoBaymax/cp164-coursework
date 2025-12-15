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

# t02.py
# Run: python t02.py
from types import SimpleNamespace

# Try multiple possible module names for compatibility
_list_module_names = ["List_linked", "list_linked", "List_linked_fixed", "list_linked_fixed"]
_sorted_module_names = ["Sorted_List_linked", "sorted_list_linked", "Sorted_List", "sorted_list"]

List = None
Sorted_List = None

for name in _list_module_names:
    try:
        m = __import__(name)
        if hasattr(m, "List"):
            List = getattr(m, "List")
            break
    except Exception:
        pass

for name in _sorted_module_names:
    try:
        m = __import__(name)
        if hasattr(m, "Sorted_List"):
            Sorted_List = getattr(m, "Sorted_List")
            break
    except Exception:
        pass

if List is None or Sorted_List is None:
    print("WARNING: Could not import List and/or Sorted_List from standard module names.")
    print("Make sure your modules are named one of:", _list_module_names, "and", _sorted_module_names)
    print("This test will fail if imports are missing.")
    # Define minimal fallbacks to avoid crash; tests will obviously fail
    class _Dummy:
        def __init__(self): pass
    if List is None:
        List = _Dummy
    if Sorted_List is None:
        Sorted_List = _Dummy

# Helper utilities
def to_pylist(lst):
    try:
        return [v for v in lst]
    except Exception as e:
        return ("ITER_FAIL", str(e))

def assert_equal(actual, expected):
    return actual == expected

def run_test(name, fn):
    try:
        ok, msg = fn()
        status = "PASS" if ok else "FAIL"
    except Exception as e:
        ok = False
        msg = f"EXCEPTION: {type(e).__name__}: {e}"
        status = "ERROR"
    print(f"{status}: {name} - {msg}")
    return ok

# Tests for List (unsorted)
def test_list_append_and_iter():
    s = List()
    try:
        s.append(99)
        s.append(1)
        arr = to_pylist(s)
        return (arr == [99,1], f"got {arr}")
    except Exception as e:
        return (False, str(e))

def test_list_clean_no_error_on_empty():
    s = List()
    try:
        s.clean()
        return (to_pylist(s) == [], "clean on empty ok")
    except Exception as e:
        return (False, str(e))

def test_list_clean_duplicates():
    s = List()
    for v in [11,11,22,22,33,33]:
        s.append(v)
    s.clean()
    arr = to_pylist(s)
    return (arr == [11,22,33], f"got {arr}")

def test_list_combine_both_empty():
    target = List()
    s1 = List()
    s2 = List()
    try:
        target.combine(s1, s2)
        ok = to_pylist(target) == []
        ok = ok and to_pylist(s1) == [] and to_pylist(s2) == []
        return (ok, f"target={to_pylist(target)} s1={to_pylist(s1)} s2={to_pylist(s2)}")
    except Exception as e:
        return (False, str(e))

def test_list_combine_one_empty_one_nonempty():
    target = List()
    s1 = List()
    s2 = List()
    s2.append(11); s2.append(22); s2.append(33)
    try:
        target.combine(s1, s2)
        arr = to_pylist(target)
        ok = (arr == [11,22,33]) and to_pylist(s1) == [] and to_pylist(s2) == []
        return (ok, f"target={arr}")
    except Exception as e:
        return (False, str(e))

def test_list_combine_both_nonempty():
    target = List()
    s1 = List(); s2 = List()
    for v in [1,3]:
        s1.append(v)
    for v in [2,4,5]:
        s2.append(v)
    try:
        target.combine(s1, s2)
        arr = to_pylist(target)
        ok = (arr == [1,2,3,4,5]) and to_pylist(s1) == [] and to_pylist(s2) == []
        return (ok, f"target={arr}")
    except Exception as e:
        return (False, str(e))

def test_list_split_empty():
    s = List()
    try:
        a,b = s.split()
        ok = to_pylist(a) == [] and to_pylist(b) == [] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_split_one():
    s = List(); s.append(99)
    try:
        a,b = s.split()
        ok = to_pylist(a) == [99] and to_pylist(b) == [] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_split_multiple_even():
    s = List()
    for v in [11,22,33,44]:
        s.append(v)
    try:
        a,b = s.split()
        ok = to_pylist(a) == [11,22] and to_pylist(b) == [33,44] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_split_multiple_odd():
    s = List()
    for v in [11,22,33,44,55]:
        s.append(v)
    try:
        a,b = s.split()
        ok = to_pylist(a) == [11,22,33] and to_pylist(b) == [44,55] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_split_alt_empty():
    s = List()
    try:
        a,b = s.split_alt()
        ok = to_pylist(a) == [] and to_pylist(b) == [] and to_pylist(s) == []
        return (ok, "split_alt empty ok")
    except Exception as e:
        return (False, str(e))

def test_list_split_alt_single():
    s = List(); s.append(99)
    try:
        a,b = s.split_alt()
        ok = to_pylist(a) == [99] and to_pylist(b) == [] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_split_alt_multiple():
    s = List()
    for v in [11,22,33,44,55]:
        s.append(v)
    try:
        a,b = s.split_alt()
        # alternating into a,b starting with a
        ok = to_pylist(a) == [11,33,55] and to_pylist(b) == [22,44] and to_pylist(s) == []
        return (ok, f"a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_list_intersection_basic():
    target = List()
    s1 = List(); s2 = List()
    for v in [11,22,33]:
        s1.append(v)
    for v in [22,33,44]:
        s2.append(v)
    try:
        target.intersection(s1, s2)
        ok = to_pylist(target) == [22,33]
        return (ok, f"got {to_pylist(target)}")
    except Exception as e:
        return (False, str(e))

def test_list_union_basic():
    target = List()
    s1 = List(); s2 = List()
    for v in [11,22,33]:
        s1.append(v)
    for v in [22,44]:
        s2.append(v)
    try:
        target.union(s1, s2)
        arr = to_pylist(target)
        ok = set(arr) == set([11,22,33,44]) and len(arr) == 4
        return (ok, f"got {arr}")
    except Exception as e:
        return (False, str(e))

# Tests for Sorted_List
def test_sorted_insert_and_iter():
    s = Sorted_List()
    try:
        for v in [44,11,33,22]:
            s.insert(v)
        arr = to_pylist(s)
        ok = arr == [11,22,33,44]
        return (ok, f"got {arr}")
    except Exception as e:
        return (False, str(e))

def test_sorted_find_and_peek():
    s = Sorted_List()
    for v in [11,22,33]:
        s.insert(v)
    try:
        found = s.find(22)
        peeked = s.peek()
        ok = (found == 22 and peeked == 11)
        return (ok, f"find={found} peek={peeked}")
    except Exception as e:
        return (False, str(e))

def test_sorted_remove_and_remove_many():
    s = Sorted_List()
    for v in [11,22,22,33]:
        s.insert(v)
    try:
        r = s.remove(22)
        cnt_before = s.count(22)
        s.remove_many(22)
        cnt_after = s.count(22)
        ok = (r == 22 and cnt_before >= 0 and cnt_after == 0)
        return (ok, f"removed {r}, counts {cnt_before}->{cnt_after}")
    except Exception as e:
        return (False, str(e))

def test_sorted_intersection_and_union():
    t = Sorted_List()
    a = Sorted_List(); b = Sorted_List()
    for v in [11,22,33,44]:
        a.insert(v)
    for v in [33,44,55]:
        b.insert(v)
    try:
        t.intersection(a,b)
        inter = to_pylist(t)
        u = Sorted_List()
        u.union(a,b)
        union = to_pylist(u)
        ok = (inter == [33,44]) and set(union) == set([11,22,33,44,55])
        return (ok, f"inter={inter} union={union}")
    except Exception as e:
        return (False, str(e))

def test_sorted_split_th_empty_and_small():
    s = Sorted_List()
    try:
        a,b = s.split_th()
        ok = to_pylist(a) == [] and to_pylist(b) == []
    except Exception as e:
        return (False, str(e))
    s2 = Sorted_List(); s2.insert(99)
    try:
        a,b = s2.split_th()
        ok2 = to_pylist(a) == [99] and to_pylist(b) == []
        return (ok and ok2, f"empty ok and single ok: a={to_pylist(a)} b={to_pylist(b)}")
    except Exception as e:
        return (False, str(e))

def test_sorted_combine_and_combine_r():
    t = Sorted_List()
    a = Sorted_List(); b = Sorted_List()
    for v in [1,3]:
        a.insert(v)
    for v in [2,4,5]:
        b.insert(v)
    try:
        t.combine(a,b)
        arr = to_pylist(t)
        ok = arr == [1,2,3,4,5]
    except Exception as e:
        return (False, str(e))
    # combine_r on others
    t2 = Sorted_List()
    a2 = Sorted_List(); b2 = Sorted_List()
    for v in [1,3]:
        a2.insert(v)
    for v in [2,4]:
        b2.insert(v)
    try:
        t2.combine_r(a2, b2)
        arr2 = to_pylist(t2)
        ok2 = arr2 == [1,2,3,4]
        return (ok and ok2, f"combine={arr} combine_r={arr2}")
    except Exception as e:
        return (False, str(e))

def test_sorted_copy_and_copy_r():
    s = Sorted_List()
    for v in [11,22,33]:
        s.insert(v)
    try:
        c = s.copy()
        cr = s.copy_r()
        ok = to_pylist(c) == [11,22,33] and to_pylist(cr) == [11,22,33]
        return (ok, f"copy={to_pylist(c)} copy_r={to_pylist(cr)}")
    except Exception as e:
        return (False, str(e))

# Assemble tests
tests = [
    ("List append and iter", test_list_append_and_iter),
    ("List clean empty", test_list_clean_no_error_on_empty),
    ("List clean duplicates", test_list_clean_duplicates),
    ("List combine both empty", test_list_combine_both_empty),
    ("List combine one empty", test_list_combine_one_empty_one_nonempty),
    ("List combine both nonempty", test_list_combine_both_nonempty),
    ("List split empty", test_list_split_empty),
    ("List split one", test_list_split_one),
    ("List split multiple even", test_list_split_multiple_even),
    ("List split multiple odd", test_list_split_multiple_odd),
    ("List split_alt empty", test_list_split_alt_empty),
    ("List split_alt single", test_list_split_alt_single),
    ("List split_alt multiple", test_list_split_alt_multiple),
    ("List intersection basic", test_list_intersection_basic),
    ("List union basic", test_list_union_basic),

    ("Sorted insert and iter", test_sorted_insert_and_iter),
    ("Sorted find and peek", test_sorted_find_and_peek),
    ("Sorted remove and remove_many", test_sorted_remove_and_remove_many),
    ("Sorted intersection and union", test_sorted_intersection_and_union),
    ("Sorted split_th empty/single", test_sorted_split_th_empty_and_small),
    ("Sorted combine & combine_r", test_sorted_combine_and_combine_r),
    ("Sorted copy & copy_r", test_sorted_copy_and_copy_r),
]

# Run tests
passed = 0
failed = 0
print("Running tests...\n")
for name, fn in tests:
    ok = run_test(name, fn)
    if ok:
        passed += 1
    else:
        failed += 1

print("\nSummary:")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("Some tests failed. Inspect failures above.")
