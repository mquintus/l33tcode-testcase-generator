import random

'''
1743 - Restore the Array From Adjacent Pairs
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5

    for n in [min_num, 3, 10, 100, 1000, 10000, max_num]:
        minval = -n // 2
        maxval = n // 2
        random_adder = random.randint(0, n - maxval)
        all_numbers = list(range(random_adder + minval, random_adder + maxval))
        random.shuffle(all_numbers)
        pairs = [[all_numbers[i], all_numbers[i-1]] for i in range(1, len(all_numbers))]
        tests.append(pairs.__str__().replace(' ', ''))

    return '''
'''.join(tests)
