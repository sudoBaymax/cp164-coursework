"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
__updated__ = "2025-10-06"
-------------------------------------------------------
"""
# Imports

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    if x<0 or y<0:
        ans = x - y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)
    
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if m%n == 0:
        ans = n
    else:
        ans = gcd(n, m%n)
    
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    
    # can't call a dynamic count variable because when the recursive case is reached it will reset the variable
    # iteration works by going throughht the string, we need something to traverse with recursion
    
    vowels = "aeiou"
    count = 0
    
    if s == "":
        count = 0
    elif s[0].lower() in vowels:
        count = 1 + vowel_count(s[1:])
    else:
        count = vowel_count(s[1:])
        
    return count
    
def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    # 2^3 = 2*2*2
    # base case: 0^0 = 1 
    # n^1 = n
    # recursive case: to_power(base, power) = to_power(base, power-1)
    if power == 0:
        ans = 1.0
    elif power < 0:
        if base == 0:
            raise ZeroDivisionError("0.0 cannot be raised to a negative power")
        ans = 1.0 / to_power(base, -power)
    else:
        ans = base * to_power(base, power - 1)
    return ans

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(s) <= 1:
        palindrome = True
    else:
        # Ignore non-letters from the start
        if not s[0].isalpha():
            palindrome = is_palindrome(s[1:])
        # Ignore non-letters from the end
        elif not s[-1].isalpha():
            palindrome = is_palindrome(s[:-1])
        # Compare first and last letters (case-insensitive)
        elif s[0].lower() != s[-1].lower():
            palindrome = False
        else:
            palindrome = is_palindrome(s[1:-1])
    return palindrome

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    if len(bag) == 0:
        new_set = []
    else:
        head = bag[0]
        # remove all future occurrences of head from the tail (doesn't change bag)
        tail = [x for x in bag[1:] if x != head]
        rest = bag_to_set(tail)
        new_set = [head] + rest
    return new_set

print(to_power(2, 2))
to_power(3, 1)
to_power(1, 0)
to_power(10, 2)

        
        