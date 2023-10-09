import random

'''
34 - Find First and Last Position of Element in Sorted Array
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 10**5
    minval = -1000000000
    maxval = 1000000000

    n = min_num
    target = 42
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))
    
    n = 10
    mean = random.randint(-10, 10)
    for target in [-1, 0, 2]:
      target += mean
      test = [mean for _ in range(n)]
      test = [-1 + mean, *test, 1 + mean]
      tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))
    
    test = [1,2,2,2,2,3,4,5,5,5,5,6,7,8,9,10,11,12,12,12,12,12,13]
    target = 2
    tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))

    n = max_num
    target = 42
    test = [42 for _ in range(n)]
    tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))

    n = max_num
    target = 42
    test = [0 for _ in range(n)]
    tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))
    
    n = max_num
    test = sorted([random.randint(minval, maxval) for _ in range(n)])
    target = test[-1]
    tests.append((test.__str__() + "\n" + target.__str__()).replace(' ', ''))

    return '''
'''.join(tests)
