import random

'''
1631. Path With Minimum Effort
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 10**6


    m = 1
    n = 2
    matrix = [[random.randint(minval,maxval) for _ in range(m)] for _ in range(n)]
    tests.append(matrix.__str__().replace(' ', ''))

    m = 2
    n = 1
    matrix = [[random.randint(minval,maxval) for _ in range(m)] for _ in range(n)]
    tests.append(matrix.__str__().replace(' ', ''))

    m = 1
    n = 1
    matrix = [[random.randint(minval,maxval) for _ in range(m)] for _ in range(n)]
    tests.append(matrix.__str__().replace(' ', ''))

    m = max_num
    n = max_num
    matrix = [[random.randint(minval,maxval) for _ in range(m)] for _ in range(n)]
    tests.append(matrix.__str__().replace(' ', ''))

    for i in range(4):
        m = max_num // (i + 2)
        n = max_num // (i + 1)
        matrix = [[random.randint(minval,maxval) for _ in range(m)] for _ in range(n)]
        tests.append(matrix.__str__().replace(' ', ''))

    return "\n".join(tests)
