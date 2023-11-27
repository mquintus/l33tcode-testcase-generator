import random

'''
935 - Knight Dialer
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5000

    test = min_num
    tests.append(test.__str__().replace(' ', ''))

    test = max_num
    tests.append(test.__str__().replace(' ', ''))

    for _ in range(6):
        test = random.randint(min_num, max_num)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
