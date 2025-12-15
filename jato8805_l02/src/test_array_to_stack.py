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
# test_io_minimal.py
from Stack_array import Stack
from utilities import array_to_stack

# Make f"{stack}" readable (TOP -> BOTTOM). Remove if not needed.
def _stack_repr(self):
    return f"TOP -> {list(self)} -> BOTTOM"
Stack.__repr__ = _stack_repr
Stack.__str__  = _stack_repr

def run_case(initial_stack_vals, source_vals):
    s = Stack()
    for v in initial_stack_vals:
        s.push(v)
    src = list(source_vals)

    array_to_stack(s, src)

    # Only these two lines per case:
    print(f"Stack: {s}")
    print(f"Source: {src}")

def main():
    # 1) Basic
    run_case([], [29, 21])
    # 2) Pre-populated stack
    run_case([35], [1, 2, 3])
    # 3) Empty source
    run_case([], [])

if __name__ == "__main__":
    main()
