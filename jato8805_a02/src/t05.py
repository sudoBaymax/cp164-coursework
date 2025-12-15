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
from Movie_utilities import genre_counts

def main():
    # Genre legend (from your course):
    # 0 sci-fi, 1 fantasy, 2 drama, 3 romance, 4 comedy, 5 zombie,
    # 6 action, 7 historical, 8 horror, 9 war, 10 mystery
    movies = [
        Movie("Juno", 2007, "Jason Reitman", 7.7, [2, 4]),          # drama, comedy
        Movie("Stardust", 2007, "Matthew Vaughn", 7.7, [1, 3]),     # fantasy, romance
        Movie("Alphaville", 1965, "Jean-Luc Godard", 7.1, [0]),     # sci-fi
        Movie("Zulu", 1964, "Cy Endfield", 7.8, [2]),               # drama
        Movie("Dark City", 1998, "Alex Proyas", 7.8, [0]),          # sci-fi
        Movie("I Am Legend", 2007, "Francis Lawrence", 7.1, [0, 6]) # sci-fi, action
    ]

    counts = genre_counts(movies)

    # Pretty print the counts aligned with Movie.GENRES
    print("Genre counts:")
    for i, name in enumerate(Movie.GENRES):
        print(f"{i:>2} {name:<16}: {counts[i]}")
    print("Counts list:", counts)

    # Expected from the dataset above:
    # sci-fi=3, fantasy=1, drama=2, romance=1, comedy=1,
    # zombie=0, action=1, historical=0, horror=0, war=0, mystery=0
    expected = [3, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0]
    assert counts == expected, f"Expected {expected}, got {counts}"

    print("genre_counts simple test passed ✅")

if __name__ == "__main__":
    main()
