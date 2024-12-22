import random

'''
2940 - Find Building Where Alice and Bob Can Meet
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5 * 10**4
    minval = 1
    maxval = 10**9

    # Testcase 1:
    # All increasing heights
    heights = [i for i in range(1, max_num+1)]
    queries = []
    for _ in range(max_num):
        start = random.randint(0, max_num-1)
        end = random.randint(start, max_num-1)
        queries.append([start,end])
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2:
    # All decreasing heights
    heights = [i for i in range(max_num, 0, -1)]
    queries = []
    for _ in range(max_num):
        start = random.randint(0, max_num-1)
        end = random.randint(start, max_num-1)
        queries.append([start,end])
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))


    # Testcase 3:
    # Bob starts at the left, Alice starts at the right
    # Bob is on the highest building, ALice is on a slightly higher building
    # And in between there are buildings of decreasing height
    heights = [i for i in range(max_num, 0, -1)]
    heights[max_num-1] = 2
    queries = [[max_num-1, 0] for _ in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 4:
    # Bob starts at the left, Alice starts at second building from the left
    # Bob is on a high building, ALice is on a very low building
    # And after them are buildings of increasing height
    heights = [i for i in range(1, max_num+1)]
    heights[0] = max_num - 10
    heights[1] = max_num - 11
    queries = [[1, 0] for _ in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 5:
    # Bob starts at the left, Alice starts at second building from the left
    # Bob is on a high building, ALice is on a slightly higher building
    # And after them are buildings of decreasing height
    heights = [i for i in range(1, max_num+1)[::-1]]
    heights[0] = max_num + 10
    heights[1] = max_num + 11
    queries = [[1, 0] for _ in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 6:
    # Bob starts at the left, Alice starts at second building from the left
    # Bob is on a high building, ALice is on a slightly higher building
    # And after them are buildings of decreasing height
    heights = [i for i in range(1, max_num+1)[::-1]]
    heights[0] = max_num + 11
    heights[1] = max_num + 10
    queries = [[i%10, 0] for i in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))
    
    # Testcase 7:
    # Total Randomness
    heights = [random.randint(minval, maxval) for i in range(1, max_num+1)]
    queries = [[random.randint(0, max_num-1), random.randint(0, max_num-1)] for _ in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 8:
    # V Shape
    heights = [i for i in range(1, max_num//2)] + [i for i in range(1, max_num//2)[::-1]]
    queries = [[random.randint(0, max_num-3), random.randint(0, max_num-3)] for _ in range(max_num)]
    test = f"{heights}\n{queries}"
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
