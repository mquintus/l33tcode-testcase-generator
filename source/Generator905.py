import random

'''
905 - Sort Array By Parity
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5000
    minval = 0
    maxval = 5000

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



    return '''
'''.join(tests)
