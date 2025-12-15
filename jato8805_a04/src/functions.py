"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports

from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source Queues into the current target Queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.insert(source1.remove())
        if not source2.is_empty():
            target.insert(source2.remove())
            
    return target

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a Priority Queue into two depending on an external
    priority key. The source Priority Queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a Priority Queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - a Priority Queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while not source.is_empty():
        value = source.remove()
        if value < key:
            target1.insert(value)
        else:
            target2.insert(value)
    
    return target1, target2