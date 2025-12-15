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

def main():
    source1 = Queue()
    source2 = Queue()
    
    for value in [5, 8, 12, 8]:
        source1.insert(value)
    
    for value in [7, 9, 14]:
        source2.insert(value)
        
    target = Queue()
    
    target.combine(source1, source2)
    
    print(target._values)   
    
    # Confirm sources emptied
    print("source1:", source1._values)   
    print("source2:", source2._values)  


if __name__ == "__main__":
    main()