import random

'''
1652 - Defuse the Bomb
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100

    n = random.randint(5, 10)
    code = 0
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + code.__str__())

    for n in [min_num, 2, 23, 42, 73, 99]:
        code = random.randint(-n+1, n-1)
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', '') + "\n" + code.__str__())

    n = max_num
    code = max_num-1
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + code.__str__())

    return '''
'''.join(tests)
