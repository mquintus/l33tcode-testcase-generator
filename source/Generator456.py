import random

'''
456 - 132 Pattern
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200000
    minval = int(-1e9)
    maxval = int(1e9)

    n = min_num
    test = [random.randint(minval, maxval)]
    tests.append(test.__str__().replace(' ', ''))

    n = 50
    test = [n-i-1 for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 50
    test = [i * 2 + 1 for i in range(n)]
    test2 = [i * 2 for i in range(n)]
    test.extend(test2)
    tests.append(test.__str__().replace(' ', ''))

    test = [1,1,0,1,0,1,0,1,0,0,0,1,1]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(1, 2) * 2 for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 20
    test = [i for i in range(n)]
    test.append(n - 2)
    tests.append(test.__str__().replace(' ', ''))

    n = 20
    test = [i + 100 for i in range(n)]
    test.append(n - 2)
    tests.append(test.__str__().replace(' ', ''))

    n = max_num - 2
    test = [i // 2 for i in range(n)]
    test.append((n // 2) - 2)
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
