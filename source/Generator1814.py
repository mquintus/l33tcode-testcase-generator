import random

'''
1814 - Count Nice Pairs in an Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 0
    maxval = 10**9
    maxval_soft = 10**4

    for n in [min_num, 20, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

        test = [random.randint(minval, maxval_soft) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    for n in [2000, max_num]:
        test = [random.randint(minval, maxval_soft)] * n
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
