import random

'''
70 - Climbing Stairs
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 45

    all_tests = list(range(min_num, max_num + 1))

    test = all_tests.pop(0)
    tests.append(test.__str__().replace(' ', ''))

    test = all_tests.pop()
    tests.append(test.__str__().replace(' ', ''))

    random.shuffle(all_tests)

    for i in range(6):
        test = all_tests.pop()
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
