import random

'''
1838 - Frequency of the Most Frequent Element
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**5

    # stepsize: First 2 elements not included
    # stepsize: Last 2 elements not included
    k = random.randint(20,70)
    test = [random.randint(1, 100),
            random.randint(500, 600),
            *([random.randint(1000, 1000)] * 2),
            random.randint(10000, 13000),
            random.randint(20000, 23000),
            ]
    test[3] += random.randint(10, 20)
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))


    for n in [min_num,2,3,1000,max_num]:
        k = random.randint(1, max_num)
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # sequence all the same
    k = 1
    test = [random.randint(minval, maxval)] * n
    test[3] += 1
    test[99997] += 1
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    # sequence all different but reachable as much as possible
    k = max_num
    test = [i for i in range(1, n)]
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    return '''
'''.join(tests)
