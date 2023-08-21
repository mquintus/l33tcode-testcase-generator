"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import random
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


def main(challenge_id=-1):
    implemented_challenges = [
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
        863,
        802,
        207,
        1218,
        1751,
        735,
        673,
        1870,
        712,
        139,
        33,
        63,
        2369,
        239,
        1615,
        1489,
        1203,
    ]
    if int(challenge_id) not in implemented_challenges:
        print(
            "Required argument challenge_id: must be a value of "
            + implemented_challenges.__str__()
        )
        return -1

    tests = []
    if int(challenge_id) == 2305:
        tests = ""
        for k in [7, *range(2, 9)]:
            cookies = [random.randint(1, 100000) for i in range(8)]
            tests += "\n".join([kwa.__str__() for kwa in [cookies, k]]) + "\n"

    if int(challenge_id) == 1514:
        tests.extend(
            [
                get_testcase_random(),
                get_testcase_random(),
                get_testcase_random(),
                #
                get_testcase_uniform(),
                get_testcase_uniform(),
            ]
        )
        tests = "\n".join([kwa.__str__() for kwa in tests])

    if int(challenge_id) == 864:
        grid = ["".join(["." for i in range(30)]) for j in range(30)]

        replace_grid_field(grid, 0, 0, "@")
        replace_grid_field(grid, 29, 29, "b")
        replace_grid_field(grid, 20, 1, "a")
        replace_grid_field(grid, 20, 2, "#")
        replace_grid_field(grid, 21, 0, "#")
        replace_grid_field(grid, 21, 1, "B")
        replace_grid_field(grid, 21, 2, "#")
        replace_grid_field(grid, 15, 15, "A")
        replace_grid_field(grid, 14, 16, "#")
        replace_grid_field(grid, 13, 17, "#")

        test = '["' + '","'.join([row.__str__() for row in grid]) + '"]'

        test2 = '["@......#.............#........",".......#######......dB........","#####..#.....#......##........",".......#...#.#..........#.....","...........#.#..........#.....","....########............#.a...","............f...........#.....","######.#E#######D########C####",".......#e...F...........#.....",".......######..........##.....",".......#..............#.......",".......#.......b....##........",".......#...........#..........",".......#.........##...........",".......#........#.............",".......#.......A..............",".......#......#...............",".......#######................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................",".............................c"]'
        tests = test + "\n" + test2

    if int(challenge_id) == 1970:
        row = 100
        col = 200
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests = "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 10000
        col = 2
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 3
        col = 6666
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    if int(challenge_id) == 1601:
        tests = ""
        for test in range(8):
            building = 20
            request_count = 16
            requests = []
            for i in range(request_count):
                requests.append(
                    [random.randint(0, building - 1), random.randint(0, building - 1)]
                )
            tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

        building = 20
        requests = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [3, 4],
            [4, 3],
            [3, 4],
            [4, 3],
            [3, 4],
            [4, 3],
        ]
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

        building = 4
        for orig in range(0, 4):
            for dest in range(0, 4):
                requests.append(orig, dest)
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

    if int(challenge_id) == 137:

        def numrandom(i):
            num = random.randint(-10000, 10000)
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
        tests = "\n".join(tests)

    if int(challenge_id) == 1493:
        nums = [0 for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [1 for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [1]
        tests.append(nums.__str__())
        nums = [0]
        tests.append(nums.__str__())
        nums = [1, 1]
        tests.append(nums.__str__())
        nums = [0, 0]
        tests.append(nums.__str__())
        nums = [0, 1]
        tests.append(nums.__str__())
        nums = [1, 0]
        tests.append(nums.__str__())

        tests = "\n".join(tests)

    if int(challenge_id) == 209:
        tests = ["10000, \n[1337]", "10, \n[1337]"]

        for i in range(6):
            target = random.randint(1, 10 ** 9)
            nums = [random.randint(1, 10 ** 4) for i in range(10 ** 5)]
            tests.append(target.__str__() + "\n" + nums.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 3:
        letters = """qwertyuiopsdfghjklzxcvbnm,.1234567890-=+_"""
        tests = [" ", "", "0", "1", "4", "10", "*", "-"]
        x = ["1", "2", "3"]
        tests.append("".join(["A" for i in range(5 * 10 ** 4)]))
        tests.append("".join(["A" for i in range(5 * 10 ** 4 - 1)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]))
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=3)])
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=4)])
        for i in range(8):
            test = "".join(
                [
                    letters[random.randint(0, len(letters) - 1)]
                    for i in range(5 * 10 ** 4)
                ]
            )
            tests.append(test)
        tests = "\n".join(['"' + test + '"' for test in tests])

    if int(challenge_id) == 2272:
        letters = "abc"
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        letters = "zyqwertyuiopasdfghjklzxcvbnmabc"
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        tests = "\n".join(tests)

    if int(challenge_id) == 111:
        trees = ["[]", "[1]"]
        tree = [1]
        tree.extend([1 for i in range(10 ** 5 - 1)])
        trees.append(tree.__str__())

        vals = [1, None]
        tree = [1]
        tree.extend([None for i in range(10 ** 5 - 1)])
        for i in range(150):
            if 2 ** i + 1 < len(tree):
                tree[2 ** i] = 1
                # tree[i**2-1] = 1
            else:
                break
            # print(i, i**2, tree[i**2])

        trees.append(tree.__str__())
        tests = "\n".join(trees)

    if int(challenge_id) == 2551:
        tests = []
        for n in range(8):
            weights = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
            k = random.randint(1, len(weights))
            test = weights.__str__() + "\n" + k.__str__()
            tests.append(test)
        tests = "\n".join(tests)

    if int(challenge_id) == 863:
        tests = []
        possible_values = [i for i in range(500)]
        for test in range(8):
            tree = []
            number_of_nodes = 488
            # tree = possible_values
            tree.extend(random.sample(possible_values, number_of_nodes))
            target = tree[-1]
            distance = test * 3
            tests.append(
                "\n".join([tree.__str__(), target.__str__(), distance.__str__()])
            )
        tests = "\n".join(tests)

    if int(challenge_id) == 802:
        tests = []
        # min test
        graph = [[0]]
        tests.append(graph.__str__())

        graph = [[0], [1]]
        tests.append(graph.__str__())

        graph = [[0, 1], [0, 1]]
        tests.append(graph.__str__())

        graph = [[], [1], []]
        tests.append(graph.__str__())

        possible_edges = [i for i in range(10 ** 4 - 2)]
        for test in range(4):
            graph = []
            number_of_edges_sum = 0
            for node in range(10 ** 4 - 2):
                number_of_edges = random.randint(0, 6)
                number_of_edges_sum += number_of_edges
                graph.append(sorted(random.sample(possible_edges, number_of_edges)))
            print(number_of_edges_sum)
            tests.append(graph.__str__())

        for test in range(4):
            graph = []
            number_of_edges = 0
            number_of_edges_sum = 0
            for node in range(10 ** 4 - 2):
                number_of_edges = 6 - (node // 1500)
                number_of_edges %= len(possible_edges)
                graph.append(sorted(random.sample(possible_edges, number_of_edges)))
                number_of_edges_sum += number_of_edges
            print(number_of_edges, number_of_edges_sum)
            tests.append(graph.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 207:
        tests = []
        # min test
        number_of_nodes = 1
        graph = [[0, 0]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2
        graph = [[0, 0], [1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2
        graph = [[0, 1], [1, 0], [0, 0], [1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 5
        graph = []
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 3
        graph = [[1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant loop
        number_of_nodes = 2000
        graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant line
        number_of_nodes = 2000
        graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes - 1)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant reverse line
        number_of_nodes = 2000
        graph = [[i - 1, i] for i in range(1, number_of_nodes)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2000
        possible_edges = [i for i in range(number_of_nodes)]
        for test in range(4):
            graph = []
            number_of_edges_sum = 0
            for node in range(number_of_nodes):
                number_of_edges = random.randint(0, 4)
                number_of_edges_sum += number_of_edges
                edges = random.sample(possible_edges, number_of_edges)
                for e in edges:
                    graph.append([node, e])
            print(number_of_edges_sum)
            tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        for test in range(4):
            graph = []
            number_of_edges = 0
            number_of_edges_sum = 0
            for node in range(number_of_nodes):
                number_of_edges = random.randint(0, 10)
                number_of_edges_sum += number_of_edges
                if number_of_edges_sum >= 5000:
                    number_of_edges_sum -= number_of_edges
                    break
                edges = random.sample(possible_edges, number_of_edges)
                for e in edges:
                    graph.append([node, e])
            print(number_of_edges, number_of_edges_sum)
            tests.append(str(number_of_nodes) + "\n" + graph.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 1218:
        from . import Generator1218
        tests = Generator1218.generate()

    if int(challenge_id) == 1751:
        from . import Generator1751
        tests = Generator1751.generate()

    if int(challenge_id) == 735:
        from . import Generator735
        tests = Generator735.generate()

    if int(challenge_id) == 673:
        from . import Generator673
        tests = Generator673.generate()

    if int(challenge_id) == 1870:
        from . import Generator1870
        tests = Generator1870.generate()

    if int(challenge_id) == 712:
        from . import Generator712
        tests = Generator712.generate()

    if int(challenge_id) == 139:
        from . import Generator139
        tests = Generator139.generate()

    if int(challenge_id) == 33:
        from . import Generator33
        tests = Generator33.generate()

    if int(challenge_id) == 63:
        from . import Generator63
        tests = Generator63.generate()

    if int(challenge_id) == 2369:
        from . import Generator2369
        tests = Generator2369.generate()

    if int(challenge_id) == 239:
        from . import Generator239
        tests = Generator239.generate()

    if int(challenge_id) == 1615:
        from . import Generator1615
        tests = Generator1615.generate()

    if int(challenge_id) == 1489:
        from . import Generator1489
        tests = Generator1489.generate()

    if int(challenge_id) == 1203:
        from . import Generator1203
        tests = Generator1203.generate()

    date = time.time()
    write_file(f"testcase_{challenge_id}_{int(date)}.txt", tests)
