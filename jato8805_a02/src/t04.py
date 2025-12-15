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
from Movie_utilities import get_by_genres

def print_movies(label, movies):
    print(label)
    if not movies:
        print("  (no matches)")
    else:
        for m in movies:
            print(f"  {m.title} ({m.year}) - genres={m.genres}")
    print(f"  Count: {len(movies)}")
    print("-" * 32)

def main():
    # Genre codes per your course:
    # 0=science fiction, 1=fantasy, 2=drama, 3=romance, 4=comedy, 6=action, ...
    movies = [
        Movie("Juno", 2007, "Jason Reitman", 7.7, [3, 4]),                # rom-com (exact [3,4])
        Movie("Broken Flowers", 2005, "Jim Jarmusch", 7.2, [3, 4]),       # rom-com (exact [3,4])
        Movie("Stardust", 2007, "Matthew Vaughn", 7.7, [1, 3]),           # fantasy+romance
        Movie("Wonder Woman", 2017, "Patty Jenkins", 7.4, [1, 6]),        # fantasy+action
        Movie("I Am Legend", 2007, "Francis Lawrence", 7.1, [0, 6]),      # sci-fi+action
        Movie("Dark City", 1998, "Alex Proyas", 7.8, [0]),                # sci-fi
    ]

    # Test 1: exact romantic comedy [3,4] → Juno, Broken Flowers (in that order)
    target = [3, 4]
    res = get_by_genres(movies, target)
    print_movies(f"get_by_genres({target})  # exact match", res)
    titles = [m.title for m in res]
    assert titles == ["Juno", "Broken Flowers"], "Expected Juno and Broken Flowers only"

    # Test 2: exact science fiction [0] → Dark City only
    target = [0]
    res = get_by_genres(movies, target)
    print_movies(f"get_by_genres({target})  # exact match", res)
    assert [m.title for m in res] == ["Dark City"]

    # Test 3: exact fantasy+romance [1,3] → Stardust only (Wonder Woman is [1,6], so exclude)
    target = [1, 3]
    res = get_by_genres(movies, target)
    print_movies(f"get_by_genres({target})  # exact match", res)
    assert [m.title for m in res] == ["Stardust"]

    # Test 4: no exact matches (e.g., [3] alone)
    target = [3]
    res = get_by_genres(movies, target)
    print_movies(f"get_by_genres({target})  # exact match", res)
    assert len(res) == 0

    print("All simple get_by_genres tests passed ✅")

if __name__ == "__main__":
    main()
