import random

'''
1249 - Minimum Remove to Make Valid Parentheses
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
#    max_num = 10**3 * 2

    for n in [min_num, min_num+1, max_num-1, max_num]:
        for a in range(2):
            test = []
            for i in range(n):
                rand = random.randint(0, 10)
                if rand == 0:
                    test.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
                elif rand < 5:
                    test.append('(')
                else:
                    test.append(')')
            tests.append('"' + ''.join(test) + '"')

    return '''
'''.join(tests)
