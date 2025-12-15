"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-20"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import get_by_year

def print_movies(label, movies):
    print(label)
    if not movies:
        print("  (no matches)")
    else:
        for m in movies:
            print(f"  {m.title} ({m.year}) - {m.director} [{m.rating}]")
    print(f"  Count: {len(movies)}")
    print("-" * 32)

def main():
    # Sample dataset
    movies = [
        Movie("Juno", 2007, "Jason Reitman", 7.7, [2, 4]),        # drama, comedy
        Movie("Stardust", 2007, "Matthew Vaughn", 7.7, [1, 3]),   # fantasy, romance
        Movie("Alphaville", 1965, "Jean-Luc Godard", 7.1, [0]),   # science fiction
        Movie("Zulu", 1964, "Cy Endfield", 7.8, [2]),             # drama
    ]
    original_ids = [id(m) for m in movies]  # to verify no mutation

    # Test 1: year with multiple matches
    y = 2007
    result = get_by_year(movies, y)
    print_movies(f"get_by_year(year={y})", result)
    assert len(result) == 2 and all(m.year == y for m in result)
    # order preserved
    assert [m.title for m in result] == ["Juno", "Stardust"]

    # Test 2: year with one match
    y = 1965
    result = get_by_year(movies, y)
    print_movies(f"get_by_year(year={y})", result)
    assert len(result) == 1 and result[0].title == "Alphaville"

    # Test 3: year with no matches
    y = 1999
    result = get_by_year(movies, y)
    print_movies(f"get_by_year(year={y})", result)
    assert len(result) == 0

    # Sanity: original list unchanged (same objects, same length)
    assert len(movies) == 4 and [id(m) for m in movies] == original_ids

    print("All simple get_by_year tests passed ✅")

if __name__ == "__main__":
    main()
