"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-24"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from List_linked import List

def make_movie_from_line(line):
    parts = line.strip().split("|")
    title = parts[0]
    year = int(parts[1])
    director = parts[2] if parts[2] != "" else None
    rating = float(parts[3]) if parts[3] != "" else None
    genres = [int(x) for x in parts[4].split(",") if x] if len(parts) > 4 else []
    return Movie(title, year, director, rating, genres)

# --- open and read from the actual text file ---
with open("movies.txt", "r", encoding="utf-8") as fv:
    movie_lines = [line.strip() for line in fv if line.strip()]

movies = [make_movie_from_line(line) for line in movie_lines]

lst = List()

print("append 5 movies")
for m in movies[:5]:
    lst.append(m)
print([m.key() for m in lst])

print("\nprepend one movie (Stardust)")
lst.prepend(movies[7])
print([m.key() for m in lst])

print("\ninsert Juno at index 1")
lst.insert(1, movies[8])
print([m.key() for m in lst])

print("\npeek (front):", lst.peek().key())

search_key = Movie("Zulu", 1964, None, None, None)
print("\nindex of Zulu (1964):", lst.index(search_key))
found = lst.find(search_key)
print("found Zulu (1964):", None if found is None else found.key())

removed = lst.remove(search_key)
print("\nremove Zulu (1964):", None if removed is None else removed.key())
print([m.key() for m in lst])

# Append another Zulu (1964) and Zulu (2013)
print("\nappend another Zulu (1964) and Zulu (2013)")
z1964 = next((m for m in movies if m.title == "Zulu" and m.year == 1964), None)
z2013 = next((m for m in movies if m.title == "Zulu" and m.year == 2013), None)
lst.append(z1964)
lst.append(z2013)
print([m.key() for m in lst])

# Count occurrences of Zulu (1964)
count_z1964 = lst.count(search_key)
print("\ncount of Zulu (1964):", count_z1964)

# find Zulu (2013)
search_z2013 = Movie("Zulu", 2013, None, None, None)
print("index of Zulu (2013):", lst.index(search_z2013))
found2013 = lst.find(search_z2013)
print("found Zulu (2013):", None if found2013 is None else found2013.key())

# remove_many Zulu (1964)
print("\nremove_many Zulu (1964)")
lst.remove_many(search_key)
print([m.key() for m in lst])
print("count of Zulu (1964) after remove_many:", lst.count(search_key))

# Final list length
print("\nfinal length of list:", len(lst))
