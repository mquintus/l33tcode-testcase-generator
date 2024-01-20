import random

'''
907 - Sum of Subarray Minimums
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 3 * 10**4
    minval = 1
    maxval = 3 * 10**4

    for n in [min_num, 100, 1000]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(1, 9) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    test = [random.randint(1, 99) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    test = [random.randint(1, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
