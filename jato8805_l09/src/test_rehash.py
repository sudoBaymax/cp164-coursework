"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-12"
-------------------------------------------------------
"""
# Imports

# test_hash_set.py
from Hash_Set_array import Hash_Set

obj = Hash_Set(5)

# print table contents as list-of-lists
print("Initial table:", [list(bucket) for bucket in obj._table])

bucket_values = [5, 11, 7, 12, 3, 9]
for element in bucket_values:
    obj.insert(element)

print("After inserts:", [list(bucket) for bucket in obj._table])
print("Count:", len(obj), "Capacity:", obj._capacity)

obj._rehash()

print("After rehash:", [list(bucket) for bucket in obj._table])
print("Count:", len(obj), "New capacity:", obj._capacity)
