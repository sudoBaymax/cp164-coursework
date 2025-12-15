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
from Movie_utilities import get_by_genre

def print_movies(label, movies):
    print(label)
    if not movies:
        print("  (no matches)")
    else:
        for m in movies:
            print(f"  {m.title} ({m.year}) - {m.director} [{m.rating}]  genres={m.genres}")
    print(f"  Count: {len(movies)}")
    print("-" * 32)

def main():
    # Genre codes from your class:
    # 0=science fiction, 1=fantasy, 2=drama, 3=romance, 4=comedy, 6=action, ...
    movies = [
        Movie("Stardust", 2007, "Matthew Vaughn", 7.7, [1, 3]),        # fantasy, romance
        Movie("Jason and the Argonauts", 1963, "Don Chaffey", 7.3, [1, 7]),  # fantasy, historical
        Movie("Wonder Woman", 2017, "Patty Jenkins", 7.4, [1, 6]),     # fantasy, action
        Movie("Juno", 2007, "Jason Reitman", 7.7, [2, 4]),             # drama, comedy
        Movie("Alphaville", 1965, "Jean-Luc Godard", 7.1, [0]),        # science fiction
    ]

    # Test fantasy (1): should return the 3 fantasy movies above.
    g = 1
    res = get_by_genre(movies, g)
    print_movies(f"get_by_genre(genre={g} -> 'fantasy')", res)
    titles = [m.title for m in res]
    assert titles == ["Stardust", "Jason and the Argonauts", "Wonder Woman"], "Order or selection incorrect"
    assert all(g in m.genres for m in res), "A returned movie doesn't include the requested genre"

    # Another quick check: a genre with no matches, e.g., 9='war' in your GENRES list
    g = 9
    res = get_by_genre(movies, g)
    print_movies(f"get_by_genre(genre={g} -> 'war')", res)
    assert len(res) == 0

    print("All simple get_by_genre tests passed ✅")

if __name__ == "__main__":
    main()