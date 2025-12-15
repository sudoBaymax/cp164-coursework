"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-03"
-------------------------------------------------------
"""
# Imports
from List_array import List
import copy
from utilities import list_to_array
from utilities import array_to_list

def inspect_list(llist):
    """
    Helper to return a Python list representation for assertions.
    """
    return copy.copy(llist._values)


def run_list_to_array_test(name, initial_llist_values, initial_target, 
                            expected_llist_values, expected_target):
    """
    Runs list_to_array test with given initial conditions and expected results.
    """
    # Prepare inputs
    llist = List()
    for v in initial_llist_values:
        llist.append(v)
    
    target = list(initial_target)  # copy
    
    # Run the function
    try:
        result = list_to_array(llist, target)
        
        # Check that function returns None
        if result is not None:
            print(f"[{name}] WARNING: list_to_array should return None, got {result}")
    except Exception as e:
        print(f"[{name}] ERROR: list_to_array raised {type(e).__name__}: {e}")
        return False
    
    # Inspect results
    got_llist = inspect_list(llist)
    got_target = list(target)
    
    ok = (got_llist == expected_llist_values) and (got_target == expected_target)
    
    if ok:
        print(f"[{name}] PASS")
    else:
        print(f"[{name}] FAIL")
        print(f"    initial_llist: {initial_llist_values}")
        print(f"    initial_target: {initial_target}")
        print(f"    expected llist: {expected_llist_values}")
        print(f"    got llist:      {got_llist}")
        print(f"    expected target: {expected_target}")
        print(f"    got target:      {got_target}")
    return ok


# ============================================================
# TEST SUITE FOR list_to_array
# ============================================================

def test_list_to_array():
    """
    Comprehensive test suite for list_to_array function.
    """
    print("=" * 60)
    print("TESTING list_to_array")
    print("=" * 60)
    
    tests = []
    
    # 1) Basic: move 4 items from llist to empty target
    tests.append(("basic_move",
                  [1, 2, 3, 4],      # initial llist
                  [],                # initial target
                  [],                # expected llist (empty after move)
                  [1, 2, 3, 4]))     # expected target
    
    # 2) Empty llist -> no change to target
    tests.append(("empty_llist",
                  [],                # initial llist
                  [],                # initial target
                  [],                # expected llist
                  []))               # expected target
    
    # 3) Single element
    tests.append(("single_element",
                  [42],              # initial llist
                  [],                # initial target
                  [],                # expected llist
                  [42]))             # expected target
    
    # 4) Target is non-empty (append to existing target)
    tests.append(("target_nonempty",
                  [4, 5, 6],         # initial llist
                  [1, 2, 3],         # initial target
                  [],                # expected llist (empty)
                  [1, 2, 3, 4, 5, 6]))  # expected target
    
    # 5) Mixed types
    tests.append(("mixed_types",
                  [None, "hello", 3.14, True],
                  [],
                  [],
                  [None, "hello", 3.14, True]))
    
    # 6) Large list
    large = list(range(100))
    tests.append(("large_list",
                  large,
                  [],
                  [],
                  large.copy()))
    
    # 7) Order preservation test
    tests.append(("order_check",
                  ['a', 'b', 'c', 'd', 'e'],
                  [],
                  [],
                  ['a', 'b', 'c', 'd', 'e']))
    
    # 8) Duplicate values
    tests.append(("duplicates",
                  [1, 1, 2, 2, 3, 3],
                  [],
                  [],
                  [1, 1, 2, 2, 3, 3]))
    
    # Run all tests
    all_ok = True
    for t in tests:
        all_ok &= run_list_to_array_test(*t)
    
    print("\nSUMMARY:", "ALL PASS" if all_ok else "SOME TESTS FAILED")
    return all_ok


def test_roundtrip():
    """
    Test that array_to_list followed by list_to_array preserves data.
    """
    print("\n" + "=" * 60)
    print("TESTING ROUNDTRIP (array_to_list -> list_to_array)")
    print("=" * 60)
    
    original = [10, 20, 30, 40, 50]
    
    # Step 1: array to list
    llist = List()
    source = original.copy()
    array_to_list(llist, source)
    
    # Verify source is empty
    if source != []:
        print("[roundtrip] FAIL: source not empty after array_to_list")
        return False
    
    # Step 2: list back to array
    target = []
    list_to_array(llist, target)
    
    # Verify llist is empty
    if not llist.is_empty():
        print("[roundtrip] FAIL: llist not empty after list_to_array")
        return False
    
    # Verify data matches original
    if target == original:
        print("[roundtrip] PASS")
        return True
    else:
        print(f"[roundtrip] FAIL: expected {original}, got {target}")
        return False


def test_multiple_operations():
    """
    Test multiple back-to-back operations.
    """
    print("\n" + "=" * 60)
    print("TESTING MULTIPLE OPERATIONS")
    print("=" * 60)
    
    llist = List()
    
    # First batch
    source1 = [1, 2, 3]
    array_to_list(llist, source1)
    target1 = []
    list_to_array(llist, target1)
    
    # Second batch
    source2 = [4, 5, 6]
    array_to_list(llist, source2)
    target2 = []
    list_to_array(llist, target2)
    
    ok = (target1 == [1, 2, 3]) and (target2 == [4, 5, 6]) and llist.is_empty()
    
    if ok:
        print("[multiple_ops] PASS")
    else:
        print(f"[multiple_ops] FAIL")
        print(f"    target1: {target1} (expected [1,2,3])")
        print(f"    target2: {target2} (expected [4,5,6])")
        print(f"    llist.is_empty(): {llist.is_empty()} (expected True)")
    
    return ok


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Run all test suites.
    """
    print("\n" + "=" * 60)
    print("LIST UTILITY FUNCTIONS - COMPREHENSIVE TEST SUITE")
    print("=" * 60 + "\n")
    
    all_ok = True
    
    # Run test suites
    all_ok &= test_list_to_array()
    all_ok &= test_roundtrip()
    all_ok &= test_multiple_operations()
    
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY:", "✓ ALL TESTS PASSED" if all_ok else "✗ SOME TESTS FAILED")
    print("=" * 60)


if __name__ == "__main__":
    main()