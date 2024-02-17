import random

'''
1642 - Furthest Building You Can Reach
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**6


    second = False
    for n in [20, 10**3]:
        first = True
        # Testcase 1 - The distance between buildings is increasing
        distances = sorted([random.randint(minval, 10) for _ in range(n)])
        heights = [10000 * random.randint(1, 9)]
        up = -1
        for d in distances:
            heights.append(min(maxval, max(1, heights[-1] + d*up)))
            if not second:
                up *= -1
        bricks = random.randint(min_num, max_num)
        ladders = random.randint(min_num, len(heights)-1) // 2
        if first:
            bricks = ladders = 0
            first = False
            second = True
        tests.append(f'{heights}\n{bricks}\n{ladders}'.replace(' ', ''))

        # Testcase 2 - The distance between buildings is decreasing
        distances = sorted([random.randint(minval, maxval) for _ in range(n )])[::-1]
        heights = [10000 * random.randint(1, 9)]
        up = 1
        for d in distances:
            heights.append(min(maxval, max(1, heights[-1] + d*up)))
            up *= -1
        bricks = random.randint(min_num, max_num)
        ladders = random.randint(min_num, len(heights)-1)
        tests.append(f'{heights}\n{bricks}\n{ladders}'.replace(' ', ''))

        # Testcase 3 - The distance between buildings is random
        # but the bricks sum up to the actual distance - the max distance
        # and we have only one ladder
        distances = [random.randint(minval, maxval) for _ in range(n )]
        heights = [10000 * random.randint(1, 9)]
        up = -1
        actual_distances = 0
        max_distance = 0
        for d in distances:
            heights.append(min(maxval, max(1, heights[-1] + d*up)))
            if up == 1:
                actual_distances += d
                max_distance = max(max_distance, d)
            up *= -1
        bricks = actual_distances - max_distance
        ladders = 1
        tests.append(f'{heights}\n{bricks}\n{ladders}'.replace(' ', ''))

        # Testcase 4 - Up up down down left right left right B A Start
        up = 1
        distances = sorted([random.randint(minval, maxval) for _ in range(n //5)])[::-1]
        distances.extend(sorted([random.randint(minval, maxval) for _ in range(n //5)]))
        distances.extend(sorted([random.randint(minval, maxval) for _ in range(n //5)][::-1]))
        distances.extend(sorted([random.randint(minval, maxval) for _ in range(n //5)]))
        heights = [10000 * random.randint(1, 9)]
        for d in distances:
            heights.append(min(maxval, max(1, heights[-1] + d*up)))
            up *= -1
        bricks = random.randint(min_num, max_num)
        ladders = random.randint(min_num, len(heights)-1)
        tests.append(f'{heights}\n{bricks}\n{ladders}'.replace(' ', ''))

    return '''
'''.join(tests)
