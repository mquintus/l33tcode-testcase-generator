import random

'''
368 - Largest Divisible Subset
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = 1
    maxval = 2 * 10**9

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))


    n = random.randint(20, 100)
    test = [max(minval, i * 2) for i in range(n)]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    n = random.randint(20, 100)
    test = [max(minval, i * 2) for i in range(int(n // 2))]
    test += [max(minval, i * 3) for i in range(1, int(n // 2))]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    n = random.randint(20, 100)
    test = [max(minval, i * 2) for i in range(int(n // 3))]
    test += [max(minval, i * 3) for i in range(1,int(n // 3))]
    test += [max(minval, i * 5) for i in range(1,int(n // 3))]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    n = random.randint(120, 240)
    test = [1]
    for i in range(n):
        if random.randint(0, 10) == 0:
            next = test[-1] * 2
        else:
            next = test[-1] * random.randint(3, 7)
        if next > maxval:
            next = random.randint(minval, maxval)
        test.append(next)
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    n = 1000
    max_value = 100000
    j = 1
    i = 0
    is_prime = [True] * (max_value)
    test = []
    while i < n and j < max_value:
        j += 1
        if is_prime[j]:
            i += 1
            test.append(j)
            for k in range(j, max_value, j):
                is_prime[k] = False
    tests.append(test.__str__().replace(' ', ''))

    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    test = [max(minval, i * 7) for i in range(5,int(n // 3))]
    test += [max(minval, i * 9) for i in range(3,int(n // 3))]
    test += [max(minval, i * 11) for i in range(1,int(n // 3))]
    test = list(set(test))
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
