import random

'''
2870 - Minimum Number of Operations to Make Array Empty
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1

    for n in [min_num, 100, 10000, max_num]:
        maxval = n // 2
        test = []
        while len(test) < n:
            multiplier = random.randint(2, n)
            multiplier = min(multiplier, n - len(test))
            multiplier = max(multiplier, 1)
            #print(multiplier)
            test.extend([random.randint(minval, maxval)] * multiplier)
        tests.append(test.__str__().replace(' ', ''))

        test = []
        while len(test) < n - 1:
            multiplier = random.randint(2, n)
            multiplier = min(multiplier, n - len(test) - 1)
            multiplier = max(multiplier, 1)
            test.extend([random.randint(minval, maxval)] * multiplier)
        test.append(maxval + 1)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
