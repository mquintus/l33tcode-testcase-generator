import random

'''
977 - Squares of a Sorted Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    minval = -10000
    maxval = 10000

    # Edgecases:
    # 1. Only 1 element
    # 2. Only 2 elements
    # 3. Only negative elements
    # 4. Only positive elements
    # 5. Random elements
    # 6. Only identical elements
    # 7. Low variance of elements
    # 8. High number of elements

    # 1. Only one element
    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    test.sort()
    tests.append(test.__str__().replace(' ', ''))

    # 2. Only two elements
    n = 2
    test = [random.randint(minval, maxval) for _ in range(n)]
    test.sort()
    tests.append(test.__str__().replace(' ', ''))

    # 3. Only negative elements
    n = 50
    test = []
    for i in range(n):
        test.append(random.randint(minval, -1))
    test.sort()
    tests.append(test.__str__().replace(' ', ''))

    # 4. Only positive elements
    n = 50
    test = []
    for i in range(n):
        test.append(random.randint(1, maxval))
    test.sort()
    tests.append(test.__str__().replace(' ', ''))

    # 5. Random elements
    n = 50
    test = sorted([random.randint(minval, maxval) for _ in range(n)])
    tests.append(test.__str__().replace(' ', ''))

    # 6. Only identical elements
    n = 50
    test = sorted([random.choice([random.randint(minval, maxval), random.randint(minval, maxval), 0, 1, -1])] * n)
    tests.append(test.__str__().replace(' ', ''))

    # 7. Low variance of elements
    n = 50
    low_variance = [random.randint(minval, maxval), random.randint(minval, maxval), 0, 1, -1]
    test = sorted([random.choice(low_variance) for i in range(n)])
    tests.append(test.__str__().replace(' ', ''))

    # 8. Max number of elements
    n = 10000
    test = sorted([random.randint(-19, 9) for _ in range(n)])
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
