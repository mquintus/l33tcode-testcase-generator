import random

'''
713 - Subarray Product Less Than K
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 3 * 10**4
    minval = 1
    maxval = 1000

    # Testcase 1 - minimal testcase
    n = min_num
    k = minval
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 2 - minimal testcase
    n = 20
    k = minval
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 3 - it's all the same number
    n = 20
    test = [random.randint(2, 5)] * n
    k = maxval
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 4 - no solutions
    n = 20
    test = [random.randint(2, 5) for _ in range(n)]
    k = 1
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 5 - random values
    n = 40
    test = [random.randint(1, 10) for _ in range(n)]
    k = 1000000
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 6 - random values
    n = 120
    test = [130 - i for i in range(n)]
    k = 1000000 - random.randint(1, 100000)
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 7 - maximal testcase
    n = max_num
    k = minval
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # Testcase 8 - maximal testcase
    n = max_num
    k = maxval
    test = [1] * n
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    return '''
'''.join(tests)
