import random

'''
3075 - Maximize Happiness of Selected Children
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**8

    for n in [min_num, min_num+1, max_num//10, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        k = random.randint(1,n)
        tests.append(test.__str__().replace(' ', '')+f"\n{k}")

        test = [i * 107 for i in range(1,n+1)]
        random.shuffle(test)
        k = random.randint(1,n)
        tests.append(test.__str__().replace(' ', '')+f"\n{k}")

    return '''
'''.join(tests)
