import random

'''
198 - House Robber
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 0
    maxval = 400

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 2 - Increasing sequence
    n = max_num
    test = [minval + i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 3 - Decreasing sequence
    n = max_num
    test = [maxval - i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 4 - Alternating sequence
    n = max_num
    test = [minval + i if i % 2 == 0 else maxval - i - random.randint(1, 10) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 5 - Up and down sequence
    n = max_num
    test = [minval + i + random.randint(1, 3) for i in range(n // 2)]
    test.extend([n//2 - i + random.randint(1, 3) for i in range(n // 2)])
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 6 - Down and up sequence
    n = max_num
    offset = random.randint(1, 10)
    test = [maxval - i - offset for i in range(n // 2)]
    test.extend([minval + i + offset for i in range(n // 2)])
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 7 - Random sequence
    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 8 - High value houses are grouped together
    n = max_num
    test = [maxval - random.randint(0, 10) if i % 4 in (1,2) else minval + random.randint(0, 10) for i in range(n) ]
    #test.sort()
    test = test[::-1]
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
