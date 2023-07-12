"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import random
import sys
import time
import itertools

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
    if int(challenge_id) not in [
        1514, 
        864, 
        1970, 
        2305,
        1601,
        137,
        1493,
        209,
        3,
        2272,
        111,
        2551,
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

            
    if int(challenge_id) == 137:
        def numrandom(i):
            num = random.randint(-10000,10000)
            num *= 10000
            num += i
            return num

        tests = []
        for test in range(8):
            n = 9999
            nums = []
            num = 0
            for i in range(n):
                num = numrandom(i)
                nums.append(num)
                nums.append(num)
                nums.append(num)
            i += 1
            num = numrandom(i)
            nums.append(num)
            random.shuffle(nums)
            tests.append(nums.__str__())
        tests = '\n'.join(tests)

    if int(challenge_id) == 1493:
        nums = [0 for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [1 for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [random.randint(0,1) for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [random.randint(0,1) for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [random.randint(0,1) for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [random.randint(0,1) for i in range(10**5)]
        tests.append(nums.__str__())
        nums = [1]
        tests.append(nums.__str__())
        nums = [0]
        tests.append(nums.__str__())
        nums = [1,1]
        tests.append(nums.__str__())
        nums = [0,0]
        tests.append(nums.__str__())
        nums = [0,1]
        tests.append(nums.__str__())
        nums = [1,0]
        tests.append(nums.__str__())

        tests = '\n'.join(tests)
    
    if int(challenge_id) == 209:
        tests = [
            "10000, \n[1337]",
            "10, \n[1337]"
        ]
        
        for i in range(6):
            target = random.randint(1, 10**9)
            nums = [random.randint(1, 10**4) for i in range(10**5)]
            tests.append(target.__str__() + "\n" + nums.__str__())
        tests = '\n'.join(tests)

    if int(challenge_id) == 3:
        letters = """qwertyuiopsdfghjklzxcvbnm,.1234567890-=+_"""
        tests = [ " ", "", "0", '1', '4', '10', '*', '-' ]
        x = ["1", "2", "3"]
        tests.append("".join(["A" for i in range(5*10**4)]))
        tests.append("".join(["A" for i in range(5*10**4-1)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5*10**4-2)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5*10**4-2)]))
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=3)])
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=4)])
        for i in range(8):
            test = "".join([letters[random.randint(0,len(letters)-1)] for i in range(5*10**4)])
            tests.append(test)
        tests = "\n".join(['"' + test + '"' for test in tests])

    if int(challenge_id) == 2272:
        letters = 'abc'
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        letters = 'zyqwertyuiopasdfghjklzxcvbnmabc'
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10**4)]
        tests.append('"' + "".join(test) + '"')
        tests = "\n".join(tests)

    if int(challenge_id) == 111:
        trees = ["[]", "[1]"]
        tree = [1]
        tree.extend([1 for i in range(10**5 - 1)])
        trees.append(tree.__str__())

        vals = [1, None]
        tree = [1]
        tree.extend([None for i in range(10**5 - 1)])
        for i in range(150):
            if 2**i + 1 < len(tree):
                tree[2**i] = 1
                #tree[i**2-1] = 1
            else:
                break
            #print(i, i**2, tree[i**2])
                    
        trees.append(tree.__str__())
        tests = "\n".join(trees)

    if int(challenge_id) == 2551:
        tests = []
        for n in range(8):
            weights = [random.randint(1, 10**9) for i in range(10**5)]
            k = random.randint(1, len(weights))
            test = weights.__str__() + "\n" + k.__str__()
            tests.append(test)
        tests = "\n".join(tests)

    date = time.time()
    write_file(f"testcase_{challenge_id}_{int(date)}.txt", tests)
