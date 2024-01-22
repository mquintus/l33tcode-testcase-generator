import random

'''
645 - Set Mismatch
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**4

    #for n in [min_num, 3, 10, 10, 10, 10, 1000, max_num]:
    for n in [min_num, 3, 10, 100, 1000, 1000, max_num, max_num]:
        test = [i for i in range(1, n+1)]
        duplicate = random.randint(1, n)
        duplicate_position = duplicate - 1
        while duplicate_position + 1 == duplicate:
            duplicate_position = random.randint(0, n-1)
        test[duplicate_position] = duplicate
        random.shuffle(test)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
