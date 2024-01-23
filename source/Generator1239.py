import random

'''
1239 - Maximum Length of a Concatenated String with Unique Characters
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 16
    letters = "abcdefghijklmnopqrstuvwxyz"

    for n in [min_num, 2, 3, 4, max_num, max_num, max_num, max_num]:
        strlen = random.randint(1, 10)
        test = ["".join([random.choice(letters) for _ in range(strlen)]) for _ in range(n)]
        tests.append(test.__str__().replace('\'', '"'))

    return '''
'''.join(tests)
