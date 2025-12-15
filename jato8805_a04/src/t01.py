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
from functions import queue_combine
from Queue_array import Queue

def main():
    # Initialize queues
    source1 = Queue()
    source2 = Queue()
    
    # Insert values into source1
    for value in [5, 8, 12, 8]:
        source1.insert(value)
    
    # Insert values into source2
    for value in [7, 9, 14]:
        source2.insert(value)
    
    print(queue_combine(source1, source2)._values)
    
if __name__ == "__main__":
    main()