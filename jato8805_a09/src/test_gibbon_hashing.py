"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-11-22"
-------------------------------------------------------
"""
# Imports

from Hash_Set_array import Hash_Set
from Word import Word
from dns.rdataclass import NONE



def gibbon_to_word(fh):
    word_arr = []
    
    for line in fh:
        line = line.strip().split()
        
        for word in line:
            if word.isalpha():
                word_arr.append(Word(word.lower()))
        
    return word_arr
    
def hash_stats(hash_set):
    total = 0
    max_word = None  
    
    for bucket in hash_set._table:
        for word in bucket:
            total += word.comparisons
            if max_word is None or w.comparisons > max_word.comparisons:
                max_word = word 
                
    return total, max_word
        
    
    
def word_to_hash(word_array, capacity):
    hashset = Hash_Set(capacity)
    
    for word in word_array:
        hashset.insert(word)
        
    return hashset


if __name__ == "__main__":
    # --- Testing gibbon_to_word and word_to_hash ---
    
    # 1. Open a sample file
    with open("simple_test.txt", "r", encoding="utf-8") as fh:
        words = gibbon_to_word(fh)

    # 2. Print the Word objects in a clean list form
    print("WORD ARRAY (first 30 words):")
    print([w.word for w in words[:30]])
    print(f"Total words: {len(words)}")

    # 3. Insert into hash set
    hset = word_to_hash(words, 20)

    # 4. Print final hash set content neatly
    print("\nHASH SET CONTENTS:")
    for slot, bucket in enumerate(hset._table):
        # if bucket is not None and len(bucket) > 0:
        print(f"Slot {slot}: {[w.word for w in bucket]}")
    
    
    
    #
    #
    # hset = Hash_Set(20)
    #
    # # Insert words
    # with open(filename, "r", encoding="utf-8") as fv:
    #     insert_words(fv, hset)
    #
    # # Compute comparison stats
    # total_comparisons, max_word = hashset_stats(hset)
    #
    # print(f"Total comparisons: {total_comparisons:,}")
    # print(f"Word with most comparisons: '{max_word.word}' ({max_word.comparisons} comparisons)")