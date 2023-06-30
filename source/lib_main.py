"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import random
import sys
import time

def write_file(filename: str, string: str):
    """A simple wrapper to write a string to a file.

    Does not allow override of an existing file.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        None
    """
    f = open(filename, "x")
    f.write(string)
    f.close()


def write_testcase(tests):
    """Convert test cases into strings, add line breaks    and write out.
    """
    write_file(tests)


"""Generate testcases for 1514_Path_with_Maximum_Probability.py
"""
def get_testcase_random() -> [int, list, list, int, int]:
    n,edges,succProb,start,end = get_testcase_uniform()
    succProb = [random.random() for i in range(len(succProb))]
    return n,edges,succProb,start,end

def get_testcase_min() -> [int, list, list, int, int]:
    n = 2
    start = 0
    end = 1
    edges = []
    succProb = []
    return n,edges,succProb,start,end

def get_testcase_uniform() -> [int, list, list, int, int]:
    n = 10**4
    start = 0
    end = 10**4 - 1
    edges = []
    succProb = []
    max_edge_count = 2*n
    for i in range(max_edge_count):
        a = random.randint(start,end)
        b = a
        while b == a or [a,b] in edges or [b,a] in edges:
            b = random.randint(start,end)
        edges.append([a, b])
        succProb.append(1)
    return n,edges,succProb,start,end

def replace_grid_field(grid, x, y, char):
    grid[y] = grid[y][:x] + char + grid[y][x + 1:]
            
def main(challenge_id=-1):
    if int(challenge_id) not in [1514, 864]:
        print("Required argument challenge_id: must be a value of [1514, 864]")
        return -1
        
    tests = []
    if int(challenge_id) == 1514:       
        tests.extend([
            get_testcase_random(),
            get_testcase_random(),
            get_testcase_random(),

            get_testcase_uniform(),
            get_testcase_uniform(),

            get_testcase_empty()
        ])
        tests = "\n".join([kwa.__str__() for kwa in tests])
    if int(challenge_id) == 864:
        grid = ["".join(['.' for i in range(30)]) for j in range(30)]
        
        replace_grid_field(grid, 0, 0, '@')
        replace_grid_field(grid, 29, 29, 'b')
        replace_grid_field(grid, 20, 1, 'a')
        replace_grid_field(grid, 20, 2, '#')
        replace_grid_field(grid, 21, 0, '#')
        replace_grid_field(grid, 21, 1, 'B')
        replace_grid_field(grid, 21, 2, '#')
        replace_grid_field(grid, 15, 15, 'A')
        replace_grid_field(grid, 14, 16, '#')
        replace_grid_field(grid, 13, 17, '#')
        
        test = '["' + '","'.join([row.__str__() for row in grid]) + '"]'
        
        test2 = '["@......#.............#........",".......#######......dB........","#####..#.....#......##........",".......#...#.#..........#.....","...........#.#..........#.....","....########............#.a...","............f...........#.....","######.#E#######D########C####",".......#e...F...........#.....",".......######..........##.....",".......#..............#.......",".......#.......b....##........",".......#...........#..........",".......#.........##...........",".......#........#.............",".......#.......A..............",".......#......#...............",".......#######................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................",".............................c"]'
        test3 = '["@......#.............#........",".......#######......dB........","#####..#.....#......##........",".......#...#.#..........#.....","...........#.#..........#.....","....########............#.a...","............f...........#.....","######.#E#######D########C####",".......#e...F...........#.....",".......######..........##.....",".......#..............#.......",".......#.......b....##........",".......#...........#..........",".......#.........##...........",".......#........#.............",".......#.......A..............",".......#......#...............",".......#######................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................",".............................c"]'
        tests = "\n".join([test,test2,test3])
        
    date = time.time()
    write_file(f"testcase_{challenge_id}_{int(date)}.txt", tests)
