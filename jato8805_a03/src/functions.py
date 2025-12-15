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
from Stack_array import Stack
from utilities import array_to_stack

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source Stack into separate target Stacks.
    When finished source Stack is empty. Values are
    pushed alternately onto the returned target Stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    t1, t2 = Stack(), Stack()
    buf = Stack()

    # move all to buf (empties source)
    while not source.is_empty():
        buf.push(source.pop())

    # deal out in original order from buf
    i = 0
    while not buf.is_empty():
        if i % 2 == 0:
            t1.push(buf.pop())
        else:
            t2.push(buf.pop())
        i += 1
    return t1, t2
    
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    stack_list = []
    
    while not source.is_empty():
        value = source.pop()
        stack_list.insert(0,value)
    
    array_to_stack(source, stack_list)
    
    return 


# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    s = Stack()
    
    for x in string:
        
        if x == "+":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)+float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "-":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)-float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "*":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)*float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "/":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)/float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == " ":
            pass
            
        else:
            s.push(x)
    
    answer = s.pop()
    
    return answer


def stack_maze(maze):
    """
    Solves a maze using depth-first search with a single Stack.
    Returns the path (without 'Start', with 'X') or None if no exit.
    """
    # Guard: must have a Start
    if 'Start' not in maze:
        return None

    stack = Stack()            # stack of frames: (node, next_child_index)
    stack.push(('Start', 0))
    onpath = {'Start'}         # nodes currently on the DFS path to avoid cycles

    while not stack.is_empty():
        node, idx = stack.peek()

        # Found exit
        if node == 'X':
            # Build path from the stack: X back to Start
            path = []
            while not stack.is_empty():
                n, _ = stack.pop()
                path.append(n)
            path.reverse()         # Start ... X
            return path[1:]        # drop 'Start', keep 'X'

        # Explore neighbors of current node
        children = maze.get(node, [])

        if idx >= len(children):
            # No more children: backtrack
            stack.pop()
            onpath.discard(node)
            continue

        # Advance the top frame's child index
        stack.pop()
        stack.push((node, idx + 1))
        nxt = children[idx]

        if nxt == 'X':
            stack.push(('X', 0))
            continue

        # Skip cycles (don’t revisit a node already on the current path)
        if nxt in onpath:
            continue

        stack.push((nxt, 0))
        onpath.add(nxt)

    # Explored everything, no exit
    return None



def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values according to opstring using one Stack.
    'S' -> push next input onto stack
    'X' -> pop from stack to output
    Returns None if the sequence can't be carried out or
    if not all cars end up in the output.
    -------------------------------------------------------
    """
    stk = Stack()
    out = []
    i = 0                   # next index in values_in
    n = len(values_in)

    for ch in opstring:
        if ch == 'S':
            if i >= n:          # no more cars to push
                return None
            stk.push(values_in[i])
            i += 1
        elif ch == 'X':
            if stk.is_empty():  # nothing to pop
                return None
            out.append(stk.pop())
        else:
            return None         # illegal character

    # valid iff: all inputs consumed, stack empty, all cars output
    if i != n:
        return None
    if not stk.is_empty():
        return None
    if len(out) != n:
        return None

    return out


# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        "cannot use '{}' as the mirror character".format(m)
        
    mirror = True
    stack = Stack()
    n = len(string)
    i = 0
    
    while mirror and i < n and string[i] != m:
        
        if not string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = False
            
    if mirror:
        
        i += 1
        
        while mirror and i > n and not stack.is_empty():
            c = stack.pop()
            
            if string[i] != c:
                mirror = False
            else:
                i += 1
                
        if not (stack.is_empty() and i == n):
            mirror = False
        
    return mirror