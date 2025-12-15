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
# from Stack_array import Stack
from Queue_array import Queue
from copy import deepcopy
from Priority_Queue_array import Priority_Queue
from Stack_array import Stack

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto Stack. At finish, source is empty.
    Last value in source is at bottom of Stack,
    first value in source is on top of Stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
        
    while source:
        stack.push(source.pop())
        
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of Stack into target. At finish, Stack is empty.
    Top value of Stack is at end of target,
    bottom value of Stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []
    while not stack.is_empty():
        temp.append(stack.pop())
        
    temp.reverse()
    target.extend(temp)
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty Stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    print("== Stack test start ==")

    # 1) Empty stack checks
    print(f"Empty? {s.is_empty()}  (expected: True)")
    print("Attempting peek() on empty stack (should raise IndexError)...")
    try:
        s.peek()
    except Exception as e:
        print(f"peek() on empty raised: {type(e).__name__}: {e}")

    print("Attempting pop() on empty stack (should raise IndexError)...")
    try:
        s.pop()
    except Exception as e:
        print(f"pop() on empty raised: {type(e).__name__}: {e}")

    # 2) Push all items from source
    print("\nPushing items from source onto stack...")
    for item in source:
        s.push(item)
        print(f" push({item!r})")

    # 3) Non-empty checks
    print(f"\nEmpty? {s.is_empty()}  (expected: False)")
    try:
        top = s.peek()
        print(f"peek() -> {top!r}  (expected: last item in source)")
    except Exception as e:
        print(f"peek() raised unexpectedly: {type(e).__name__}: {e}")

    # 4) Pop everything to verify LIFO
    print("\nPopping all items (LIFO order):")
    while not s.is_empty():
        print(f" pop() -> {s.pop()!r}")

    # 5) Back to empty, re-test error paths quickly
    print(f"\nEmpty? {s.is_empty()}  (expected: True)")
    print("Re-testing peek()/pop() on empty...")
    for fn in ("peek", "pop"):
        try:
            getattr(s, fn)()
        except Exception as e:
            print(f"{fn}() on empty raised: {type(e).__name__}: {e}")

    print("== Stack test end ==\n")

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into Queue. At finish, source is empty.
    Last value in source is at rear of Queue,
    first value in source is at front of Queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # [] = queue
    # [1, 2, 3] = source
        
    for value in source:
        queue.insert(value)
    source.clear()
        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of Queue into target. At finish, queue is empty.
    Front value of Queue is at front of target,
    rear value of Queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())

def queue_test(a):
    """
    -------------------------------------------------------
    Tests Queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty Queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("== Queue test ==")
    print("Start empty?:", q.is_empty())

    # Insert everything (rear)
    for x in a:
        q.insert(x)
    print("Len after inserts:", len(q))

    # Peek (front)
    try:
        print("Front (peek):", q.peek())
    except Exception as e:
        print("peek() error:", e)

    # Remove all (FIFO)
    removed = []
    while not q.is_empty():
        removed.append(q.remove())
    print("Removed in order:", removed)

    print("End empty?:", q.is_empty())
    print()

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        pq.insert(value)
    source.clear()

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests Priority Queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty Priority Queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("== Priority_Queue test ==")
    print("Start empty?:", pq.is_empty())

    # Insert everything (priority defined by the PQ / item < operator)
    for x in a:
        pq.insert(x)
    print("Len after inserts (if __len__ defined):", getattr(pq, "__len__", lambda: "n/a")())

    # Peek highest priority
    try:
        print("Front (peek, highest priority):", pq.peek())
    except Exception as e:
        print("peek() error:", e)

    # Remove all in priority order
    removed = []
    while not pq.is_empty():
        removed.append(pq.remove())
    print("Removed in priority order:", removed)

    print("End empty?:", pq.is_empty())
    print()
    
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    # llist - List object 
        # initially empty
        # uses private helper methods 
    # source - Python List
        # contains a complete and filled python list
        # transfer the source elements to llist while using pop
        # a duplicate looking list should be represented in llist by the end while source is empty
    
    # implementation
        # iterate through python source using a while loop (while the source the source is not empty)
        # store the popped element in a variable
        # append the variable to llist
        # after the while loop have an empty return statement
    
    for item in source:
        llist.append(item)
        
    source.clear()
        
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # llist = List object (use methods)
    # target = python list (don't use methods)
    
    while not llist.is_empty():
        target.append(llist.pop(0))
        
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # Test empty list
    print(f"is_empty on empty list: {lst.is_empty()}")
    
    # Test append
    for value in source:
        lst.append(value)
    print(f"Appended {len(source)} items, length: {len(lst)}")
    
    # Test indexing
    print(f"lst[0]: {lst[0]}")
    
    # Test contains
    print(f"{source[0]} in lst: {source[0] in lst}")
    
    # Test count
    print(f"count({source[0]}): {lst.count(source[0])}")
    
    # Test max/min
    print(f"max: {lst.max()}, min: {lst.min()}")
    
    # Test remove
    removed = lst.remove(source[0])
    print(f"Removed: {removed}, length: {len(lst)}")
    
    # Test pop
    popped = lst.pop(0)
    print(f"Popped: {popped}, length: {len(lst)}")
    
    return