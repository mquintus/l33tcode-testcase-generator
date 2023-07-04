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
    if int(challenge_id) not in [1514, 864, 1970, 2305]:
    if int(challenge_id) not in [
        1514, 
        864, 
        1970, 
        2305,
        1601,
        ]:
        print("Required argument challenge_id: must be a value of [1514, 864, 1970, 2305]")
        return -1
        
    tests = []
    if int(challenge_id) == 2305:
        tests = ''
        for k in [7, *range(2, 9)]:
            cookies = [random.randint(1, 100000) for i in range(8)]
            tests += "\n".join([kwa.__str__() for kwa in [cookies, k]]) + "\n"
            

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
        tests = test  + "\n" + test2
    
    
    if int(challenge_id) == 1970:
        row = 100
        col = 200
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y+1,x+1])
        random.shuffle(cells)
        tests = "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 10000
        col = 2
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y+1,x+1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y+1,x+1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y+1,x+1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row - 1 , -1, -1):
                cells.append([y+1,x+1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 3
        col = 6666
        cells = []
        for x in range(col):
            for y in range(row - 1 , -1, -1):
                cells.append([y+1,x+1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row - 1 , -1, -1):
                cells.append([y+1,x+1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    
    if int(challenge_id) == 1601:
        tests = ""
        for test in range(8):
            building = 20
            request_count = 16
            requests = []
            for i in range(request_count):
                requests.append([random.randint(0,building-1),random.randint(0,building-1)])
            tests += "\n" + "\n".join([building.__str__(), requests.__str__()])
            
        building = 20
        requests = [[0,1],[1,2],[2,3],[3,0],[0,1],[1,2],[2,3],[3,0],[3,4],[4,3],[3,4],[4,3],[3,4],[4,3]]
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])
        
        building = 4
        for orig in range(0,4):
            for dest in range(0,4):
                requests.append(orig, dest)
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

            

    date = time.time()
    write_file(f"testcase_{challenge_id}_{int(date)}.txt", tests)
