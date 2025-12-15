"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-12"
-------------------------------------------------------
"""
# Imports

from Movie import Movie

def main():
    # make a Movie object with some genres
    m = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8])
    print(m.genres_string())  # should print: romance, comedy, zombie, horror

    m2 = Movie("Drama SciFi", 2000, "Some Director", 6.0, [2, 0])
    print(m2.genres_string())  # should print: drama, science fiction
    
if __name__ == "__main__":
    main()
    
    