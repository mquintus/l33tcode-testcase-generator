import random

'''
1552 - Magnetic Force Between Two Balls
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5

    n = max_num
    test = [int(((1 + i)*10) ** 1.1) for i in range(n)]
    #random.shuffle(test)
    m = max_num // 7
    tests.append(test.__str__().replace(' ', '') + "\n" + str(m))

    for n in [min_num, 1000, max_num]:
        for m in [2,3,max_num//7]:
            if m > n:
                continue
            test = [20 * (i+1) + random.randint(-9, 9) for i in range(n)]
            random.shuffle(test)
            tests.append(test.__str__().replace(' ', '') + "\n" + str(m))
            #max_val *= 10
    
    return '''
'''.join(tests)
