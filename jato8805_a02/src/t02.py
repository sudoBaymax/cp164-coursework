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

"""
Quick manual test for get_by_rating using one main().
Adjust imports to match your project structure.
"""
from Movie import Movie
from Movie_utilities import get_by_rating

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
        Movie("Juno", 2007, "Jason Reitman", 7.7, [2, 4]),
        Movie("Stardust", 2007, "Matthew Vaughn", 7.7, [1, 3]),
        Movie("Alphaville", 1965, "Jean-Luc Godard", 7.1, [0]),
        Movie("Zulu", 1964, "Cy Endfield", 7.8, [2]),
        Movie("Dark City", 1998, "Alex Proyas", 7.8, [0]),
        Movie("I Am Legend", 2007, "Francis Lawrence", 7.1, [0, 6]),
    ]

    # Test 1: threshold that should include multiple (>= 7.7)
    thr = 7.7
    res = get_by_rating(movies, thr)
    print_movies(f"get_by_rating(rating >= {thr})", res)
    # Assert: every result >= thr, and expected count is 4 (7.7, 7.7, 7.8, 7.8)
    assert all(m.rating >= thr for m in res), "Found a movie below the threshold"
    assert len(res) == 4, "Expected 4 movies with rating >= 7.7"

    # Test 2: threshold equal to an existing rating (== 7.1 should still include >= 7.1)
    thr = 7.1
    res = get_by_rating(movies, thr)
    print_movies(f"get_by_rating(rating >= {thr})", res)
    # Expect all except none below 7.1 → 6 movies here
    assert all(m.rating >= thr for m in res)
    assert len(res) == 6

    # Test 3: high threshold (>= 8.5) → likely no matches
    thr = 8.5
    res = get_by_rating(movies, thr)
    print_movies(f"get_by_rating(rating >= {thr})", res)
    assert len(res) == 0

    print("All simple get_by_rating tests passed ✅")

if __name__ == "__main__":
    main()
