"""
-------------------------------------------------------
Movie None-handling quick test
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-30"
-------------------------------------------------------
Verifies:
- Partial-key Movies (title+year only) do not crash.
- __str__ shows "None" for missing non-key fields.
- write() emits empty fields for missing values.
- genres_string()/genres_list_string() are safe on None/[].
- Comparisons (__eq__/__lt__) depend only on (title, year).
-------------------------------------------------------
"""

from Movie import Movie
from io import StringIO

def show(t): print(f"\n{t}")

def main():
    m_full  = Movie("Inception", 2010, "Christopher Nolan", 8.8, [0, 2])
    m_key   = Movie("Inception", 2010, None, None, None)
    m_other = Movie("Interstellar", 2014, "Christopher Nolan", 8.6, [0, 2])
    m_empty = Movie("Dunkirk", 2017, "Christopher Nolan", 7.9, [])

    show("__str__ (full vs partial-key)")
    print(m_full); print(); print(m_key)

    show("genres_string / genres_list_string")
    print("None ->", repr(m_key.genres_string()), repr(m_key.genres_list_string()))
    print("[]   ->", repr(m_empty.genres_string()), repr(m_empty.genres_list_string()))

    show("write()")
    buf = StringIO(); m_key.write(buf);  print("partial-key:", buf.getvalue().strip())
    buf = StringIO(); m_full.write(buf); print("full:       ", buf.getvalue().strip())

    show("comparisons (key = title+year)")
    print("m_full == m_key:", m_full == m_key)
    print("case-insensitive:", m_key == Movie("INCEPTION", 2010, None, None, None))
    print("m_full <  m_other:", m_full < m_other)
    print("m_other < m_full:", m_other < m_full)

if __name__ == "__main__":
    main()
