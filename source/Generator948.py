import random

'''
948 - Bag of Tokens
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 1000
    minval = 0
    maxval = 100

    # Edgecases:
    # 1. Zero elements, lots of power
    # 2. Zero elements, no power
    # 3. One element, lots of power
    # 4. One element, no power
    # 5. Two elements, lots of power
    # 6. Two elements, no power

    for n in [min_num, 1, 2, 3]:
        for power in range(0, n+1):
            tokens = [max(minval, power - 1 + i) for i in range(n)]
            test = tokens.__str__().replace(' ', '')
            test += f"\n{power}"
            tests.append(test)

    offset = random.randint(minval + maxval // 2, maxval)
    n = max_num
    for power in [1, n]:
        tokens = [offset + i for i in range(n)]
        test = tokens.__str__().replace(' ', '')
        test += f"\n{power}"
        tests.append(test)

    n = max_num
    for power in [1, n]:
        tokens = [random.randint(1,99) for i in range(n)]
        test = tokens.__str__().replace(' ', '')
        test += f"\n{power}"
        tests.append(test)

    return '''
'''.join(tests)
