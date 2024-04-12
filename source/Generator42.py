import random

'''
42 - Trapping Rain Water
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 2 * 10**4 - 10
    minval = 0
    maxval = 100000

    n = random.randint(min_num, 3)
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    n = 3
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 0 - Minimal Testcase
    # Testcase 1 - Monotonic Increasing
    # Testcase 2 - Monotonic Decreasing
    # Testcase 3 - Two alternating values
    # Testcase 4 - The same value
    # Testcase 5 - Overlapping increase and decrease
    # Testcase 7 - Random Values

    n = max_num
    test = [50]
    for i in range(n):
      test.append(test[-1] + random.randint(0,2))
    tests.append(test.__str__().replace(' ', ''))

    test = []
    curr = n * 4
    for i in range(n):
      test.append(curr - random.randint(0,4))
      curr = test[-1]
    tests.append(test.__str__().replace(' ', ''))
    
    test = []
    one = random.randint(1,999)
    two = random.randint(1,999)
    for i in range(n//2):
      test.append(one)
      test.append(two)
    tests.append(test.__str__().replace(' ', ''))
    
    test = []
    one = random.randint(1,99)
    for i in range(n):
      test.append(one)
    tests.append(test.__str__().replace(' ', ''))
    
    test = []
    one = random.randint(maxval-2000, maxval-1000)
    for i in range(n // 2):
      one -= random.randint(0,10)
      test.append(one)
    for i in range(n // 2):
      one += random.randint(0,10)
      test.append(one)
    tests.append(test.__str__().replace(' ', ''))
    
    test = []
    one = random.randint(n*4, n*5)
    two = random.randint(0, 100)
    for i in range(n // 2):
      one -= random.randint(2,3)
      two += random.randint(2,5)
      two = min(maxval, two)
      one = max(minval, one)
      test.append(one)
      test.append(two)
    tests.append(test.__str__().replace(' ', ''))


    # Testcase 7
    n = max_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
