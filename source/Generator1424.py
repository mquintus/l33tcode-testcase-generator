import random

'''
1424 - Diagonal Traverse II
'''
def generate() -> str:
    tests = []
    min_rows = 1
    max_rows = 10**4
    min_cols = 1
    max_cols = 10**4
    minval = 1
    maxval = 1000
    max_cells = 10**5 // 2

    softmax = random.randint(10, 30)

    testcases = [
        [min_cols],
        [softmax for i in range(min_rows)],
        [1 for _ in range(softmax)],
        list(range(1, softmax)),
        list(range(softmax, 0, -1)),
        [random.randint(min_cols, softmax) for _ in range(softmax)],
        [max_cols, max_cols // random.randint(20,50), max_cols // random.randint(2,5)],
        [random.randint(1,3) for _ in range(max_rows)]
    ]

    for rows in testcases:
        test = []
        for cols in rows:
            test.append([random.randint(minval, min(i+100, maxval)) for i in range(cols)])
        tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
