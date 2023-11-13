import random

'''
2785 - Sort Vowels in a String
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    letters = 'abcedfghijklmnopqrstuvwxyz'
    letters += letters.upper()

    vowels = 'aeiouAEIOU'


    for n in [min_num, 100, max_num]:
        test = "".join([random.choice(letters) for _ in range(n)])
        tests.append(f'"{test}"')

        test = "".join([random.choice(vowels) for _ in range(n)])
        tests.append(f'"{test}"')

    test = "".join([random.choice('acAB') for _ in range(max_num)])
    tests.append(f'"{test}"')

    return '''
'''.join(tests)
