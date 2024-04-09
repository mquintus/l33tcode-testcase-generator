import random

'''
2073 - Time Needed to Buy Tickets
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100


    for n in [min_num, min_num+1]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        k = random.randint(0, n-1)
        tests.append(test.__str__().replace(' ', '')+"\n"+str(k))

    n = max_num - 2
    test = [i+1 for i in range(n)]
    k = n - 1
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))

    n = max_num - 1
    test = [max(1,n-i-1) for i in range(n)]
    k = n - 1
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))
    
    n = max_num - 2
    test = []
    for i in range(n//2):
        test.append(n - 10 - i)
        test.append(    10 + i)
    k = n - 2
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))

    n = max_num - 1
    test = []
    for i in range(n//2):
        test.append(    10 + i)
        test.append(n - 10 - i)
    k = n - 2
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))

    n = max_num
    test = [maxval for _ in range(n)]
    k = n - 1
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))
        
    
    return '''
'''.join(tests)
