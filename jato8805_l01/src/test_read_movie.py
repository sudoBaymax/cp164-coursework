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
from Movie_utilities import read_movie

def main():
    movie_one = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8]) # should print 3,4,5,8

if __name__ == "__main__":
    # Manual interactive test
    result = read_movie("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
    print(result)