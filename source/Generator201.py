import random

'''
201 - Bitwise AND of Numbers Range
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 2*31 - 1

    for _ in range(4):
        left = random.randint(min_num, max_num - 1)
        right = random.randint(left, max_num)
        tests.append(left.__str__() + '\n' + right.__str__())

    for _ in range(4):
        left_exp = random.randint(20, 30)
        right_exp = random.randint(left_exp + 1, 31)
        left = 2 ** left_exp
        right = (2 ** right_exp) - random.randint(1, 31)
        tests.append(left.__str__() + '\n' + right.__str__())

    return '''
'''.join(tests)
