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
from utilities import array_to_list
import copy

def inspect_list(llist):
    """
    Helper to return a Python list representation for assertions.
    Uses the internal _values attribute which your List_array implementation
    seems to include. If your List API provides a different accessor,
    replace this function accordingly.
    """
    return copy.copy(llist._values)

def run_test(name, source, initial_llist_values, expected_llist_values, expected_source):
    """
    Runs array_to_list on a copy of source and a List prefilled with
    initial_llist_values. Compares final results to expected values.
    """
    # Prepare inputs
    llist = List()
    # Prefill llist if initial values provided
    for v in initial_llist_values:
        llist.append(v)
    
    src = list(source)  # copy so caller's lists are not mutated
    
    # Run the function (do not print its return)
    try:
        array_to_list(llist, src)
    except Exception as e:
        print(f"[{name}] ERROR: array_to_list raised {type(e).__name__}: {e}")
        return False
    
    # Inspect results
    got_llist = inspect_list(llist)
    got_source = list(src)
    
    ok = (got_llist == expected_llist_values) and (got_source == expected_source)
    
    if ok:
        print(f"[{name}] PASS")
    else:
        print(f"[{name}] FAIL")
        print(f"    initial_llist: {initial_llist_values}")
        print(f"    initial_source: {source}")
        print(f"    expected llist: {expected_llist_values}")
        print(f"    got llist:      {got_llist}")
        print(f"    expected source: {expected_source}")
        print(f"    got source:      {got_source}")
    return ok
    

def twice_call_test():
    """
    Test calling array_to_list twice on the same list.
    """
    name = "call_twice"
    l = List()
    src = [7, 8, 9]
    for x in []:  # keep initial llist empty
        l.append(x)
    try:
        array_to_list(l, src)
        # After first call
        mid_llist = inspect_list(l).copy()
        mid_src = list(src)
        # Second call
        array_to_list(l, src)
        final_llist = inspect_list(l)
        final_src = list(src)
    except Exception as e:
        print(f"[{name}] ERROR: raised {type(e).__name__}: {e}")
        return False

    ok = (mid_llist == [7,8,9]) and (mid_src == []) and (final_llist == [7,8,9]) and (final_src == [])
    if ok:
        print(f"[{name}] PASS")
    else:
        print(f"[{name}] FAIL")
        print(f"    mid_llist: {mid_llist}, mid_src: {mid_src}")
        print(f"    final_llist: {final_llist}, final_src: {final_src}")
    return ok


def main():
    tests = []
    
    # 1) Basic: move 4 items into empty list
    tests.append(("basic_move",
                  [1, 2, 3, 4],
                  [],                # initial llist
                  [1, 2, 3, 4],      # expected llist
                  []))               # expected source
    
    # 2) Empty source -> no change
    tests.append(("empty_source",
                  [],
                  [],                # initial llist
                  [],                # expected llist (unchanged)
                  []))
    
    # 3) Single-element source
    tests.append(("single_element",
                  [42],
                  [],                # initial llist
                  [42],
                  []))
    
    # 4) llist is non-empty already (preserve previous items, append at end)
    tests.append(("llist_nonempty",
                  [5, 6],
                  [1, 2, 3],         # initial llist
                  [1, 2, 3, 5, 6],
                  []))
    
    # 5) source contains different types
    tests.append(("mixed_types",
                  [None, "a", 3.14],
                  [],
                  [None, "a", 3.14],
                  []))
    
    # 6) large list sanity check (just length and order)
    large = list(range(1000))
    expected_large = large.copy()
    tests.append(("large_list",
                  large,
                  [],
                  expected_large,
                  []))

    # Run table-driven tests
    all_ok = True
    for t in tests:
        all_ok &= run_test(*t)
    
    # Run the twice-call test
    all_ok &= twice_call_test()
    
    print("\nSUMMARY:", "ALL PASS" if all_ok else "SOME TESTS FAILED")
    
if __name__ == "__main__":
    main()