"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-09-27"
-------------------------------------------------------
"""
# Imports
from functions import reroute

# 1) Example from the handout
print(reroute("SSXSSXXX", [1,2,3,4]))  # -> [2, 4, 3, 1]

# 2) Invalid: pop before any push
print(reroute("XSSX", [1,2]))          # -> None

# 3) Invalid: leaves cars unprocessed (not enough S)
print(reroute("SSXX", [1,2,3]))        # -> None

# 4) Valid: empty input / no ops
print(reroute("", []))                 # -> []
