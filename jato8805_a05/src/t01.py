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
import traceback
from Movie import Movie
from List_array import List

PASSED = 0
FAILED = 0

def ok(msg):
    print(f"  PASS: {msg}")

def fail(msg):
    print(f"  FAIL: {msg}")

def expect_eq(a, b, msg):
    global PASSED, FAILED
    if a == b:
        PASSED += 1; ok(msg)
    else:
        FAILED += 1; fail(f"{msg} | expected: {b!r}, got: {a!r}")

def expect_true(cond, msg):
    global PASSED, FAILED
    if cond:
        PASSED += 1; ok(msg)
    else:
        FAILED += 1; fail(msg)

def expect_raises(func, exc_type, msg):
    global PASSED, FAILED
    try:
        func()
    except Exception as e:
        if isinstance(e, exc_type):
            PASSED += 1; ok(msg + f" (raised {exc_type.__name__})")
        else:
            FAILED += 1; fail(msg + f" (raised {type(e).__name__} != {exc_type.__name__})")
    else:
        FAILED += 1; fail(msg + " (no exception)")

def print_header(title):
    print("\n" + "="*60)
    print(title)
    print("-"*60)

# Test groups
def test_basic_append_getitem_len():
    print_header("Basic: append, __getitem__, __len__, deepcopy semantics")
    lst = List()
    m1 = Movie("Edge", 2005, "Dir", 7.5, [0,2])
    m2 = Movie("Edge2", 2010, "Dir2", 8.1, [1])
    lst.append(m1); lst.append(m2)
    expect_eq(len(lst), 2, "len after two appends == 2")
    expect_eq(str(lst[0]).splitlines()[0], "Title:    Edge", "getitem 0 correct")
    expect_eq(str(lst[-1]).splitlines()[0], "Title:    Edge2", "getitem -1 correct")
    # mutate original and ensure stored copy doesn't change
    m1.title = "Changed"
    expect_eq(str(lst[0]).splitlines()[0], "Title:    Edge", "stored deepcopy preserved after original mutated")

def test_prepend_and_remove_front():
    print_header("Prepend and remove_front")
    lst = List()
    lst.prepend(Movie("First", 2001, None, None, None)); lst.prepend(Movie("Zero", 2000, None, None, None))
    expect_eq(len(lst), 2, "len after two prepends == 2")
    removed = lst.remove_front()
    expect_eq(str(removed).splitlines()[0], "Title:    Zero", "remove_front returned first inserted element")
    expect_eq(len(lst), 1, "len decreased after remove_front")

def test_remove_and_remove_many_and_clean():
    print_header("Remove, remove_many, clean")
    lst = List()
    a = Movie("A",2000, None, None, None); b = Movie("B",2001, None, None, None); c = Movie("A",2000, None, None, None)
    lst.append(a); lst.append(b); lst.append(c)
    # remove first "A"
    removed = lst.remove(Movie("A",2000, None, None, None))
    expect_eq(removed == a, True, "remove returns removed movie equal to original")
    expect_eq(len(lst), 2, "len after remove == 2")
    # remove_many on value not present -> no error and no change
    lst.remove_many(Movie("ZZ",1999, None, None, None))
    expect_eq(len(lst), 2, "remove_many on non-existent key leaves list unchanged")
    # add duplicates and clean
    lst.append(Movie("B",2001, None, None, None)); lst.append(Movie("A",2000, None, None, None))
    expect_eq(len(lst), 4, "len after adding duplicates == 4")
    lst.clean()
    expect_eq(len(lst), 2, "clean removed duplicates keeping first occurrence")

def test_combine_and_union_and_intersection():
    print_header("Combine, union, intersection (and source-emptying behavior)")
    s1 = List(); s2 = List(); target = List()
    for t in ["a","b","c"]:
        s1.append(Movie(t,2000, None, None, None))
    for t in ["1","2"]:
        s2.append(Movie(t,2010, None, None, None))
    target.combine(s1, s2)
    expect_eq(len(target), 5, "combine produced 5 elements")
    expect_eq(len(s1), 0, "s1 emptied after combine")
    expect_eq(len(s2), 0, "s2 emptied after combine")

    # union
    s1 = List(); s2 = List(); target = List()
    s1.append(Movie("X",2000, None, None, None)); s1.append(Movie("Y",2001, None, None, None))
    s2.append(Movie("Y",2001, None, None, None)); s2.append(Movie("Z",2002, None, None, None))
    target.union(s1, s2)
    expect_eq(len(target), 3, "union combined unique values")
    expect_eq(len(s1), 0, "s1 emptied after union")
    expect_eq(len(s2), 0, "s2 emptied after union")

    # intersection (sources unchanged)
    s1 = List(); s2 = List(); target = List()
    s1.append(Movie("A",2000, None, None, None)); s1.append(Movie("B",2001, None, None, None)); s1.append(Movie("C",2002, None, None, None))
    s2.append(Movie("B",2001, None, None, None)); s2.append(Movie("D",2003, None, None, None)); s2.append(Movie("A",2000, None, None, None))
    target.intersection(s1, s2)
    expect_eq(len(target), 2, "intersection found two common movies")
    expect_eq(len(s1), 3, "s1 unchanged after intersection")
    expect_eq(len(s2), 3, "s2 unchanged after intersection")

def test_split_variants():
    print_header("split, split_alt, split_apply, split_key")
    s = List()
    for i in range(5):
        s.append(Movie(str(i), 2000+i, None, None, None))
    t1, t2 = s.split()
    expect_eq(len(t1) + len(t2), 5, "split total preserved")
    expect_eq(len(s), 0, "original emptied after split")

    s2 = List()
    for i in range(6):
        s2.append(Movie(str(i), 2000+i, None, None, None))
    a,b = s2.split_alt()
    expect_eq(len(a) + len(b), 6, "split_alt total preserved")
    expect_eq(len(s2), 0, "original emptied after split_alt")

    s3 = List()
    for i in range(6):
        s3.append(i)
    ta, tb = s3.split_apply(lambda x: x % 2 == 0)
    expect_eq(len(ta) + len(tb), 6, "split_apply preserves total count")

    s4 = List()
    for v in [1,5,3,7,2]:
        s4.append(v)
    tless, tge = s4.split_key(4)
    expect_true(all(v < 4 for v in tless._values), "split_key less-than correct")
    expect_true(all(v >= 4 for v in tge._values), "split_key >= correct")

def test_other_operations_and_edges():
    print_header("Other operations & edge cases")
    lst = List()
    expect_true(lst.is_empty(), "empty list is_empty True")
    expect_eq(len(lst), 0, "len empty list == 0")
    # peek/pop/remove_front on empty should raise assertions
    expect_raises(lambda: lst.peek(), AssertionError, "peek on empty raises AssertionError")
    expect_raises(lambda: lst.pop(), AssertionError, "pop on empty raises AssertionError")
    expect_raises(lambda: lst.remove_front(), AssertionError, "remove_front on empty raises AssertionError")

    # fill and test reverse, max, min, apply, pop with index, setitem
    for i in range(6):
        lst.append(i)
    lst.reverse()
    expect_eq(lst[0], 5, "reverse worked (first element 5)")
    expect_eq(lst.max(), 5, "max returned 5")
    expect_eq(lst.min(), 0, "min returned 0")
    lst.apply(lambda x: x * 10)
    expect_eq(lst[0], 50, "apply transformed values")
    val = lst.pop()
    expect_eq(val, 0, "pop without args returned last value (0 after reverse+apply)")
    lst.append(999)
    val2 = lst.pop(0)
    expect_eq(val2, 50, "pop(0) returned first element")
    lst[0] = 42
    expect_eq(lst[0], 42, "setitem updated value correctly")

def run_all_tests():
    tests = [
        test_basic_append_getitem_len,
        test_prepend_and_remove_front,
        test_remove_and_remove_many_and_clean,
        test_combine_and_union_and_intersection,
        test_split_variants,
        test_other_operations_and_edges
    ]
    print("="*60)
    print("Running List ADT test suite")
    print("="*60)
    total_tests = len(tests)
    for t in tests:
        try:
            t()
        except Exception as e:
            print("Exception during test", t.__name__, ":", type(e).__name__, e)
            traceback.print_exc()
    print("\n" + "="*60)
    print(f"TOTAL PASSED: {PASSED}, TOTAL FAILED: {FAILED}")
    print("="*60)
    if FAILED == 0:
        print("ALL TESTS PASSED ✅")
    else:
        print("Some tests failed ❌")

if __name__ == '__main__':
    run_all_tests()
