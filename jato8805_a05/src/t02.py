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
from Movie import Movie
from Sorted_List_array import Sorted_List
import traceback

PASSED = 0; FAILED = 0

def ok(msg): print("  PASS:", msg)
def fail(msg): print("  FAIL:", msg)

def expect_eq(a, b, msg):
    global PASSED, FAILED
    if a == b: PASSED += 1; ok(msg)
    else: FAILED += 1; fail(f"{msg} | expected: {b!r}, got: {a!r}")

def expect_true(cond, msg):
    global PASSED, FAILED
    if cond: PASSED += 1; ok(msg)
    else: FAILED += 1; fail(msg)

def expect_raises(func, exc_type, msg):
    global PASSED, FAILED
    try:
        func()
    except Exception as e:
        if isinstance(e, exc_type): PASSED += 1; ok(msg + f" (raised {exc_type.__name__})")
        else: FAILED += 1; fail(msg + f" (raised {type(e).__name__} != {exc_type.__name__})")
    else:
        FAILED += 1; fail(msg + " (no exception)")

def print_header(title):
    print("\n" + "="*60); print(title); print("-"*60)

def test_insert_and_order_and_stability():
    print_header("insert: ordering and stability")
    s = Sorted_List()
    s.insert(5); s.insert(3); s.insert(5); s.insert(1); s.insert(3)
    expect_eq(s._values, [1,3,3,5,5], "integers sorted with duplicates preserved order of equals")
    s2 = Sorted_List()
    m1 = Movie("A",2000); m2 = Movie("A",2000); m3 = Movie("B",2001)
    s2.insert(m1); s2.insert(m2); s2.insert(m3)
    expect_eq([repr(x) for x in s2._values], [repr(m1), repr(m2), repr(m3)], "Movie stability preserved")

def test_contains_find_count_index():
    print_header("contains, find, count, index")
    s = Sorted_List()
    for v in [1,2,2,3,4,4,4]: s.insert(v)
    expect_true(2 in s, "__contains__ finds existing value")
    expect_eq(s.count(4), 3, "count returns correct number")
    expect_eq(s.index(3), 3, "index returns first occurrence index (3)")
    expect_eq(s.find(2), 2, "find returns deepcopy of value 2 (int)")
    expect_eq(s.find(99), None, "find returns None for missing value")

def test_combine_union_intersection_clean_copy():
    print_header("combine, union, intersection, clean, copy")
    a = Sorted_List(); b = Sorted_List(); tgt = Sorted_List()
    for x in [1,3,5]: a.insert(x)
    for x in [2,3,4]: b.insert(x)
    tgt.combine(a,b)
    expect_eq(tgt._values, [1,2,3,3,4,5], "combine merged sorted sequences")
    expect_eq(len(a), 0, "source a emptied after combine"); expect_eq(len(b), 0, "source b emptied after combine")

    a = Sorted_List(); b = Sorted_List(); tgt = Sorted_List()
    for x in [1,2,3]: a.insert(x)
    for x in [2,3,4]: b.insert(x)
    tgt.union(a,b)
    expect_eq(tgt._values, [1,2,3,4], "union created sorted unique list")
    expect_eq(len(a), 0, "a emptied after union"); expect_eq(len(b), 0, "b emptied after union")

    a = Sorted_List(); b = Sorted_List(); tgt = Sorted_List()
    for x in [1,2,3,4]: a.insert(x)
    for x in [2,4,6]: b.insert(x)
    tgt.intersection(a,b)
    expect_eq(tgt._values, [2,4], "intersection returns common sorted unique values")
    expect_eq(a._values, [1,2,3,4], "a unchanged after intersection"); expect_eq(b._values, [2,4,6], "b unchanged after intersection")

    s = Sorted_List(); s._values = [1,1,2,2,2,3]
    s.clean(); expect_eq(s._values, [1,2,3], "clean removed duplicates")

    s = Sorted_List(); s.insert(10); s.insert(5)
    c = s.copy(); expect_eq(c._values, s._values, "copy has same values"); expect_true(c is not s, "copy is distinct object")

def test_peek_pop_remove_front_remove_many_max_min_eq_is_empty():
    print_header("peek, pop, remove_front, remove_many, max/min, eq, is_empty edges")
    s = Sorted_List()
    expect_true(s.is_empty(), "empty is_empty True")
    expect_raises(lambda: s.peek(), AssertionError, "peek on empty raises")
    expect_raises(lambda: s.pop(), AssertionError, "pop on empty raises")
    expect_raises(lambda: s.remove_front(), AssertionError, "remove_front on empty raises")

    for v in [2,2,3,5,5,7]: s.insert(v)
    expect_eq(s.peek(), 2, "peek returns first value")
    expect_eq(s.pop(), 7, "pop returns last value")
    expect_eq(s.remove_front(), 2, "remove_front removed first value")
    s.remove_many(2)
    expect_true(2 not in s and s._values == [3,5,5], "remove_many removed all 2s")
    expect_eq(s.max(), 5, "max returns 5"); expect_eq(s.min(), 3, "min returns 3")
    a = Sorted_List(); b = Sorted_List()
    for x in [1,2,3]: a.insert(x); b.insert(1); b.insert(2); b.insert(3)
    expect_true(a == b, "__eq__ true for equal lists")

def test_split_variants_and_iterator():
    print_header("split variants and iterator")
    s = Sorted_List(); [s.insert(i) for i in range(7)]
    t1, t2 = s.split(); expect_eq(len(t1._values)+len(t2._values), 7, "split preserved total count"); expect_eq(len(s._values), 0, "source emptied after split")
    s = Sorted_List(); [s.insert(i) for i in range(6)]; a,b = s.split_alt(); expect_eq(len(a._values)+len(b._values), 6, "split_alt preserved count"); expect_eq(len(s._values), 0, "source emptied after split_alt")
    s = Sorted_List(); [s.insert(i) for i in range(8)]; ta,tb = s.split_apply(lambda x: x%2==0); expect_eq(len(ta._values)+len(tb._values), 8, "split_apply preserved count")
    s = Sorted_List(); [s.insert(i) for i in [1,5,3,7,2]]; tless,tge = s.split_key(4); expect_true(all(v<4 for v in tless._values), "split_key less-than correct"); expect_true(all(v>=4 for v in tge._values), "split_key >= correct")
    s = Sorted_List(); [s.insert(i) for i in range(5)]; seq = [v for v in s]; expect_eq(seq, s._values, "iterator yields values in order")

def run_all():
    tests = [
        test_insert_and_order_and_stability,
        test_contains_find_count_index,
        test_combine_union_intersection_clean_copy,
        test_peek_pop_remove_front_remove_many_max_min_eq_is_empty,
        test_split_variants_and_iterator
    ]
    print("="*60); print("Running Sorted_List ADT test suite"); print("="*60)
    for t in tests:
        try: t()
        except Exception as e:
            print("Exception during", t.__name__, type(e).__name__, e); traceback.print_exc()
    print("\n" + "="*60); print(f"TOTAL PASSED: {PASSED}, TOTAL FAILED: {FAILED}"); print("="*60)
    if FAILED == 0: print("ALL TESTS PASSED ✅")
    else: print("Some tests failed ❌")

if __name__ == '__main__':
    run_all()