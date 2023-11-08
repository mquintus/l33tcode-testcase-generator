import random

def get_unique_numbers(n, minVal):
    unique_numbers = list(range(minVal, minVal + n))
    random.shuffle(unique_numbers)
    return unique_numbers

def binary_tree_with_duplicates(n, minVal, maxVal):
    '''
    The datastructure is a list, e.g.
    [0,1,2,3,null,4,5,6,7,8]
         0
        / \
       1   2
      /    /\
     3    4  5
    /\   /
   6  7 8

    That is if a null value exists, the numbering is continued
    jumping over the non-existant places in the tree.

    This also means that the number of 'none' values can't exceed
    the number of children on the current level
   '''

    i = 1
    binary_tree = [random.randint(minVal, maxVal)]
    nodes_on_parent_level = -1
    nodes_on_current_level = 1
    places_on_current_level = 0
    while i < n:
        if places_on_current_level == 0:
            # Move on to next level
            nodes_on_parent_level = nodes_on_current_level
            nodes_on_current_level = 0
            places_on_current_level = 2 * nodes_on_parent_level

        skip_node = False
        can_skip_node = (nodes_on_current_level > 0) | (places_on_current_level > 0)
        if can_skip_node:
            skip_node = random.randint(1,4) == 1
        if skip_node:
            binary_tree.append(None)
        else:
            binary_tree.append(random.randint(minVal, maxVal))
            nodes_on_current_level += 1
            i += 1
        places_on_current_level -= 1
    return binary_tree








