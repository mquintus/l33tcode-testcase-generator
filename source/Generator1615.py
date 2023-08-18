import random


def generate() -> str:
    tests = []
    max_length = 100

    '''
    First test case:
    Connect all cities with index 0, 5, 10, 15, ...
    with cities with index 2, 4, 6, 8, 10, ...
    Keep order (a smaller b)
    '''
    n = max_length
    test = []
    for i in range(n-1):
        if i % 5 == 0:
            test.extend([[i, j] for j in range(i+1, n) if j % 2 == 0])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Second test case:
    Connect all cities with index 0, 4, 8, 12, ...
    with cities 0, 5, 10, 15, ...
    Reverse order (a greater b)
    '''
    test = []
    for i in range(n-1):
        if i % 4 == 0:
            test.extend([[j, i] for j in range(i+1, n) if j % 5 == 0])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Third test case:
    Connect all cities with index 0, 5, 10, 15, ...
    with cities with indexes of different patters (modulo + 3) == 0:
    city 0 is connected to 3, 6, 9, 12, 15, ...
    city 1 is connected to 4, 8, 12, 16, ...
    ...
    city 45 is connected to 48, 96
    ...
    city 96 is connected to 99
    Keep order (a smaller b)
    '''
    n = max_length
    test = []
    for i in range(n-1):
        if i % 5 == 0:
            test.extend([[i, j] for j in range(i+1, n) if j % (i+3) == 0])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Fourth test case:
    Each town is connected randomly.
    Keep order (a smaller b)
    '''
    n = max_length
    test = []
    for i in range(n-1):
        test.extend([[i, j] for j in range(i+1, n) if random.randint(0, 1) == 0])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Edge case: Hundred unconnected cities
    '''
    n = max_length
    test = []
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Edge case: Two fully connected cities
    '''
    n = 2
    test = []
    for i in range(n-1):
        test.extend([[j, i] for j in range(i+1, n)])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Edge case: Three fully connected cities
    '''
    n = 3
    test = []
    for i in range(n-1):
        test.extend([[j, i] for j in range(i+1, n)])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    '''
    Edge case: Four fully connected cities
    '''
    n = 4
    test = []
    for i in range(n-1):
        test.extend([[j, i] for j in range(i+1, n)])
    tests.append(str(n) + "\n" + test.__str__())
    tests[-1] = tests[-1].replace(" ", "")

    return "\n".join(tests)
