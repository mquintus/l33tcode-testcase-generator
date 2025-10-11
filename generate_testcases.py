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
        948,
        1750,
        141,
        876,
        2540,
        349,
        791,
        1171,
        2485,
        930,
        238,
        525,
        57,
        452,
        621,
        1669,
        206,
        234,
        143,
        287,
        442,
        41,
        713,
        2958,
        2962,
        992,
        2444,
        58,
        205,
        79,
        1614,
        1544,
        1249,
        678,
        1700,
        2073,
        950,
        402,
        42,
        85,
        404,
        129,
        623,
        988,
        463,
        200,
        1992,
        1971,
        752,
        310,
        1137,
        2370,
        1289,
        514,
        834,
        2997,
        1915,
        2000,
        2441,
        165,
        881,
        237,
        2487,
        2816,
        506,
        3075,
        786,
        857,
        2373,
        861,
        1219,
        2812,
        2331,
        1325,
        979,
        3068,
        1863,
        78,
        131,
        2597,
        1255,
        140,
        552,
        1608,
        1208,
        1404,
        1442,
        260,
        3110,
        344,
        2486,
        409,
        1002,
        846,
        648,
        523,
        974,
        1051,
        1122,
        75,
        2037,
        945,
        502,
        330,
        633,
        826,
        1482,
        1552,
        1052,
        1248,
        1438,
        995,
        1038,
        1382,
        1791,
        2285,
        2192,
        1579,
        1550,
        350,
        1509,
        2181,
        2058,
        2582,
        1518,
        1823,
        1701,
        1598,
        1190,
        1717,
        2751,
        726,
        2196,
        2096,
        1110,
        1530,
        1380,
        1605,
        2392,
        2418,
        1636,
        2191,
        912,
        1334,
        2976,
        2045,
        1395,
        1653,
        1105,
        2678,
        2134,
        1460,
        1508,
        2053,
        3016,
        273,
        885,
        840,
        959,
        1568,
        703,
        40,
        719,
        860,
        1937,
        264,
        650,
        1140,
        664,
        476,
        592,
        564,
        145,
        590,
        1514,
        1905,
        947,
        2699,
        1514,
        2022,
        1894,
        1945,
        874,
        2028,
        3217,
        1367,
        725,
        2326,
        2807,
        2220,
        1684,
        1310,
        2419,
        1371,
        539,
        884,
        179,
        241,
        214,
        386,
        440,
        2707,
        3043,
        2416,
        729,
        731,
        641,
        432,
        1381,
        1497,
        1331,
        1590,
        2491,
        567,
        1813,
        2696,
        1963,
        921,
        962,
        1942,
        2406,
        632,
        2530,
        2938,
        1405,
        670,
        2044,
        1545,
        1106,
        1593,
        2583,
        2641,
        951,
        1233,
        2458,
        1277,
        2501,
        2684,
        1671,
        2463,
        1957,
        2490,
        796,
        3163,
        2914,
        3011,
        2275,
        1829,
        3133,
        3097,
        2601,
        2070,
        2563,
        2064,
        1574,
        3254,
        862,
        1652,
        2461,
        2516,
        2257,
        1072,
        1861,
        1975,
        773,
        2924,
        3243,
        2290,
        2577,
        2097,
        1346,
        1455,
        2109,
        2825,
        2337,
        2554,
        1760,
        2054,
        3152,
        2981,
        2779,
        2558,
        2593,
        2762,
        1792,
        3264,
        2182,
        1475,
        769,
        2415,
        2872,
        2940,
        2471,
        3203,
        515,
        494,
        1014,
        689,
        1639,
        2466,
        983,
        1422,
        2559,
        2270,
        1930,
        2381,
        1769,
        1408,
        3042,
        2185,
        916,
        1400,
        2116,
        3223,
        2657,
        2429,
        2425,
        2683,
        1368,
        407,
        2661,
        2017,
        1765,
        1267,
        802,
        2948,
        2127,
        1462,
        2658,
        684,
        2493,
        827,
        3151,
        1752,
        3105,
        1800,
        1790,
        1726,
        3160,
        2349,
        2364,
        3174,
        1910,
        2342,
        3066,
        1352,
        2698,
        1718,
        1079,
        2375,
        1415,
        1980,
        1261,
        1028,
        889,
        2467,
        1524,
        1749,
        873,
        1092,
        2460,
        2570,
        2161,
        1780,
        2579,
        2965,
        2523,
        2379,
        3208,
        3306,
        1358,
        2529,
        3356,
        2226,
        2560,
        2594,
        2206,
        2401,
        3191,
        3108,
        2115,
        2685,
        1976,
        3169,
        3394,
        2033,
        2780,
        2503,
        2818,
        763,
        2551,
        2140,
        2873,
        2874,
        1123,
        1863,
        368,
        416,
        3396,
        3375,
        2999,
        2843,
        3272,
        1922,
        1534,
        2179,
        2537,
        2176,
        38,
        2563,
        781,
        2145,
        2338,
        1399,
        2799,
        2845,
        2444,
        3392,
        2302,
        2962,
        1295,
        2071,
        838,
        1007,
        1128,
        790,
        1920,
        3341,
        3342,
        3343,
        2918,
        1550,
        2094,
        3335,
        3337,
        2900,
        2901,
        75,
        1931,
        3024,
        3355,
        73,
        3362,
        3068,
        2942,
        2131,
        1857,
        2894,
        3372,
        3373,
        2359,
        909,
        2929,
        135,
        1298,
        3403,
        1061,
        2434,
        3170,
        386,
        440,
        3442,
        3445,
        3423,
        2616,
        2566,
        1432,
        2016,
        3405,
        2966,
        2294,
        3443,
        3085,
        2138,
        2081,
        2200,
        2040,
        2311,
        2014,
        2099,
        1498,
        594,
        3330,
        3333,
        3304,
        3307,
        1394,
        1865,
        1353,
        1751,
        3439,
        3440,
        2402,
        1900,
        2410,
        1290,
        3136,
        3201,
        3202,
        2163,
        1233,
        1948,
        1957,
        1695,
        1717,
        2322,
        3487,
        3480,
        2210,
        2044,
        2411,
        2419,
        898,
        118,
        2561,
        2106,
        904,
        3477,
        3479,
        3363,
        808,
        231,
        869,
        2438,
        2787,
        326,
        2264,
        342,
        1323,
        837,
        679,
        2348,
        1277,
        1504,
        3195,
        3197,
        1493,
        498,
        3000,
        3459,
        3446,
        3021,
        36,
        37,
        1792,
        3025,
        3027,
        3516,
        2749,
        3495,
        1304,
        1317,
        2327,
        1733,
        2785,
        3227,
        3541,
        966,
        1935,
        2197,
        2353,
        3408,
        3484,
        3508,
        1912,
        3005,
        165,
        166,
        120,
        611,
        812,
        976,
        1039,
        2221,
        1518,
        3100,
        407,
        11,
        417,
        778,
        1488,
        2300,
        3494,
        3147,
        3186,
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

    if int(challenge_id) == 948:
        from source import Generator948
        tests = Generator948.generate()

    if int(challenge_id) == 1750:
        from source import Generator1750
        tests = Generator1750.generate()

    if int(challenge_id) == 141:
        from source import Generator141
        tests = Generator141.generate()

    if int(challenge_id) == 876:
        from source import Generator876
        tests = Generator876.generate()

    if int(challenge_id) == 2540:
        from source import Generator2540
        tests = Generator2540.generate()

    if int(challenge_id) == 349:
        from source import Generator349
        tests = Generator349.generate()

    if int(challenge_id) == 791:
        from source import Generator791
        tests = Generator791.generate()

    if int(challenge_id) == 1171:
        from source import Generator1171
        tests = Generator1171.generate()

    if int(challenge_id) == 2485:
        from source import Generator2485
        tests = Generator2485.generate()

    if int(challenge_id) == 930:
        from source import Generator930
        tests = Generator930.generate()

    if int(challenge_id) == 238:
        from source import Generator238
        tests = Generator238.generate()

    if int(challenge_id) == 525:
        from source import Generator525
        tests = Generator525.generate()

    if int(challenge_id) == 57:
        from source import Generator57
        tests = Generator57.generate()

    if int(challenge_id) == 452:
        from source import Generator452
        tests = Generator452.generate()

    if int(challenge_id) == 621:
        from source import Generator621
        tests = Generator621.generate()

    if int(challenge_id) == 1669:
        from source import Generator1669
        tests = Generator1669.generate()

    if int(challenge_id) == 206:
        from source import Generator206
        tests = Generator206.generate()

    if int(challenge_id) == 234:
        from source import Generator234
        tests = Generator234.generate()

    if int(challenge_id) == 143:
        from source import Generator143
        tests = Generator143.generate()

    if int(challenge_id) == 287:
        from source import Generator287
        tests = Generator287.generate()

    if int(challenge_id) == 442:
        from source import Generator442
        tests = Generator442.generate()

    if int(challenge_id) == 41:
        from source import Generator41
        tests = Generator41.generate()

    if int(challenge_id) == 713:
        from source import Generator713
        tests = Generator713.generate()

    if int(challenge_id) == 2958:
        from source import Generator2958
        tests = Generator2958.generate()

    if int(challenge_id) == 2962:
        from source import Generator2962
        tests = Generator2962.generate()

    if int(challenge_id) == 992:
        from source import Generator992
        tests = Generator992.generate()

    if int(challenge_id) == 2444:
        from source import Generator2444
        tests = Generator2444.generate()

    if int(challenge_id) == 58:
        from source import Generator58
        tests = Generator58.generate()

    if int(challenge_id) == 205:
        from source import Generator205
        tests = Generator205.generate()

    if int(challenge_id) == 79:
        from source import Generator79
        tests = Generator79.generate()

    if int(challenge_id) == 1614:
        from source import Generator1614
        tests = Generator1614.generate()

    if int(challenge_id) == 1544:
        from source import Generator1544
        tests = Generator1544.generate()

    if int(challenge_id) == 1249:
        from source import Generator1249
        tests = Generator1249.generate()

    if int(challenge_id) == 678:
        from source import Generator678
        tests = Generator678.generate()

    if int(challenge_id) == 1700:
        from source import Generator1700
        tests = Generator1700.generate()

    if int(challenge_id) == 2073:
        from source import Generator2073
        tests = Generator2073.generate()

    if int(challenge_id) == 950:
        from source import Generator950
        tests = Generator950.generate()

    if int(challenge_id) == 402:
        from source import Generator402
        tests = Generator402.generate()

    if int(challenge_id) == 42:
        from source import Generator42
        tests = Generator42.generate()

    if int(challenge_id) == 85:
        from source import Generator85
        tests = Generator85.generate()

    if int(challenge_id) == 404:
        from source import Generator404
        tests = Generator404.generate()

    if int(challenge_id) == 129:
        from source import Generator129
        tests = Generator129.generate()

    if int(challenge_id) == 623:
        from source import Generator623
        tests = Generator623.generate()

    if int(challenge_id) == 988:
        from source import Generator988
        tests = Generator988.generate()

    if int(challenge_id) == 463:
        from source import Generator463
        tests = Generator463.generate()

    if int(challenge_id) == 200:
        from source import Generator200
        tests = Generator200.generate()

    if int(challenge_id) == 1992:
        from source import Generator1992
        tests = Generator1992.generate()

    if int(challenge_id) == 1971:
        from source import Generator1971
        tests = Generator1971.generate()

    if int(challenge_id) == 752:
        from source import Generator752
        tests = Generator752.generate()

    if int(challenge_id) == 310:
        from source import Generator310
        tests = Generator310.generate()

    if int(challenge_id) == 1137:
        from source import Generator1137
        tests = Generator1137.generate()

    if int(challenge_id) == 2370:
        from source import Generator2370
        tests = Generator2370.generate()

    if int(challenge_id) == 1289:
        from source import Generator1289
        tests = Generator1289.generate()

    if int(challenge_id) == 514:
        from source import Generator514
        tests = Generator514.generate()

    if int(challenge_id) == 834:
        from source import Generator834
        tests = Generator834.generate()

    if int(challenge_id) == 2997:
        from source import Generator2997
        tests = Generator2997.generate()

    if int(challenge_id) == 1915:
        from source import Generator1915
        tests = Generator1915.generate()

    if int(challenge_id) == 2000:
        from source import Generator2000
        tests = Generator2000.generate()

    if int(challenge_id) == 2441:
        from source import Generator2441
        tests = Generator2441.generate()

    if int(challenge_id) == 165:
        from source import Generator165
        tests = Generator165.generate()

    if int(challenge_id) == 881:
        from source import Generator881
        tests = Generator881.generate()

    if int(challenge_id) == 237:
        from source import Generator237
        tests = Generator237.generate()

    if int(challenge_id) == 2487:
        from source import Generator2487
        tests = Generator2487.generate()

    if int(challenge_id) == 2816:
        from source import Generator2816
        tests = Generator2816.generate()

    if int(challenge_id) == 506:
        from source import Generator506
        tests = Generator506.generate()

    if int(challenge_id) == 3075:
        from source import Generator3075
        tests = Generator3075.generate()

    if int(challenge_id) == 786:
        from source import Generator786
        tests = Generator786.generate()

    if int(challenge_id) == 857:
        from source import Generator857
        tests = Generator857.generate()

    if int(challenge_id) == 2373:
        from source import Generator2373
        tests = Generator2373.generate()

    if int(challenge_id) == 861:
        from source import Generator861
        tests = Generator861.generate()

    if int(challenge_id) == 1219:
        from source import Generator1219
        tests = Generator1219.generate()

    if int(challenge_id) == 2812:
        from source import Generator2812
        tests = Generator2812.generate()

    if int(challenge_id) == 2331:
        from source import Generator2331
        tests = Generator2331.generate()

    if int(challenge_id) == 1325:
        from source import Generator1325
        tests = Generator1325.generate()

    if int(challenge_id) == 979:
        from source import Generator979
        tests = Generator979.generate()

    if int(challenge_id) == 3068:
        from source import Generator3068
        tests = Generator3068.generate()

    if int(challenge_id) == 1863:
        from source import Generator1863
        tests = Generator1863.generate()

    if int(challenge_id) == 78:
        from source import Generator78
        tests = Generator78.generate()

    if int(challenge_id) == 131:
        from source import Generator131
        tests = Generator131.generate()

    if int(challenge_id) == 2597:
        from source import Generator2597
        tests = Generator2597.generate()

    if int(challenge_id) == 1255:
        from source import Generator1255
        tests = Generator1255.generate()

    if int(challenge_id) == 140:
        from source import Generator140
        tests = Generator140.generate()

    if int(challenge_id) == 552:
        from source import Generator552
        tests = Generator552.generate()

    if int(challenge_id) == 1608:
        from source import Generator1608
        tests = Generator1608.generate()

    if int(challenge_id) == 1208:
        from source import Generator1208
        tests = Generator1208.generate()

    if int(challenge_id) == 1404:
        from source import Generator1404
        tests = Generator1404.generate()

    if int(challenge_id) == 1442:
        from source import Generator1442
        tests = Generator1442.generate()

    if int(challenge_id) == 260:
        from source import Generator260
        tests = Generator260.generate()

    if int(challenge_id) == 3110:
        from source import Generator3110
        tests = Generator3110.generate()

    if int(challenge_id) == 344:
        from source import Generator344
        tests = Generator344.generate()

    if int(challenge_id) == 2486:
        from source import Generator2486
        tests = Generator2486.generate()

    if int(challenge_id) == 409:
        from source import Generator409
        tests = Generator409.generate()

    if int(challenge_id) == 1002:
        from source import Generator1002
        tests = Generator1002.generate()

    if int(challenge_id) == 846:
        from source import Generator846
        tests = Generator846.generate()

    if int(challenge_id) == 648:
        from source import Generator648
        tests = Generator648.generate()

    if int(challenge_id) == 523:
        from source import Generator523
        tests = Generator523.generate()

    if int(challenge_id) == 974:
        from source import Generator974
        tests = Generator974.generate()

    if int(challenge_id) == 1051:
        from source import Generator1051
        tests = Generator1051.generate()

    if int(challenge_id) == 1122:
        from source import Generator1122
        tests = Generator1122.generate()

    if int(challenge_id) == 75:
        from source import Generator75
        tests = Generator75.generate()

    if int(challenge_id) == 2037:
        from source import Generator2037
        tests = Generator2037.generate()

    if int(challenge_id) == 945:
        from source import Generator945
        tests = Generator945.generate()

    if int(challenge_id) == 502:
        from source import Generator502
        tests = Generator502.generate()

    if int(challenge_id) == 330:
        from source import Generator330
        tests = Generator330.generate()

    if int(challenge_id) == 633:
        from source import Generator633
        tests = Generator633.generate()

    if int(challenge_id) == 826:
        from source import Generator826
        tests = Generator826.generate()

    if int(challenge_id) == 1482:
        from source import Generator1482
        tests = Generator1482.generate()

    if int(challenge_id) == 1552:
        from source import Generator1552
        tests = Generator1552.generate()

    if int(challenge_id) == 1052:
        from source import Generator1052
        tests = Generator1052.generate()

    if int(challenge_id) == 1248:
        from source import Generator1248
        tests = Generator1248.generate()

    if int(challenge_id) == 1438:
        from source import Generator1438
        tests = Generator1438.generate()

    if int(challenge_id) == 995:
        from source import Generator995
        tests = Generator995.generate()

    if int(challenge_id) == 1038:
        from source import Generator1038
        tests = Generator1038.generate()

    if int(challenge_id) == 1382:
        from source import Generator1382
        tests = Generator1382.generate()

    if int(challenge_id) == 1791:
        from source import Generator1791
        tests = Generator1791.generate()

    if int(challenge_id) == 2285:
        from source import Generator2285
        tests = Generator2285.generate()

    if int(challenge_id) == 2192:
        from source import Generator2192
        tests = Generator2192.generate()

    if int(challenge_id) == 1579:
        from source import Generator1579
        tests = Generator1579.generate()

    if int(challenge_id) == 1550:
        from source import Generator1550
        tests = Generator1550.generate()

    if int(challenge_id) == 350:
        from source import Generator350
        tests = Generator350.generate()

    if int(challenge_id) == 1509:
        from source import Generator1509
        tests = Generator1509.generate()

    if int(challenge_id) == 2181:
        from source import Generator2181
        tests = Generator2181.generate()

    if int(challenge_id) == 2058:
        from source import Generator2058
        tests = Generator2058.generate()

    if int(challenge_id) == 2582:
        from source import Generator2582
        tests = Generator2582.generate()

    if int(challenge_id) == 1518:
        from source import Generator1518
        tests = Generator1518.generate()

    if int(challenge_id) == 1823:
        from source import Generator1823
        tests = Generator1823.generate()

    if int(challenge_id) == 1701:
        from source import Generator1701
        tests = Generator1701.generate()

    if int(challenge_id) == 1598:
        from source import Generator1598
        tests = Generator1598.generate()

    if int(challenge_id) == 1190:
        from source import Generator1190
        tests = Generator1190.generate()

    if int(challenge_id) == 1717:
        from source import Generator1717
        tests = Generator1717.generate()

    if int(challenge_id) == 2751:
        from source import Generator2751
        tests = Generator2751.generate()

    if int(challenge_id) == 726:
        from source import Generator726
        tests = Generator726.generate()

    if int(challenge_id) == 2196:
        from source import Generator2196
        tests = Generator2196.generate()

    if int(challenge_id) == 2096:
        from source import Generator2096
        tests = Generator2096.generate()

    if int(challenge_id) == 1110:
        from source import Generator1110
        tests = Generator1110.generate()

    if int(challenge_id) == 1530:
        from source import Generator1530
        tests = Generator1530.generate()

    if int(challenge_id) == 1380:
        from source import Generator1380
        tests = Generator1380.generate()

    if int(challenge_id) == 1605:
        from source import Generator1605
        tests = Generator1605.generate()

    if int(challenge_id) == 2392:
        from source import Generator2392
        tests = Generator2392.generate()

    if int(challenge_id) == 2418:
        from source import Generator2418
        tests = Generator2418.generate()

    if int(challenge_id) == 1636:
        from source import Generator1636
        tests = Generator1636.generate()

    if int(challenge_id) == 2191:
        from source import Generator2191
        tests = Generator2191.generate()

    if int(challenge_id) == 912:
        from source import Generator912
        tests = Generator912.generate()

    if int(challenge_id) == 1334:
        from source import Generator1334
        tests = Generator1334.generate()

    if int(challenge_id) == 2976:
        from source import Generator2976
        tests = Generator2976.generate()

    if int(challenge_id) == 2045:
        from source import Generator2045
        tests = Generator2045.generate()

    if int(challenge_id) == 1395:
        from source import Generator1395
        tests = Generator1395.generate()

    if int(challenge_id) == 1653:
        from source import Generator1653
        tests = Generator1653.generate()

    if int(challenge_id) == 1105:
        from source import Generator1105
        tests = Generator1105.generate()

    if int(challenge_id) == 2678:
        from source import Generator2678
        tests = Generator2678.generate()

    if int(challenge_id) == 2134:
        from source import Generator2134
        tests = Generator2134.generate()

    if int(challenge_id) == 1460:
        from source import Generator1460
        tests = Generator1460.generate()

    if int(challenge_id) == 1508:
        from source import Generator1508
        tests = Generator1508.generate()

    if int(challenge_id) == 2053:
        from source import Generator2053
        tests = Generator2053.generate()

    if int(challenge_id) == 3016:
        from source import Generator3016
        tests = Generator3016.generate()

    if int(challenge_id) == 273:
        from source import Generator273
        tests = Generator273.generate()

    if int(challenge_id) == 885:
        from source import Generator885
        tests = Generator885.generate()

    if int(challenge_id) == 840:
        from source import Generator840
        tests = Generator840.generate()

    if int(challenge_id) == 959:
        from source import Generator959
        tests = Generator959.generate()

    if int(challenge_id) == 1568:
        from source import Generator1568
        tests = Generator1568.generate()

    if int(challenge_id) == 703:
        from source import Generator703
        tests = Generator703.generate()

    if int(challenge_id) == 40:
        from source import Generator40
        tests = Generator40.generate()

    if int(challenge_id) == 719:
        from source import Generator719
        tests = Generator719.generate()

    if int(challenge_id) == 860:
        from source import Generator860
        tests = Generator860.generate()

    if int(challenge_id) == 1937:
        from source import Generator1937
        tests = Generator1937.generate()

    if int(challenge_id) == 264:
        from source import Generator264
        tests = Generator264.generate()

    if int(challenge_id) == 650:
        from source import Generator650
        tests = Generator650.generate()

    if int(challenge_id) == 1140:
        from source import Generator1140
        tests = Generator1140.generate()

    if int(challenge_id) == 664:
        from source import Generator664
        tests = Generator664.generate()

    if int(challenge_id) == 476:
        from source import Generator476
        tests = Generator476.generate()

    if int(challenge_id) == 592:
        from source import Generator592
        tests = Generator592.generate()

    if int(challenge_id) == 564:
        from source import Generator564
        tests = Generator564.generate()

    if int(challenge_id) == 145:
        from source import Generator145
        tests = Generator145.generate()

    if int(challenge_id) == 590:
        from source import Generator590
        tests = Generator590.generate()

    if int(challenge_id) == 1514:
        from source import Generator1514
        tests = Generator1514.generate()

    if int(challenge_id) == 1905:
        from source import Generator1905
        tests = Generator1905.generate()

    if int(challenge_id) == 947:
        from source import Generator947
        tests = Generator947.generate()

    if int(challenge_id) == 2699:
        from source import Generator2699
        tests = Generator2699.generate()

    if int(challenge_id) == 1514:
        from source import Generator1514
        tests = Generator1514.generate()

    if int(challenge_id) == 2022:
        from source import Generator2022
        tests = Generator2022.generate()

    if int(challenge_id) == 1894:
        from source import Generator1894
        tests = Generator1894.generate()

    if int(challenge_id) == 1945:
        from source import Generator1945
        tests = Generator1945.generate()

    if int(challenge_id) == 874:
        from source import Generator874
        tests = Generator874.generate()

    if int(challenge_id) == 2028:
        from source import Generator2028
        tests = Generator2028.generate()

    if int(challenge_id) == 3217:
        from source import Generator3217
        tests = Generator3217.generate()

    if int(challenge_id) == 1367:
        from source import Generator1367
        tests = Generator1367.generate()

    if int(challenge_id) == 725:
        from source import Generator725
        tests = Generator725.generate()

    if int(challenge_id) == 2326:
        from source import Generator2326
        tests = Generator2326.generate()

    if int(challenge_id) == 2807:
        from source import Generator2807
        tests = Generator2807.generate()

    if int(challenge_id) == 2220:
        from source import Generator2220
        tests = Generator2220.generate()

    if int(challenge_id) == 1684:
        from source import Generator1684
        tests = Generator1684.generate()

    if int(challenge_id) == 1310:
        from source import Generator1310
        tests = Generator1310.generate()

    if int(challenge_id) == 2419:
        from source import Generator2419
        tests = Generator2419.generate()

    if int(challenge_id) == 1371:
        from source import Generator1371
        tests = Generator1371.generate()

    if int(challenge_id) == 539:
        from source import Generator539
        tests = Generator539.generate()

    if int(challenge_id) == 884:
        from source import Generator884
        tests = Generator884.generate()

    if int(challenge_id) == 179:
        from source import Generator179
        tests = Generator179.generate()

    if int(challenge_id) == 241:
        from source import Generator241
        tests = Generator241.generate()

    if int(challenge_id) == 214:
        from source import Generator214
        tests = Generator214.generate()

    if int(challenge_id) == 386:
        from source import Generator386
        tests = Generator386.generate()

    if int(challenge_id) == 440:
        from source import Generator440
        tests = Generator440.generate()

    if int(challenge_id) == 2707:
        from source import Generator2707
        tests = Generator2707.generate()

    if int(challenge_id) == 3043:
        from source import Generator3043
        tests = Generator3043.generate()

    if int(challenge_id) == 2416:
        from source import Generator2416
        tests = Generator2416.generate()

    if int(challenge_id) == 729:
        from source import Generator729
        tests = Generator729.generate()

    if int(challenge_id) == 731:
        from source import Generator731
        tests = Generator731.generate()

    if int(challenge_id) == 641:
        from source import Generator641
        tests = Generator641.generate()

    if int(challenge_id) == 432:
        from source import Generator432
        tests = Generator432.generate()

    if int(challenge_id) == 1381:
        from source import Generator1381
        tests = Generator1381.generate()

    if int(challenge_id) == 1497:
        from source import Generator1497
        tests = Generator1497.generate()

    if int(challenge_id) == 1331:
        from source import Generator1331
        tests = Generator1331.generate()

    if int(challenge_id) == 1590:
        from source import Generator1590
        tests = Generator1590.generate()

    if int(challenge_id) == 2491:
        from source import Generator2491
        tests = Generator2491.generate()

    if int(challenge_id) == 567:
        from source import Generator567
        tests = Generator567.generate()

    if int(challenge_id) == 1813:
        from source import Generator1813
        tests = Generator1813.generate()

    if int(challenge_id) == 2696:
        from source import Generator2696
        tests = Generator2696.generate()

    if int(challenge_id) == 1963:
        from source import Generator1963
        tests = Generator1963.generate()

    if int(challenge_id) == 921:
        from source import Generator921
        tests = Generator921.generate()

    if int(challenge_id) == 962:
        from source import Generator962
        tests = Generator962.generate()

    if int(challenge_id) == 1942:
        from source import Generator1942
        tests = Generator1942.generate()

    if int(challenge_id) == 2406:
        from source import Generator2406
        tests = Generator2406.generate()

    if int(challenge_id) == 632:
        from source import Generator632
        tests = Generator632.generate()

    if int(challenge_id) == 2530:
        from source import Generator2530
        tests = Generator2530.generate()

    if int(challenge_id) == 2938:
        from source import Generator2938
        tests = Generator2938.generate()

    if int(challenge_id) == 1405:
        from source import Generator1405
        tests = Generator1405.generate()

    if int(challenge_id) == 670:
        from source import Generator670
        tests = Generator670.generate()

    if int(challenge_id) == 2044:
        from source import Generator2044
        tests = Generator2044.generate()

    if int(challenge_id) == 1545:
        from source import Generator1545
        tests = Generator1545.generate()

    if int(challenge_id) == 1106:
        from source import Generator1106
        tests = Generator1106.generate()

    if int(challenge_id) == 1593:
        from source import Generator1593
        tests = Generator1593.generate()

    if int(challenge_id) == 2583:
        from source import Generator2583
        tests = Generator2583.generate()

    if int(challenge_id) == 2641:
        from source import Generator2641
        tests = Generator2641.generate()

    if int(challenge_id) == 951:
        from source import Generator951
        tests = Generator951.generate()

    if int(challenge_id) == 1233:
        from source import Generator1233
        tests = Generator1233.generate()

    if int(challenge_id) == 2458:
        from source import Generator2458
        tests = Generator2458.generate()

    if int(challenge_id) == 1277:
        from source import Generator1277
        tests = Generator1277.generate()

    if int(challenge_id) == 2501:
        from source import Generator2501
        tests = Generator2501.generate()

    if int(challenge_id) == 2684:
        from source import Generator2684
        tests = Generator2684.generate()

    if int(challenge_id) == 1671:
        from source import Generator1671
        tests = Generator1671.generate()

    if int(challenge_id) == 2463:
        from source import Generator2463
        tests = Generator2463.generate()

    if int(challenge_id) == 1957:
        from source import Generator1957
        tests = Generator1957.generate()

    if int(challenge_id) == 2490:
        from source import Generator2490
        tests = Generator2490.generate()

    if int(challenge_id) == 796:
        from source import Generator796
        tests = Generator796.generate()

    if int(challenge_id) == 3163:
        from source import Generator3163
        tests = Generator3163.generate()

    if int(challenge_id) == 2914:
        from source import Generator2914
        tests = Generator2914.generate()

    if int(challenge_id) == 3011:
        from source import Generator3011
        tests = Generator3011.generate()

    if int(challenge_id) == 2275:
        from source import Generator2275
        tests = Generator2275.generate()

    if int(challenge_id) == 1829:
        from source import Generator1829
        tests = Generator1829.generate()

    if int(challenge_id) == 3133:
        from source import Generator3133
        tests = Generator3133.generate()

    if int(challenge_id) == 3097:
        from source import Generator3097
        tests = Generator3097.generate()

    if int(challenge_id) == 2601:
        from source import Generator2601
        tests = Generator2601.generate()

    if int(challenge_id) == 2070:
        from source import Generator2070
        tests = Generator2070.generate()

    if int(challenge_id) == 2563:
        from source import Generator2563
        tests = Generator2563.generate()

    if int(challenge_id) == 2064:
        from source import Generator2064
        tests = Generator2064.generate()

    if int(challenge_id) == 1574:
        from source import Generator1574
        tests = Generator1574.generate()

    if int(challenge_id) == 3254:
        from source import Generator3254
        tests = Generator3254.generate()

    if int(challenge_id) == 862:
        from source import Generator862
        tests = Generator862.generate()

    if int(challenge_id) == 1652:
        from source import Generator1652
        tests = Generator1652.generate()

    if int(challenge_id) == 2461:
        from source import Generator2461
        tests = Generator2461.generate()

    if int(challenge_id) == 2516:
        from source import Generator2516
        tests = Generator2516.generate()

    if int(challenge_id) == 2257:
        from source import Generator2257
        tests = Generator2257.generate()

    if int(challenge_id) == 1072:
        from source import Generator1072
        tests = Generator1072.generate()

    if int(challenge_id) == 1861:
        from source import Generator1861
        tests = Generator1861.generate()

    if int(challenge_id) == 1975:
        from source import Generator1975
        tests = Generator1975.generate()

    if int(challenge_id) == 773:
        from source import Generator773
        tests = Generator773.generate()

    if int(challenge_id) == 2924:
        from source import Generator2924
        tests = Generator2924.generate()

    if int(challenge_id) == 3243:
        from source import Generator3243
        tests = Generator3243.generate()

    if int(challenge_id) == 2290:
        from source import Generator2290
        tests = Generator2290.generate()

    if int(challenge_id) == 2577:
        from source import Generator2577
        tests = Generator2577.generate()

    if int(challenge_id) == 2097:
        from source import Generator2097
        tests = Generator2097.generate()

    if int(challenge_id) == 1346:
        from source import Generator1346
        tests = Generator1346.generate()

    if int(challenge_id) == 1455:
        from source import Generator1455
        tests = Generator1455.generate()

    if int(challenge_id) == 2109:
        from source import Generator2109
        tests = Generator2109.generate()

    if int(challenge_id) == 2825:
        from source import Generator2825
        tests = Generator2825.generate()

    if int(challenge_id) == 2337:
        from source import Generator2337
        tests = Generator2337.generate()

    if int(challenge_id) == 2554:
        from source import Generator2554
        tests = Generator2554.generate()

    if int(challenge_id) == 1760:
        from source import Generator1760
        tests = Generator1760.generate()

    if int(challenge_id) == 2054:
        from source import Generator2054
        tests = Generator2054.generate()

    if int(challenge_id) == 3152:
        from source import Generator3152
        tests = Generator3152.generate()

    if int(challenge_id) == 2981:
        from source import Generator2981
        tests = Generator2981.generate()

    if int(challenge_id) == 2779:
        from source import Generator2779
        tests = Generator2779.generate()

    if int(challenge_id) == 2558:
        from source import Generator2558
        tests = Generator2558.generate()

    if int(challenge_id) == 2593:
        from source import Generator2593
        tests = Generator2593.generate()

    if int(challenge_id) == 2762:
        from source import Generator2762
        tests = Generator2762.generate()

    if int(challenge_id) == 1792:
        from source import Generator1792
        tests = Generator1792.generate()

    if int(challenge_id) == 3264:
        from source import Generator3264
        tests = Generator3264.generate()

    if int(challenge_id) == 2182:
        from source import Generator2182
        tests = Generator2182.generate()

    if int(challenge_id) == 1475:
        from source import Generator1475
        tests = Generator1475.generate()

    if int(challenge_id) == 769:
        from source import Generator769
        tests = Generator769.generate()

    if int(challenge_id) == 2415:
        from source import Generator2415
        tests = Generator2415.generate()

    if int(challenge_id) == 2872:
        from source import Generator2872
        tests = Generator2872.generate()

    if int(challenge_id) == 2940:
        from source import Generator2940
        tests = Generator2940.generate()

    if int(challenge_id) == 2471:
        from source import Generator2471
        tests = Generator2471.generate()

    if int(challenge_id) == 3203:
        from source import Generator3203
        tests = Generator3203.generate()

    if int(challenge_id) == 515:
        from source import Generator515
        tests = Generator515.generate()

    if int(challenge_id) == 494:
        from source import Generator494
        tests = Generator494.generate()

    if int(challenge_id) == 1014:
        from source import Generator1014
        tests = Generator1014.generate()

    if int(challenge_id) == 689:
        from source import Generator689
        tests = Generator689.generate()

    if int(challenge_id) == 1639:
        from source import Generator1639
        tests = Generator1639.generate()

    if int(challenge_id) == 2466:
        from source import Generator2466
        tests = Generator2466.generate()

    if int(challenge_id) == 983:
        from source import Generator983
        tests = Generator983.generate()

    if int(challenge_id) == 1422:
        from source import Generator1422
        tests = Generator1422.generate()

    if int(challenge_id) == 2559:
        from source import Generator2559
        tests = Generator2559.generate()

    if int(challenge_id) == 2270:
        from source import Generator2270
        tests = Generator2270.generate()

    if int(challenge_id) == 1930:
        from source import Generator1930
        tests = Generator1930.generate()

    if int(challenge_id) == 2381:
        from source import Generator2381
        tests = Generator2381.generate()

    if int(challenge_id) == 1769:
        from source import Generator1769
        tests = Generator1769.generate()

    if int(challenge_id) == 1408:
        from source import Generator1408
        tests = Generator1408.generate()

    if int(challenge_id) == 3042:
        from source import Generator3042
        tests = Generator3042.generate()

    if int(challenge_id) == 2185:
        from source import Generator2185
        tests = Generator2185.generate()

    if int(challenge_id) == 916:
        from source import Generator916
        tests = Generator916.generate()

    if int(challenge_id) == 1400:
        from source import Generator1400
        tests = Generator1400.generate()

    if int(challenge_id) == 2116:
        from source import Generator2116
        tests = Generator2116.generate()

    if int(challenge_id) == 3223:
        from source import Generator3223
        tests = Generator3223.generate()

    if int(challenge_id) == 2657:
        from source import Generator2657
        tests = Generator2657.generate()

    if int(challenge_id) == 2429:
        from source import Generator2429
        tests = Generator2429.generate()

    if int(challenge_id) == 2425:
        from source import Generator2425
        tests = Generator2425.generate()

    if int(challenge_id) == 2683:
        from source import Generator2683
        tests = Generator2683.generate()

    if int(challenge_id) == 1368:
        from source import Generator1368
        tests = Generator1368.generate()

    if int(challenge_id) == 407:
        from source import Generator407
        tests = Generator407.generate()

    if int(challenge_id) == 2661:
        from source import Generator2661
        tests = Generator2661.generate()

    if int(challenge_id) == 2017:
        from source import Generator2017
        tests = Generator2017.generate()

    if int(challenge_id) == 1765:
        from source import Generator1765
        tests = Generator1765.generate()

    if int(challenge_id) == 1267:
        from source import Generator1267
        tests = Generator1267.generate()

    if int(challenge_id) == 802:
        from source import Generator802
        tests = Generator802.generate()

    if int(challenge_id) == 2948:
        from source import Generator2948
        tests = Generator2948.generate()

    if int(challenge_id) == 2127:
        from source import Generator2127
        tests = Generator2127.generate()

    if int(challenge_id) == 1462:
        from source import Generator1462
        tests = Generator1462.generate()

    if int(challenge_id) == 2658:
        from source import Generator2658
        tests = Generator2658.generate()

    if int(challenge_id) == 684:
        from source import Generator684
        tests = Generator684.generate()

    if int(challenge_id) == 2493:
        from source import Generator2493
        tests = Generator2493.generate()

    if int(challenge_id) == 827:
        from source import Generator827
        tests = Generator827.generate()

    if int(challenge_id) == 3151:
        from source import Generator3151
        tests = Generator3151.generate()

    if int(challenge_id) == 1752:
        from source import Generator1752
        tests = Generator1752.generate()

    if int(challenge_id) == 3105:
        from source import Generator3105
        tests = Generator3105.generate()

    if int(challenge_id) == 1800:
        from source import Generator1800
        tests = Generator1800.generate()

    if int(challenge_id) == 1790:
        from source import Generator1790
        tests = Generator1790.generate()

    if int(challenge_id) == 1726:
        from source import Generator1726
        tests = Generator1726.generate()

    if int(challenge_id) == 3160:
        from source import Generator3160
        tests = Generator3160.generate()

    if int(challenge_id) == 2349:
        from source import Generator2349
        tests = Generator2349.generate()

    if int(challenge_id) == 2364:
        from source import Generator2364
        tests = Generator2364.generate()

    if int(challenge_id) == 3174:
        from source import Generator3174
        tests = Generator3174.generate()

    if int(challenge_id) == 1910:
        from source import Generator1910
        tests = Generator1910.generate()

    if int(challenge_id) == 2342:
        from source import Generator2342
        tests = Generator2342.generate()

    if int(challenge_id) == 3066:
        from source import Generator3066
        tests = Generator3066.generate()

    if int(challenge_id) == 1352:
        from source import Generator1352
        tests = Generator1352.generate()

    if int(challenge_id) == 2698:
        from source import Generator2698
        tests = Generator2698.generate()

    if int(challenge_id) == 1718:
        from source import Generator1718
        tests = Generator1718.generate()

    if int(challenge_id) == 1079:
        from source import Generator1079
        tests = Generator1079.generate()

    if int(challenge_id) == 2375:
        from source import Generator2375
        tests = Generator2375.generate()

    if int(challenge_id) == 1415:
        from source import Generator1415
        tests = Generator1415.generate()

    if int(challenge_id) == 1980:
        from source import Generator1980
        tests = Generator1980.generate()

    if int(challenge_id) == 1261:
        from source import Generator1261
        tests = Generator1261.generate()

    if int(challenge_id) == 1028:
        from source import Generator1028
        tests = Generator1028.generate()

    if int(challenge_id) == 889:
        from source import Generator889
        tests = Generator889.generate()

    if int(challenge_id) == 2467:
        from source import Generator2467
        tests = Generator2467.generate()

    if int(challenge_id) == 1524:
        from source import Generator1524
        tests = Generator1524.generate()

    if int(challenge_id) == 1749:
        from source import Generator1749
        tests = Generator1749.generate()

    if int(challenge_id) == 873:
        from source import Generator873
        tests = Generator873.generate()

    if int(challenge_id) == 1092:
        from source import Generator1092
        tests = Generator1092.generate()

    if int(challenge_id) == 2460:
        from source import Generator2460
        tests = Generator2460.generate()

    if int(challenge_id) == 2570:
        from source import Generator2570
        tests = Generator2570.generate()

    if int(challenge_id) == 2161:
        from source import Generator2161
        tests = Generator2161.generate()

    if int(challenge_id) == 1780:
        from source import Generator1780
        tests = Generator1780.generate()

    if int(challenge_id) == 2579:
        from source import Generator2579
        tests = Generator2579.generate()

    if int(challenge_id) == 2965:
        from source import Generator2965
        tests = Generator2965.generate()

    if int(challenge_id) == 2523:
        from source import Generator2523
        tests = Generator2523.generate()

    if int(challenge_id) == 2379:
        from source import Generator2379
        tests = Generator2379.generate()

    if int(challenge_id) == 3208:
        from source import Generator3208
        tests = Generator3208.generate()

    if int(challenge_id) == 3306:
        from source import Generator3306
        tests = Generator3306.generate()

    if int(challenge_id) == 1358:
        from source import Generator1358
        tests = Generator1358.generate()

    if int(challenge_id) == 2529:
        from source import Generator2529
        tests = Generator2529.generate()

    if int(challenge_id) == 3356:
        from source import Generator3356
        tests = Generator3356.generate()

    if int(challenge_id) == 2226:
        from source import Generator2226
        tests = Generator2226.generate()

    if int(challenge_id) == 2560:
        from source import Generator2560
        tests = Generator2560.generate()

    if int(challenge_id) == 2594:
        from source import Generator2594
        tests = Generator2594.generate()

    if int(challenge_id) == 2206:
        from source import Generator2206
        tests = Generator2206.generate()

    if int(challenge_id) == 2401:
        from source import Generator2401
        tests = Generator2401.generate()

    if int(challenge_id) == 3191:
        from source import Generator3191
        tests = Generator3191.generate()

    if int(challenge_id) == 3108:
        from source import Generator3108
        tests = Generator3108.generate()

    if int(challenge_id) == 2115:
        from source import Generator2115
        tests = Generator2115.generate()

    if int(challenge_id) == 2685:
        from source import Generator2685
        tests = Generator2685.generate()

    if int(challenge_id) == 1976:
        from source import Generator1976
        tests = Generator1976.generate()

    if int(challenge_id) == 3169:
        from source import Generator3169
        tests = Generator3169.generate()

    if int(challenge_id) == 3394:
        from source import Generator3394
        tests = Generator3394.generate()

    if int(challenge_id) == 2033:
        from source import Generator2033
        tests = Generator2033.generate()

    if int(challenge_id) == 2780:
        from source import Generator2780
        tests = Generator2780.generate()

    if int(challenge_id) == 2503:
        from source import Generator2503
        tests = Generator2503.generate()

    if int(challenge_id) == 2818:
        from source import Generator2818
        tests = Generator2818.generate()

    if int(challenge_id) == 763:
        from source import Generator763
        tests = Generator763.generate()

    if int(challenge_id) == 2551:
        from source import Generator2551
        tests = Generator2551.generate()

    if int(challenge_id) == 2140:
        from source import Generator2140
        tests = Generator2140.generate()

    if int(challenge_id) == 2873:
        from source import Generator2873
        tests = Generator2873.generate()

    if int(challenge_id) == 2874:
        from source import Generator2874
        tests = Generator2874.generate()

    if int(challenge_id) == 1123:
        from source import Generator1123
        tests = Generator1123.generate()

    if int(challenge_id) == 1863:
        from source import Generator1863
        tests = Generator1863.generate()

    if int(challenge_id) == 368:
        from source import Generator368
        tests = Generator368.generate()

    if int(challenge_id) == 416:
        from source import Generator416
        tests = Generator416.generate()

    if int(challenge_id) == 3396:
        from source import Generator3396
        tests = Generator3396.generate()

    if int(challenge_id) == 3375:
        from source import Generator3375
        tests = Generator3375.generate()

    if int(challenge_id) == 2999:
        from source import Generator2999
        tests = Generator2999.generate()

    if int(challenge_id) == 2843:
        from source import Generator2843
        tests = Generator2843.generate()

    if int(challenge_id) == 3272:
        from source import Generator3272
        tests = Generator3272.generate()

    if int(challenge_id) == 1922:
        from source import Generator1922
        tests = Generator1922.generate()

    if int(challenge_id) == 1534:
        from source import Generator1534
        tests = Generator1534.generate()

    if int(challenge_id) == 2179:
        from source import Generator2179
        tests = Generator2179.generate()

    if int(challenge_id) == 2537:
        from source import Generator2537
        tests = Generator2537.generate()

    if int(challenge_id) == 2176:
        from source import Generator2176
        tests = Generator2176.generate()

    if int(challenge_id) == 38:
        from source import Generator38
        tests = Generator38.generate()

    if int(challenge_id) == 2563:
        from source import Generator2563
        tests = Generator2563.generate()

    if int(challenge_id) == 781:
        from source import Generator781
        tests = Generator781.generate()

    if int(challenge_id) == 2145:
        from source import Generator2145
        tests = Generator2145.generate()

    if int(challenge_id) == 2338:
        from source import Generator2338
        tests = Generator2338.generate()

    if int(challenge_id) == 1399:
        from source import Generator1399
        tests = Generator1399.generate()

    if int(challenge_id) == 2799:
        from source import Generator2799
        tests = Generator2799.generate()

    if int(challenge_id) == 2845:
        from source import Generator2845
        tests = Generator2845.generate()

    if int(challenge_id) == 2444:
        from source import Generator2444
        tests = Generator2444.generate()

    if int(challenge_id) == 3392:
        from source import Generator3392
        tests = Generator3392.generate()

    if int(challenge_id) == 2302:
        from source import Generator2302
        tests = Generator2302.generate()

    if int(challenge_id) == 2962:
        from source import Generator2962
        tests = Generator2962.generate()

    if int(challenge_id) == 1295:
        from source import Generator1295
        tests = Generator1295.generate()

    if int(challenge_id) == 2071:
        from source import Generator2071
        tests = Generator2071.generate()

    if int(challenge_id) == 838:
        from source import Generator838
        tests = Generator838.generate()

    if int(challenge_id) == 1007:
        from source import Generator1007
        tests = Generator1007.generate()

    if int(challenge_id) == 1128:
        from source import Generator1128
        tests = Generator1128.generate()

    if int(challenge_id) == 790:
        from source import Generator790
        tests = Generator790.generate()

    if int(challenge_id) == 1920:
        from source import Generator1920
        tests = Generator1920.generate()

    if int(challenge_id) == 3341:
        from source import Generator3341
        tests = Generator3341.generate()

    if int(challenge_id) == 3342:
        from source import Generator3342
        tests = Generator3342.generate()

    if int(challenge_id) == 3343:
        from source import Generator3343
        tests = Generator3343.generate()

    if int(challenge_id) == 2918:
        from source import Generator2918
        tests = Generator2918.generate()

    if int(challenge_id) == 1550:
        from source import Generator1550
        tests = Generator1550.generate()

    if int(challenge_id) == 2094:
        from source import Generator2094
        tests = Generator2094.generate()

    if int(challenge_id) == 3335:
        from source import Generator3335
        tests = Generator3335.generate()

    if int(challenge_id) == 3337:
        from source import Generator3337
        tests = Generator3337.generate()

    if int(challenge_id) == 2900:
        from source import Generator2900
        tests = Generator2900.generate()

    if int(challenge_id) == 2901:
        from source import Generator2901
        tests = Generator2901.generate()

    if int(challenge_id) == 75:
        from source import Generator75
        tests = Generator75.generate()

    if int(challenge_id) == 1931:
        from source import Generator1931
        tests = Generator1931.generate()

    if int(challenge_id) == 3024:
        from source import Generator3024
        tests = Generator3024.generate()

    if int(challenge_id) == 3355:
        from source import Generator3355
        tests = Generator3355.generate()

    if int(challenge_id) == 73:
        from source import Generator73
        tests = Generator73.generate()

    if int(challenge_id) == 3362:
        from source import Generator3362
        tests = Generator3362.generate()

    if int(challenge_id) == 3068:
        from source import Generator3068
        tests = Generator3068.generate()

    if int(challenge_id) == 2942:
        from source import Generator2942
        tests = Generator2942.generate()

    if int(challenge_id) == 2131:
        from source import Generator2131
        tests = Generator2131.generate()

    if int(challenge_id) == 1857:
        from source import Generator1857
        tests = Generator1857.generate()

    if int(challenge_id) == 2894:
        from source import Generator2894
        tests = Generator2894.generate()

    if int(challenge_id) == 3372:
        from source import Generator3372
        tests = Generator3372.generate()

    if int(challenge_id) == 3373:
        from source import Generator3373
        tests = Generator3373.generate()

    if int(challenge_id) == 2359:
        from source import Generator2359
        tests = Generator2359.generate()

    if int(challenge_id) == 909:
        from source import Generator909
        tests = Generator909.generate()

    if int(challenge_id) == 2929:
        from source import Generator2929
        tests = Generator2929.generate()

    if int(challenge_id) == 135:
        from source import Generator135
        tests = Generator135.generate()

    if int(challenge_id) == 1298:
        from source import Generator1298
        tests = Generator1298.generate()

    if int(challenge_id) == 3403:
        from source import Generator3403
        tests = Generator3403.generate()

    if int(challenge_id) == 1061:
        from source import Generator1061
        tests = Generator1061.generate()

    if int(challenge_id) == 2434:
        from source import Generator2434
        tests = Generator2434.generate()

    if int(challenge_id) == 3170:
        from source import Generator3170
        tests = Generator3170.generate()

    if int(challenge_id) == 386:
        from source import Generator386
        tests = Generator386.generate()

    if int(challenge_id) == 440:
        from source import Generator440
        tests = Generator440.generate()

    if int(challenge_id) == 3442:
        from source import Generator3442
        tests = Generator3442.generate()

    if int(challenge_id) == 3445:
        from source import Generator3445
        tests = Generator3445.generate()

    if int(challenge_id) == 3423:
        from source import Generator3423
        tests = Generator3423.generate()

    if int(challenge_id) == 2616:
        from source import Generator2616
        tests = Generator2616.generate()

    if int(challenge_id) == 2566:
        from source import Generator2566
        tests = Generator2566.generate()

    if int(challenge_id) == 1432:
        from source import Generator1432
        tests = Generator1432.generate()

    if int(challenge_id) == 2016:
        from source import Generator2016
        tests = Generator2016.generate()

    if int(challenge_id) == 3405:
        from source import Generator3405
        tests = Generator3405.generate()

    if int(challenge_id) == 2966:
        from source import Generator2966
        tests = Generator2966.generate()

    if int(challenge_id) == 2294:
        from source import Generator2294
        tests = Generator2294.generate()

    if int(challenge_id) == 3443:
        from source import Generator3443
        tests = Generator3443.generate()

    if int(challenge_id) == 3085:
        from source import Generator3085
        tests = Generator3085.generate()

    if int(challenge_id) == 2138:
        from source import Generator2138
        tests = Generator2138.generate()

    if int(challenge_id) == 2081:
        from source import Generator2081
        tests = Generator2081.generate()

    if int(challenge_id) == 2200:
        from source import Generator2200
        tests = Generator2200.generate()

    if int(challenge_id) == 2040:
        from source import Generator2040
        tests = Generator2040.generate()

    if int(challenge_id) == 2311:
        from source import Generator2311
        tests = Generator2311.generate()

    if int(challenge_id) == 2014:
        from source import Generator2014
        tests = Generator2014.generate()

    if int(challenge_id) == 2099:
        from source import Generator2099
        tests = Generator2099.generate()

    if int(challenge_id) == 1498:
        from source import Generator1498
        tests = Generator1498.generate()

    if int(challenge_id) == 594:
        from source import Generator594
        tests = Generator594.generate()

    if int(challenge_id) == 3330:
        from source import Generator3330
        tests = Generator3330.generate()

    if int(challenge_id) == 3333:
        from source import Generator3333
        tests = Generator3333.generate()

    if int(challenge_id) == 3304:
        from source import Generator3304
        tests = Generator3304.generate()

    if int(challenge_id) == 3307:
        from source import Generator3307
        tests = Generator3307.generate()

    if int(challenge_id) == 1394:
        from source import Generator1394
        tests = Generator1394.generate()

    if int(challenge_id) == 1865:
        from source import Generator1865
        tests = Generator1865.generate()

    if int(challenge_id) == 1353:
        from source import Generator1353
        tests = Generator1353.generate()

    if int(challenge_id) == 1751:
        from source import Generator1751
        tests = Generator1751.generate()

    if int(challenge_id) == 3439:
        from source import Generator3439
        tests = Generator3439.generate()

    if int(challenge_id) == 3440:
        from source import Generator3440
        tests = Generator3440.generate()

    if int(challenge_id) == 2402:
        from source import Generator2402
        tests = Generator2402.generate()

    if int(challenge_id) == 1900:
        from source import Generator1900
        tests = Generator1900.generate()

    if int(challenge_id) == 2410:
        from source import Generator2410
        tests = Generator2410.generate()

    if int(challenge_id) == 1290:
        from source import Generator1290
        tests = Generator1290.generate()

    if int(challenge_id) == 3136:
        from source import Generator3136
        tests = Generator3136.generate()

    if int(challenge_id) == 3201:
        from source import Generator3201
        tests = Generator3201.generate()

    if int(challenge_id) == 3202:
        from source import Generator3202
        tests = Generator3202.generate()

    if int(challenge_id) == 2163:
        from source import Generator2163
        tests = Generator2163.generate()

    if int(challenge_id) == 1233:
        from source import Generator1233
        tests = Generator1233.generate()

    if int(challenge_id) == 1948:
        from source import Generator1948
        tests = Generator1948.generate()

    if int(challenge_id) == 1957:
        from source import Generator1957
        tests = Generator1957.generate()

    if int(challenge_id) == 1695:
        from source import Generator1695
        tests = Generator1695.generate()

    if int(challenge_id) == 1717:
        from source import Generator1717
        tests = Generator1717.generate()

    if int(challenge_id) == 2322:
        from source import Generator2322
        tests = Generator2322.generate()

    if int(challenge_id) == 3487:
        from source import Generator3487
        tests = Generator3487.generate()

    if int(challenge_id) == 3480:
        from source import Generator3480
        tests = Generator3480.generate()

    if int(challenge_id) == 2210:
        from source import Generator2210
        tests = Generator2210.generate()

    if int(challenge_id) == 2044:
        from source import Generator2044
        tests = Generator2044.generate()

    if int(challenge_id) == 2411:
        from source import Generator2411
        tests = Generator2411.generate()

    if int(challenge_id) == 2419:
        from source import Generator2419
        tests = Generator2419.generate()

    if int(challenge_id) == 898:
        from source import Generator898
        tests = Generator898.generate()

    if int(challenge_id) == 118:
        from source import Generator118
        tests = Generator118.generate()

    if int(challenge_id) == 2561:
        from source import Generator2561
        tests = Generator2561.generate()

    if int(challenge_id) == 2106:
        from source import Generator2106
        tests = Generator2106.generate()

    if int(challenge_id) == 904:
        from source import Generator904
        tests = Generator904.generate()

    if int(challenge_id) == 3477:
        from source import Generator3477
        tests = Generator3477.generate()

    if int(challenge_id) == 3479:
        from source import Generator3479
        tests = Generator3479.generate()

    if int(challenge_id) == 3363:
        from source import Generator3363
        tests = Generator3363.generate()

    if int(challenge_id) == 808:
        from source import Generator808
        tests = Generator808.generate()

    if int(challenge_id) == 231:
        from source import Generator231
        tests = Generator231.generate()

    if int(challenge_id) == 869:
        from source import Generator869
        tests = Generator869.generate()

    if int(challenge_id) == 2438:
        from source import Generator2438
        tests = Generator2438.generate()

    if int(challenge_id) == 2787:
        from source import Generator2787
        tests = Generator2787.generate()

    if int(challenge_id) == 326:
        from source import Generator326
        tests = Generator326.generate()

    if int(challenge_id) == 2264:
        from source import Generator2264
        tests = Generator2264.generate()

    if int(challenge_id) == 342:
        from source import Generator342
        tests = Generator342.generate()

    if int(challenge_id) == 1323:
        from source import Generator1323
        tests = Generator1323.generate()

    if int(challenge_id) == 837:
        from source import Generator837
        tests = Generator837.generate()

    if int(challenge_id) == 679:
        from source import Generator679
        tests = Generator679.generate()

    if int(challenge_id) == 2348:
        from source import Generator2348
        tests = Generator2348.generate()

    if int(challenge_id) == 1277:
        from source import Generator1277
        tests = Generator1277.generate()

    if int(challenge_id) == 1504:
        from source import Generator1504
        tests = Generator1504.generate()

    if int(challenge_id) == 3195:
        from source import Generator3195
        tests = Generator3195.generate()

    if int(challenge_id) == 3197:
        from source import Generator3197
        tests = Generator3197.generate()

    if int(challenge_id) == 1493:
        from source import Generator1493
        tests = Generator1493.generate()

    if int(challenge_id) == 498:
        from source import Generator498
        tests = Generator498.generate()

    if int(challenge_id) == 3000:
        from source import Generator3000
        tests = Generator3000.generate()

    if int(challenge_id) == 3459:
        from source import Generator3459
        tests = Generator3459.generate()

    if int(challenge_id) == 3446:
        from source import Generator3446
        tests = Generator3446.generate()

    if int(challenge_id) == 3021:
        from source import Generator3021
        tests = Generator3021.generate()

    if int(challenge_id) == 36:
        from source import Generator36
        tests = Generator36.generate()

    if int(challenge_id) == 37:
        from source import Generator37
        tests = Generator37.generate()

    if int(challenge_id) == 1792:
        from source import Generator1792
        tests = Generator1792.generate()

    if int(challenge_id) == 3025:
        from source import Generator3025
        tests = Generator3025.generate()

    if int(challenge_id) == 3027:
        from source import Generator3027
        tests = Generator3027.generate()

    if int(challenge_id) == 3516:
        from source import Generator3516
        tests = Generator3516.generate()

    if int(challenge_id) == 2749:
        from source import Generator2749
        tests = Generator2749.generate()

    if int(challenge_id) == 3495:
        from source import Generator3495
        tests = Generator3495.generate()

    if int(challenge_id) == 1304:
        from source import Generator1304
        tests = Generator1304.generate()

    if int(challenge_id) == 1317:
        from source import Generator1317
        tests = Generator1317.generate()

    if int(challenge_id) == 2327:
        from source import Generator2327
        tests = Generator2327.generate()

    if int(challenge_id) == 1733:
        from source import Generator1733
        tests = Generator1733.generate()

    if int(challenge_id) == 2785:
        from source import Generator2785
        tests = Generator2785.generate()

    if int(challenge_id) == 3227:
        from source import Generator3227
        tests = Generator3227.generate()

    if int(challenge_id) == 3541:
        from source import Generator3541
        tests = Generator3541.generate()

    if int(challenge_id) == 966:
        from source import Generator966
        tests = Generator966.generate()

    if int(challenge_id) == 1935:
        from source import Generator1935
        tests = Generator1935.generate()

    if int(challenge_id) == 2197:
        from source import Generator2197
        tests = Generator2197.generate()

    if int(challenge_id) == 2353:
        from source import Generator2353
        tests = Generator2353.generate()

    if int(challenge_id) == 3408:
        from source import Generator3408
        tests = Generator3408.generate()

    if int(challenge_id) == 3484:
        from source import Generator3484
        tests = Generator3484.generate()

    if int(challenge_id) == 3508:
        from source import Generator3508
        tests = Generator3508.generate()

    if int(challenge_id) == 1912:
        from source import Generator1912
        tests = Generator1912.generate()

    if int(challenge_id) == 3005:
        from source import Generator3005
        tests = Generator3005.generate()

    if int(challenge_id) == 165:
        from source import Generator165
        tests = Generator165.generate()

    if int(challenge_id) == 166:
        from source import Generator166
        tests = Generator166.generate()

    if int(challenge_id) == 120:
        from source import Generator120
        tests = Generator120.generate()

    if int(challenge_id) == 611:
        from source import Generator611
        tests = Generator611.generate()

    if int(challenge_id) == 812:
        from source import Generator812
        tests = Generator812.generate()

    if int(challenge_id) == 976:
        from source import Generator976
        tests = Generator976.generate()

    if int(challenge_id) == 1039:
        from source import Generator1039
        tests = Generator1039.generate()

    if int(challenge_id) == 2221:
        from source import Generator2221
        tests = Generator2221.generate()

    if int(challenge_id) == 1518:
        from source import Generator1518
        tests = Generator1518.generate()

    if int(challenge_id) == 3100:
        from source import Generator3100
        tests = Generator3100.generate()

    if int(challenge_id) == 407:
        from source import Generator407
        tests = Generator407.generate()

    if int(challenge_id) == 11:
        from source import Generator11
        tests = Generator11.generate()

    if int(challenge_id) == 417:
        from source import Generator417
        tests = Generator417.generate()

    if int(challenge_id) == 778:
        from source import Generator778
        tests = Generator778.generate()

    if int(challenge_id) == 1488:
        from source import Generator1488
        tests = Generator1488.generate()

    if int(challenge_id) == 2300:
        from source import Generator2300
        tests = Generator2300.generate()

    if int(challenge_id) == 3494:
        from source import Generator3494
        tests = Generator3494.generate()

    if int(challenge_id) == 3147:
        from source import Generator3147
        tests = Generator3147.generate()

    if int(challenge_id) == 3186:
        from source import Generator3186
        tests = Generator3186.generate()

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