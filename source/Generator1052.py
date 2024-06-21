import random

'''
1052 - Grumpy Bookstore Owner
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 2*10**4
    minval = 0
    maxval = 999
    
    # Testcase 1 - All days are grumpy
    n = 50
    customers = [random.randint(minval, maxval) for _ in range(n)]
    grumpy = [1 for _ in range(n)]
    minutes = random.randint(1, n)
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    # Testcase 2 - No days are grumpy
    n = 50
    customers = [random.randint(minval, maxval) for _ in range(n)]
    grumpy = [0 for _ in range(n)]
    minutes = random.randint(1, n)
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    # Testcase 3 - All days are grumpy but no minutes
    n = 50
    customers = [random.randint(minval, maxval) for _ in range(n)]
    grumpy = [1 for _ in range(n)]
    minutes = 1
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    ## Testcase 4 - Random values, max length
    n = max_num
    customers = [random.randint(minval, maxval) for _ in range(n)]
    grumpy = [random.choice([0,1]) for _ in range(n)]
    minutes = random.randint(n // 3, (2 * n) // 3)
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    # Testcase 5 - Increasing customers, alternating grumpiness
    n = max_num
    customers = [int(i*1000/n) for i in range(1, n+1)]
    grumpy = [random.choice([0,1]) for _ in range(n)]
    minutes = random.randint(n // 7, (2 * n) // 7)
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    # Testcase 6 - Modulo customers, reverse, alternating grumpiness
    n = max_num
    customers = [1+((-i)%42)+random.randint(0,5) for i in range(1, n+1)]
    grumpy = [random.choice([0,1]) for _ in range(n)]
    minutes = random.randint(n // 7, (2 * n) // 7)
    tests.append(f'{customers}\n{grumpy}\n{minutes}'.replace(" ", ""))

    return '''
'''.join(tests)
