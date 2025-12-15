"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-18"
-------------------------------------------------------
"""
# Imports

# test_reverse_pipeline.py
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

def pretty_stack(s: Stack) -> str:
    # Your __iter__ yields TOP -> BOTTOM
    return f"TOP -> {list(s)} -> BOTTOM"

def run_case(name, arr):
    print(f"\n=== {name} ===")
    original = list(arr)           # keep a copy to check reversal
    src = list(arr)                # this will be drained by array_to_stack
    tgt = []                       # will receive values from stack
    s = Stack()

    print(f"Input array: {original}")
    array_to_stack(s, src)
    print(f"After array_to_stack:\n  Stack:  {pretty_stack(s)}\n  Source: {src}")

    stack_to_array(s, tgt)
    print(f"After stack_to_array:\n  Stack:  {pretty_stack(s)}\n  Target: {tgt}")
    print(f"Expected reversed: {original[::-1]}")

    # Proof: target must equal reversed(original); stack & source must be empty
    assert tgt == original[::-1], "❌ target is not the reversed input"
    assert src == [], "❌ source should be empty after array_to_stack"
    assert list(s) == [], "❌ stack should be empty after stack_to_array"
    print("✅ Reversal property holds.")

def main():
    run_case("Basic odd length", [1, 2, 3])
    run_case("Two elements", [29, 21])
    run_case("Duplicates", [2, 2, 3, 2])
    run_case("Empty list", [])

if __name__ == "__main__":
    main()
