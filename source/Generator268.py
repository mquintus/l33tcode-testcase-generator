import random

'''
268 - Missing Number
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**4

    for n in [min_num, 3, 10**3, max_num]:
        # Remove a random number from the list (except zero)
        test = [i for i in range(n)]
        test.remove(random.choice(test[1:]))
        tests.append(test.__str__().replace(' ', ''))

        # Remove zero from the list
        test = [i + 1 for i in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
