import random

'''
446 - Arithmetic Slices II - Subsequence
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = -1000
    maxval = 1000

    # Edge case 1 - Only one element
    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 2 - A sequence of the same number
    n = 24
    test = [random.randint(minval, maxval)] * n
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 3 - A sequence of increasing values
    n = max_num
    difference = random.randint(minval, maxval)
    test = [difference * i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 4 - A mix of same numbers and sequence of increasing values
    n = max_num
    difference = random.randint(minval, maxval)
    test = [difference * i for i in range(n // 4)]
    test.extend([1 + difference * i for i in range(n // 4)])
    test.extend([2 + difference * i for i in range(n // 4)])
    test.extend([difference * i for i in range(n // 4)])
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 5 - Three alternating values that form a sequence
    n = 30
    basis = random.randint(minval, maxval)
    test = [basis * ((i % 3) + 1) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 6 - Random values
    n = max_num
    test = [random.randint(minval, maxval) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 7 - Numbers double
    test = [2**i for i in range(30)]
    test.extend([3**i for i in range(10)])
    tests.append(test.__str__().replace(' ', ''))

    # Edge case 8 - Numbers half
    start = 2**30
    test = []
    for i in range(30):
        test.append(start)
        start //= 2

    start = 2**30 - 1000
    for i in range(30):
        test.append(start)
        start //= 2
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
