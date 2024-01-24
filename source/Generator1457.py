import random

'''
1457 - Pseudo-Palindromic Paths in a Binary Tree
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 9

    for n in [min_num, 10, 20, 30, 40, 50, max_num, max_num]:
        test = []
        prev_skip = True
        for i in range(n):
            skip = False
            if not prev_skip:
                skip = random.choice([True, False])

            if skip:
                prev_skip = True
                test.append("null")
            else:
                prev_skip = False
                test.append(random.randint(minval,maxval))
        tests.append(test.__str__().replace(' ', '').replace("'", ''))

    return '''
'''.join(tests)
