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
        459,
        97,
        403,
        1326,
        2707,
        1376,
        1282,
        1647,
        135,
        332,
        1584,
        1631,
        847,
        1337,
        287,
        287,
        1658,
        4,
        392,
        1048,
        799,
        389,
        316,
        880,
        905,
        896,
        456,
        557,
        2038,
        1512,
        706,
        229,
        343,
        1420,
        1458,
        34,
        2009,
        2251,
        1095,
        746,
        2742,
        1269,
        119,
        1361,
        2050,
        844,
        341,
        1425,
        1793,
        342,
        515,
        779,
        823,
        5,
        1220,
        458,
        1356,
        2433,
        501,
        2265,
        1441,
        1503,
        1535,
        1845,
        1921,
        2849,
        1759,
        1743,
        2642,
        815,
        2785,
        1930,
        1846,
        1980,
        1877,
        1838,
        1887,
        2391,
        1814,
        1424,
        1630,
        1561,
        1685,
        1727,
        935,
        2147,
        191,
        1611,
        1662,
        1160,
        1266,
        2264,
        1688,
        1716,
        1903,
        606,
        94,
        867,
        1287,
        1464,
        1582,
        2482,
        1436,
        242,
        2353,
        1913,
        661,
        2706,
        1637,
        1422,
        1496,
        1758,
        91,
        1155,
        1578,
        1335,
        1897,
        1624,
        455,
        2610,
        2125,
        2870,
        300,
        1235,
        446,
        938,
        872,
        2385,
        1026,
        1704,
        1347,
        1657,
        2225,
        380,
        1207,
        322,
        70,
        931,
        907,
        198,
        645,
        1239,
        1457,
        1143,
        576,
        629,
        1074,
        232,
        150,
        739,
        2966,
        1291,
        1043,
        76,
        387,
        49,
        451,
        279,
        368,
        647,
        1463,
        169,
        2108,
        2149,
        2971,
        1481,
        1642,
        2402,
        231,
        268,
        201,
        997,
        787,
        2092,
        2709,
        100,
        543,
        513,
        1609,
        2864,
        977,
        19,
        # insert next challenge here
    ]
    if int(challenge_id) == -1:
        challenge_id = implemented_challenges[-1]

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
        from source import Generator1218
        tests = Generator1218.generate()

    if int(challenge_id) == 1751:
        from source import Generator1751
        tests = Generator1751.generate()

    if int(challenge_id) == 735:
        from source import Generator735
        tests = Generator735.generate()

    if int(challenge_id) == 673:
        from source import Generator673
        tests = Generator673.generate()

    if int(challenge_id) == 1870:
        from source import Generator1870
        tests = Generator1870.generate()

    if int(challenge_id) == 712:
        from source import Generator712
        tests = Generator712.generate()

    if int(challenge_id) == 139:
        from source import Generator139
        tests = Generator139.generate()

    if int(challenge_id) == 33:
        from source import Generator33
        tests = Generator33.generate()

    if int(challenge_id) == 63:
        from source import Generator63
        tests = Generator63.generate()

    if int(challenge_id) == 2369:
        from source import Generator2369
        tests = Generator2369.generate()

    if int(challenge_id) == 239:
        from source import Generator239
        tests = Generator239.generate()

    if int(challenge_id) == 1615:
        from source import Generator1615
        tests = Generator1615.generate()

    if int(challenge_id) == 1489:
        from source import Generator1489
        tests = Generator1489.generate()

    if int(challenge_id) == 1203:
        from source import Generator1203
        tests = Generator1203.generate()

    if int(challenge_id) == 459:
        from source import Generator459
        tests = Generator459.generate()

    if int(challenge_id) == 97:
        from source import Generator97
        tests = Generator97.generate()

    if int(challenge_id) == 403:
        from source import Generator403
        tests = Generator403.generate()

    if int(challenge_id) == 1326:
        from source import Generator1326
        tests = Generator1326.generate()

    if int(challenge_id) == 2707:
        from source import Generator2707
        tests = Generator2707.generate()

    if int(challenge_id) == 1376:
        from source import Generator1376
        tests = Generator1376.generate()

    if int(challenge_id) == 1282:
        from source import Generator1282
        tests = Generator1282.generate()

    if int(challenge_id) == 1647:
        from source import Generator1647
        tests = Generator1647.generate()

    if int(challenge_id) == 135:
        from source import Generator135
        tests = Generator135.generate()

    if int(challenge_id) == 332:
        from source import Generator332
        tests = Generator332.generate()

    if int(challenge_id) == 1584:
        from source import Generator1584
        tests = Generator1584.generate()

    if int(challenge_id) == 1631:
        from source import Generator1631
        tests = Generator1631.generate()

    if int(challenge_id) == 847:
        from source import Generator847
        tests = Generator847.generate()

    if int(challenge_id) == 1337:
        from source import Generator1337
        tests = Generator1337.generate()

    if int(challenge_id) == 287:
        from source import Generator287
        tests = Generator287.generate()

    if int(challenge_id) == 287:
        from source import Generator287
        tests = Generator287.generate()

    if int(challenge_id) == 1658:
        from source import Generator1658
        tests = Generator1658.generate()

    if int(challenge_id) == 4:
        from source import Generator4
        tests = Generator4.generate()

    if int(challenge_id) == 392:
        from source import Generator392
        tests = Generator392.generate()

    if int(challenge_id) == 1048:
        from source import Generator1048
        tests = Generator1048.generate()

    if int(challenge_id) == 799:
        from source import Generator799
        tests = Generator799.generate()

    if int(challenge_id) == 389:
        from source import Generator389
        tests = Generator389.generate()

    if int(challenge_id) == 316:
        from source import Generator316
        tests = Generator316.generate()

    if int(challenge_id) == 880:
        from source import Generator880
        tests = Generator880.generate()

    if int(challenge_id) == 905:
        from source import Generator905
        tests = Generator905.generate()

    if int(challenge_id) == 896:
        from source import Generator896
        tests = Generator896.generate()

    if int(challenge_id) == 456:
        from source import Generator456
        tests = Generator456.generate()

    if int(challenge_id) == 557:
        from source import Generator557
        tests = Generator557.generate()

    if int(challenge_id) == 2038:
        from source import Generator2038
        tests = Generator2038.generate()

    if int(challenge_id) == 1512:
        from source import Generator1512
        tests = Generator1512.generate()

    if int(challenge_id) == 706:
        from source import Generator706
        tests = Generator706.generate()

    if int(challenge_id) == 229:
        from source import Generator229
        tests = Generator229.generate()

    if int(challenge_id) == 343:
        from source import Generator343
        tests = Generator343.generate()

    if int(challenge_id) == 1420:
        from source import Generator1420
        tests = Generator1420.generate()

    if int(challenge_id) == 1458:
        from source import Generator1458
        tests = Generator1458.generate()

    if int(challenge_id) == 34:
        from source import Generator34
        tests = Generator34.generate()

    if int(challenge_id) == 2009:
        from source import Generator2009
        tests = Generator2009.generate()

    if int(challenge_id) == 2251:
        from source import Generator2251
        tests = Generator2251.generate()

    if int(challenge_id) == 1095:
        from source import Generator1095
        tests = Generator1095.generate()

    if int(challenge_id) == 746:
        from source import Generator746
        tests = Generator746.generate()

    if int(challenge_id) == 2742:
        from source import Generator2742
        tests = Generator2742.generate()

    if int(challenge_id) == 1269:
        from source import Generator1269
        tests = Generator1269.generate()

    if int(challenge_id) == 119:
        from source import Generator119
        tests = Generator119.generate()

    if int(challenge_id) == 1361:
        from source import Generator1361
        tests = Generator1361.generate()

    if int(challenge_id) == 2050:
        from source import Generator2050
        tests = Generator2050.generate()

    if int(challenge_id) == 844:
        from source import Generator844
        tests = Generator844.generate()

    if int(challenge_id) == 341:
        from source import Generator341
        tests = Generator341.generate()

    if int(challenge_id) == 1425:
        from source import Generator1425
        tests = Generator1425.generate()

    if int(challenge_id) == 1793:
        from source import Generator1793
        tests = Generator1793.generate()

    if int(challenge_id) == 342:
        from source import Generator342
        tests = Generator342.generate()

    if int(challenge_id) == 515:
        from source import Generator515
        tests = Generator515.generate()

    if int(challenge_id) == 779:
        from source import Generator779
        tests = Generator779.generate()

    if int(challenge_id) == 823:
        from source import Generator823
        tests = Generator823.generate()

    if int(challenge_id) == 5:
        from source import Generator5
        tests = Generator5.generate()

    if int(challenge_id) == 1220:
        from source import Generator1220
        tests = Generator1220.generate()

    if int(challenge_id) == 458:
        from source import Generator458
        tests = Generator458.generate()

    if int(challenge_id) == 1356:
        from source import Generator1356
        tests = Generator1356.generate()

    if int(challenge_id) == 2433:
        from source import Generator2433
        tests = Generator2433.generate()

    if int(challenge_id) == 501:
        from source import Generator501
        tests = Generator501.generate()

    if int(challenge_id) == 2265:
        from source import Generator2265
        tests = Generator2265.generate()

    if int(challenge_id) == 1441:
        from source import Generator1441
        tests = Generator1441.generate()

    if int(challenge_id) == 1503:
        from source import Generator1503
        tests = Generator1503.generate()

    if int(challenge_id) == 1535:
        from source import Generator1535
        tests = Generator1535.generate()

    if int(challenge_id) == 1845:
        from source import Generator1845
        tests = Generator1845.generate()

    if int(challenge_id) == 1921:
        from source import Generator1921
        tests = Generator1921.generate()

    if int(challenge_id) == 2849:
        from source import Generator2849
        tests = Generator2849.generate()

    if int(challenge_id) == 1759:
        from source import Generator1759
        tests = Generator1759.generate()

    if int(challenge_id) == 1743:
        from source import Generator1743
        tests = Generator1743.generate()

    if int(challenge_id) == 2642:
        from source import Generator2642
        tests = Generator2642.generate()

    if int(challenge_id) == 815:
        from source import Generator815
        tests = Generator815.generate()

    if int(challenge_id) == 2785:
        from source import Generator2785
        tests = Generator2785.generate()

    if int(challenge_id) == 1930:
        from source import Generator1930
        tests = Generator1930.generate()

    if int(challenge_id) == 1846:
        from source import Generator1846
        tests = Generator1846.generate()

    if int(challenge_id) == 1980:
        from source import Generator1980
        tests = Generator1980.generate()

    if int(challenge_id) == 1877:
        from source import Generator1877
        tests = Generator1877.generate()

    if int(challenge_id) == 1838:
        from source import Generator1838
        tests = Generator1838.generate()

    if int(challenge_id) == 1887:
        from source import Generator1887
        tests = Generator1887.generate()

    if int(challenge_id) == 2391:
        from source import Generator2391
        tests = Generator2391.generate()

    if int(challenge_id) == 1814:
        from source import Generator1814
        tests = Generator1814.generate()

    if int(challenge_id) == 1424:
        from source import Generator1424
        tests = Generator1424.generate()

    if int(challenge_id) == 1630:
        from source import Generator1630
        tests = Generator1630.generate()

    if int(challenge_id) == 1561:
        from source import Generator1561
        tests = Generator1561.generate()

    if int(challenge_id) == 1685:
        from source import Generator1685
        tests = Generator1685.generate()

    if int(challenge_id) == 1727:
        from source import Generator1727
        tests = Generator1727.generate()

    if int(challenge_id) == 935:
        from source import Generator935
        tests = Generator935.generate()

    if int(challenge_id) == 2147:
        from source import Generator2147
        tests = Generator2147.generate()

    if int(challenge_id) == 191:
        from source import Generator191
        tests = Generator191.generate()

    if int(challenge_id) == 1611:
        from source import Generator1611
        tests = Generator1611.generate()

    if int(challenge_id) == 1662:
        from source import Generator1662
        tests = Generator1662.generate()

    if int(challenge_id) == 1160:
        from source import Generator1160
        tests = Generator1160.generate()

    if int(challenge_id) == 1266:
        from source import Generator1266
        tests = Generator1266.generate()

    if int(challenge_id) == 2264:
        from source import Generator2264
        tests = Generator2264.generate()

    if int(challenge_id) == 1688:
        from source import Generator1688
        tests = Generator1688.generate()

    if int(challenge_id) == 1716:
        from source import Generator1716
        tests = Generator1716.generate()

    if int(challenge_id) == 1903:
        from source import Generator1903
        tests = Generator1903.generate()

    if int(challenge_id) == 606:
        from source import Generator606
        tests = Generator606.generate()

    if int(challenge_id) == 94:
        from source import Generator94
        tests = Generator94.generate()

    if int(challenge_id) == 867:
        from source import Generator867
        tests = Generator867.generate()

    if int(challenge_id) == 1287:
        from source import Generator1287
        tests = Generator1287.generate()

    if int(challenge_id) == 1464:
        from source import Generator1464
        tests = Generator1464.generate()

    if int(challenge_id) == 1582:
        from source import Generator1582
        tests = Generator1582.generate()

    if int(challenge_id) == 2482:
        from source import Generator2482
        tests = Generator2482.generate()

    if int(challenge_id) == 1436:
        from source import Generator1436
        tests = Generator1436.generate()

    if int(challenge_id) == 242:
        from source import Generator242
        tests = Generator242.generate()

    if int(challenge_id) == 2353:
        from source import Generator2353
        tests = Generator2353.generate()

    if int(challenge_id) == 1913:
        from source import Generator1913
        tests = Generator1913.generate()

    if int(challenge_id) == 661:
        from source import Generator661
        tests = Generator661.generate()

    if int(challenge_id) == 2706:
        from source import Generator2706
        tests = Generator2706.generate()

    if int(challenge_id) == 1637:
        from source import Generator1637
        tests = Generator1637.generate()

    if int(challenge_id) == 1422:
        from source import Generator1422
        tests = Generator1422.generate()

    if int(challenge_id) == 1496:
        from source import Generator1496
        tests = Generator1496.generate()

    if int(challenge_id) == 1758:
        from source import Generator1758
        tests = Generator1758.generate()

    if int(challenge_id) == 91:
        from source import Generator91
        tests = Generator91.generate()

    if int(challenge_id) == 1155:
        from source import Generator1155
        tests = Generator1155.generate()

    if int(challenge_id) == 1578:
        from source import Generator1578
        tests = Generator1578.generate()

    if int(challenge_id) == 1335:
        from source import Generator1335
        tests = Generator1335.generate()

    if int(challenge_id) == 1897:
        from source import Generator1897
        tests = Generator1897.generate()

    if int(challenge_id) == 1624:
        from source import Generator1624
        tests = Generator1624.generate()

    if int(challenge_id) == 455:
        from source import Generator455
        tests = Generator455.generate()

    if int(challenge_id) == 2610:
        from source import Generator2610
        tests = Generator2610.generate()

    if int(challenge_id) == 2125:
        from source import Generator2125
        tests = Generator2125.generate()

    if int(challenge_id) == 2870:
        from source import Generator2870
        tests = Generator2870.generate()

    if int(challenge_id) == 300:
        from source import Generator300
        tests = Generator300.generate()

    if int(challenge_id) == 1235:
        from source import Generator1235
        tests = Generator1235.generate()

    if int(challenge_id) == 446:
        from source import Generator446
        tests = Generator446.generate()

    if int(challenge_id) == 938:
        from source import Generator938
        tests = Generator938.generate()

    if int(challenge_id) == 872:
        from source import Generator872
        tests = Generator872.generate()

    if int(challenge_id) == 2385:
        from source import Generator2385
        tests = Generator2385.generate()

    if int(challenge_id) == 1026:
        from source import Generator1026
        tests = Generator1026.generate()

    if int(challenge_id) == 1704:
        from source import Generator1704
        tests = Generator1704.generate()

    if int(challenge_id) == 1347:
        from source import Generator1347
        tests = Generator1347.generate()

    if int(challenge_id) == 1657:
        from source import Generator1657
        tests = Generator1657.generate()

    if int(challenge_id) == 2225:
        from source import Generator2225
        tests = Generator2225.generate()

    if int(challenge_id) == 380:
        from source import Generator380
        tests = Generator380.generate()

    if int(challenge_id) == 1207:
        from source import Generator1207
        tests = Generator1207.generate()

    if int(challenge_id) == 70:
        from source import Generator70
        tests = Generator70.generate()

    if int(challenge_id) == 322:
        from source import Generator322
        tests = Generator322.generate()

    if int(challenge_id) == 931:
        from source import Generator931
        tests = Generator931.generate()

    if int(challenge_id) == 907:
        from source import Generator907
        tests = Generator907.generate()

    if int(challenge_id) == 198:
        from source import Generator198
        tests = Generator198.generate()

    if int(challenge_id) == 645:
        from source import Generator645
        tests = Generator645.generate()

    if int(challenge_id) == 1239:
        from source import Generator1239
        tests = Generator1239.generate()

    if int(challenge_id) == 1457:
        from source import Generator1457
        tests = Generator1457.generate()

    if int(challenge_id) == 1143:
        from source import Generator1143
        tests = Generator1143.generate()

    if int(challenge_id) == 576:
        from source import Generator576
        tests = Generator576.generate()

    if int(challenge_id) == 629:
        from source import Generator629
        tests = Generator629.generate()

    if int(challenge_id) == 1074:
        from source import Generator1074
        tests = Generator1074.generate()

    if int(challenge_id) == 232:
        from source import Generator232
        tests = Generator232.generate()

    if int(challenge_id) == 150:
        from source import Generator150
        tests = Generator150.generate()

    if int(challenge_id) == 739:
        from source import Generator739
        tests = Generator739.generate()

    if int(challenge_id) == 2966:
        from source import Generator2966
        tests = Generator2966.generate()

    if int(challenge_id) == 1291:
        from source import Generator1291
        tests = Generator1291.generate()

    if int(challenge_id) == 1043:
        from source import Generator1043
        tests = Generator1043.generate()

    if int(challenge_id) == 76:
        from source import Generator76
        tests = Generator76.generate()

    if int(challenge_id) == 387:
        from source import Generator387
        tests = Generator387.generate()

    if int(challenge_id) == 49:
        from source import Generator49
        tests = Generator49.generate()

    if int(challenge_id) == 451:
        from source import Generator451
        tests = Generator451.generate()

    if int(challenge_id) == 279:
        from source import Generator279
        tests = Generator279.generate()

    if int(challenge_id) == 368:
        from source import Generator368
        tests = Generator368.generate()

    if int(challenge_id) == 647:
        from source import Generator647
        tests = Generator647.generate()

    if int(challenge_id) == 1463:
        from source import Generator1463
        tests = Generator1463.generate()

    if int(challenge_id) == 169:
        from source import Generator169
        tests = Generator169.generate()

    if int(challenge_id) == 2108:
        from source import Generator2108
        tests = Generator2108.generate()

    if int(challenge_id) == 2149:
        from source import Generator2149
        tests = Generator2149.generate()

    if int(challenge_id) == 2971:
        from source import Generator2971
        tests = Generator2971.generate()

    if int(challenge_id) == 1481:
        from source import Generator1481
        tests = Generator1481.generate()

    if int(challenge_id) == 1642:
        from source import Generator1642
        tests = Generator1642.generate()

    if int(challenge_id) == 2402:
        from source import Generator2402
        tests = Generator2402.generate()

    if int(challenge_id) == 231:
        from source import Generator231
        tests = Generator231.generate()

    if int(challenge_id) == 268:
        from source import Generator268
        tests = Generator268.generate()

    if int(challenge_id) == 201:
        from source import Generator201
        tests = Generator201.generate()

    if int(challenge_id) == 997:
        from source import Generator997
        tests = Generator997.generate()

    if int(challenge_id) == 787:
        from source import Generator787
        tests = Generator787.generate()

    if int(challenge_id) == 2092:
        from source import Generator2092
        tests = Generator2092.generate()

    if int(challenge_id) == 2709:
        from source import Generator2709
        tests = Generator2709.generate()

    if int(challenge_id) == 100:
        from source import Generator100
        tests = Generator100.generate()

    if int(challenge_id) == 543:
        from source import Generator543
        tests = Generator543.generate()

    if int(challenge_id) == 513:
        from source import Generator513
        tests = Generator513.generate()

    if int(challenge_id) == 1609:
        from source import Generator1609
        tests = Generator1609.generate()

    if int(challenge_id) == 2864:
        from source import Generator2864
        tests = Generator2864.generate()

    if int(challenge_id) == 977:
        from source import Generator977
        tests = Generator977.generate()

    if int(challenge_id) == 19:
        from source import Generator19
        tests = Generator19.generate()

    # insert next challenge import here

    date = time.time()
    filename = f"testcase_{challenge_id}_{int(date)}.txt"
    write_file(filename, tests)
    return filename

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate testcases for a challenge")
    parser.add_argument("challenge_id", nargs='?', help="The challenge id", default=-1, type=int)
    args = parser.parse_args()
    filename = main(args.challenge_id)
    print("Testcases written to", filename)