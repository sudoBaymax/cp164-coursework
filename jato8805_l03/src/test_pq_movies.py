"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-26"
-------------------------------------------------------
"""
# Imports
from utilities import priority_queue_test
from Movie_utilities import read_movies

def demo_with_movies(path="movies.txt"):
    with open(path, "r", encoding="utf-8") as fv:
        movies = read_movies(fv)      # list[Movie]
    priority_queue_test(movies)       # prints FIFO by priority (as defined by Movie/<)
    
if __name__ == "__main__":
    demo_with_movies()