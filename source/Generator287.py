import random

'''
287 - Find the Duplicate Number
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5

    for n in [min_num, 3, 4, 5, 99, 100, max_num - 1, max_num]:
        test = [i for i in range(1, n)]
        random.shuffle(test)

        duplicate_number = random.randint(1, n-1)
        freq = 2
        if random.choice([True, False]):
            freq = random.randint(2, n)
        test = test[:-freq+1]
        test.extend([duplicate_number] * freq)

        random.shuffle(test)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
