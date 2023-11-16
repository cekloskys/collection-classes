from node.node import *
from stack.stack import *

def serialsearch (a: stack, first: int, size: int, target):
    """Searches for a target value in a stack of nodes
    starting at first.

    Args:
        a (stack): the stack to search
        first (int): the stack position at which the search will start
        size (int): the number of nodes to search
        target: the target value to search for

    Returns:
        int: If target appears in the stack, position of the node 
        that contains target; else -1.
    """
    # set an int counter variable i to 0
    i = 0

    # set a boolean variable found to false
    # will be set to true if the target is found
    found = False

    # while there are more elements to search
    # and the target hasn't been found
    # and i plus first doesn't exceed the length
    # of the stack
    while ((i < size) and (i + first <= a.size()) and not found):
        # if the current element is the target
        # if (a[i + first] == target):
        if (node.listPosition(a.getHead(), i + first).getData() == target):
            # set found to true
            found = True
        else:
            # increment counter variable i by 1
            i = i + 1
    # check if the target was found
    if (found):
        # return index of target
        return i + first
    else:
        # return negative 1
        return -1