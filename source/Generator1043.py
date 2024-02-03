import random

'''
1043 - Partition Array for Maximum Sum
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 500
    minval = 0
    maxval = 500

    k = 1
    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + '\n' + str(k))

    k = 2
    n = 100
    test = [0 if i % 4 in [1,2] else random.randint(minval, maxval) for i in range(n)]
    tests.append(test.__str__().replace(' ', '') + '\n' + str(k))

    for k in [1, 10, random.randint(400, 500)]:
        n = max_num
        test = [i for i in range(n // 2)] + [i for i in range(n // 2, 0, -1)]
        tests.append(test.__str__().replace(' ', '') + '\n' + str(k))

        n = max_num
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', '') + '\n' + str(k))

    return '''
'''.join(tests)
