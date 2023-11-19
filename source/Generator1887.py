import random

'''
1887 - Reduction Operations to Make the Array Elements Equal
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    minval = 1
    maxval = 10**4

    for n in [min_num, 3, max_num, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    for n in [2, 3, max_num, max_num]:
        test = []
        test.extend([random.randint(minval, maxval)] * (n // 2))
        test.extend([random.randint(minval, maxval)] * (n // 2))
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
