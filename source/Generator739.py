import random

'''
739 - Daily Temperatures
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 30
    maxval = 100

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = min_num + 1
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    test = [random.randint(minval, maxval) for _ in range(30, 101)]
    tests.append(test.__str__().replace(' ', ''))

    test = [random.randint(minval, maxval) for _ in range(100, 29, -1)]
    tests.append(test.__str__().replace(' ', ''))

    n = 1000
    test = [minval + (i % (maxval - minval)) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 1000
    test = [minval + (i % (maxval - minval)) for i in range(n, 0, -1)]
    tests.append(test.__str__().replace(' ', ''))

    n = 2000
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
