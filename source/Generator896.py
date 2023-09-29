import random

'''
896 - Monotonic Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100000
    minval = -100000
    maxval = 100000

    n = 100
    test = [i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 99
    test = [n-i-1 for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 50
    test = [i * 2 + 1 for i in range(n)]
    test2 = [i * 2 for i in range(n)]
    test.extend(test2)
    tests.append(test.__str__().replace(' ', ''))

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = min_num
    test = [i for i in range(n)]
    test.append(n - 1)
    tests.append(test.__str__().replace(' ', ''))

    n = max_num - 2
    test = [i for i in range(n)]
    test.append(n - 1)
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
