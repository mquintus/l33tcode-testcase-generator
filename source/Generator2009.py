import random

'''
2009 - Minimum Number of Operations to Make Array Continuous
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**9

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    i = random.randint(minval, maxval)
    test = [i + 42, i + 44]
    tests.append(test.__str__().replace(' ', ''))

    test = [i + 42, i + 43]
    tests.append(test.__str__().replace(' ', ''))

    n = 10
    test = [maxval - (i * 2) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 20
    test = [100 - i * 3 for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 20
    test = [minval + i // 2 for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [1000 + i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [int(random.randint(minval, maxval - n*3) + (i * 1.8)) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
