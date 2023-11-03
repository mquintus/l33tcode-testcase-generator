import random

'''
1441 - Build an Array With Stack Operations
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100

    all_numbers = range(1,101)

    for sel in [min_num, 2, 3, 10, 50, 75, 99, max_num]:
        test = sorted(list(random.sample(all_numbers, sel)))
        tests.append(test.__str__().replace(' ', '') + "\n100")

    return '''
'''.join(tests)
