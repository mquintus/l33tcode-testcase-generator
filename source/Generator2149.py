import random

'''
2149 - Rearrange Array Elements by Sign
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1
    maxval = 10**4

    for n in [min_num, 4, 6, 40, 500, 6000, 70000, max_num]:
        test = [-1 * random.randint(minval, maxval) for _ in range(n // 2)]
        test.extend([random.randint(minval, maxval) for _ in range(n // 2)])
        random.shuffle(test)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
