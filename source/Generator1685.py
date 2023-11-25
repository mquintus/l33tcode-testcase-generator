import random

'''
1685 - Sum of Absolute Differences in a Sorted Array
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1
    maxval = 10**4

    for n in [min_num, 10, 10_000, max_num]:
        for strategy in ['random', 'identical']:
            if strategy == 'random':
                test = [random.randint(minval, maxval) for _ in range(n)]
                test.sort()
            elif strategy == 'identical':
                test = [random.randint(minval, maxval)] * n
            tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
