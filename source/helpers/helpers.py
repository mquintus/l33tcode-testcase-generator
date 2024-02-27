import random

def get_testcase_random() -> [int, list, list, int, int]:
    n, edges, succProb, start, end = get_testcase_uniform()
    succProb = [random.random() for i in range(len(succProb))]
    return n, edges, succProb, start, end


def get_testcase_min() -> [int, list, list, int, int]:
    n = 2
    start = 0
    end = 1
    edges = []
    succProb = []
    return n, edges, succProb, start, end


def get_testcase_uniform() -> [int, list, list, int, int]:
    n = 10 ** 4
    start = 0
    end = 10 ** 4 - 1
    edges = []
    succProb = []
    max_edge_count = 2 * n
    for i in range(max_edge_count):
        a = random.randint(start, end)
        b = a
        while b == a or [a, b] in edges or [b, a] in edges:
            b = random.randint(start, end)
        edges.append([a, b])
        succProb.append(1)
    return n, edges, succProb, start, end


def replace_grid_field(grid, x, y, char):
    grid[y] = grid[y][:x] + char + grid[y][x + 1 :]


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








