import random

'''
1512 - Number of Good Pairs
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # all the same
    match = random.randint(minval, maxval)
    test = [match] * max_num
    tests.append(test.__str__().replace(' ', ''))

    # all the max
    match = maxval
    test = [match] * max_num
    tests.append(test.__str__().replace(' ', ''))

    # only pairs
    test = []
    for _ in range(max_num // 2):
        match = random.randint(minval, maxval)
        test.extend([match] * 2)
    tests.append(test.__str__().replace(' ', ''))

    # in reverse
    test = test[::-1]
    tests.append(test.__str__().replace(' ', ''))

    # in shuffled
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', ''))

    # all different
    test = [i for i in range(minval, maxval + 1)]
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
