import random

'''
1482 - Minimum Number of Days to Make m Bouquets
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**9
    min_m = 1
    max_m = 10**6
    min_k = 1

    # Smart Testcases:
    ## Testcase 1
    # n = 5, m = 2, k = 2
    # test = [1, 2, 3, 1, 2]
    test = [1, 2, 3, 1, 2]
    tests.append(test.__str__().replace(' ', '') + "\n2\n2")
    
    ## Testcase 2
    # It's immidiately possible to make m single bouquets
    # n = 90, m = 10, k = 1
    test = [1] * 10 + [random.randint(777, maxval)] * 1
    #random.shuffle(test)
    tests.append(test.__str__().replace(' ', '') + "\n10\n1")
    
    ## Testcase 3
    # It's immidiately possible to make 5 double bouquets
    # n = 90, m = 5, k = 2
    test = []
    for i in range(5):
        test += [1,1,1] + [random.randint(777, 999)] * 5
    tests.append(test.__str__().replace(' ', '') + "\n5\n2")
    
    ## Testcase 4
    # 5er bouquets
    n = 1000
    k = 5
    m = n // 5 - 1
    test = []
    for i in range(n // 5):
        test += [random.randint(1+i, 9+i)] * 5
    tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))


    ## Testcase 4
    # n = 40000, m = 10000, k = 5
    # test = [random.randint(minval, maxval) for _ in range(n)]
    test = [random.randint(minval, 999) for _ in range(40000)]
    tests.append(test.__str__().replace(' ', '') + "\n1200\n5")
    
    ## Testcase 5
    # n = 10000, m = 10000, k = 10000
    # test = [random.randint(minval, maxval) for _ in range(n)]
    test = [random.randint(minval, 99) for _ in range(10000)]
    tests.append(test.__str__().replace(' ', '') + "\n10000\n10000")
    
    ## Testcase 6
    # Just one large bouquet
    n = max_num
    k = n
    m = 1
    test = [random.randint(1, 9) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))

    ## Testcase 7
    # Many 2 bouquets
    n = max_num
    k = 2
    m = n // 2
    test = [42 for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))

    ## Testcase 8
    # Many 7 bouquets
    n = max_num
    k = 7
    m = max_num // 70
    test = [random.randint(100, n) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))


    # Random Testcases
    for n in [min_num, 4321, 10000, 20000, max_num]:
        max_k = n
        k = random.randint(min_k, max_k)
        m = n // k
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))

   # Random Testcases
    for n in [min_num, 4321, 10000, 20000, max_num]:
        max_k = min(n, 20)
        k = random.randint(min_k, max_k)
        m = n // k
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', '') + "\n" + str(m) + "\n" + str(k))

  
    return '''
'''.join(tests)
