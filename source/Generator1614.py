import random

'''
1614 - Maximum Nesting Depth of the Parentheses
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 100


    alphabet ='0123456789+-/'

    test = '"()"'
    tests.append(test)

    test = '"()()"'
    tests.append(test)

    test = '"42"'
    tests.append(test)

    for n in [20, 20, max_num, max_num]:
        p = random.randint(1, n)
        test = [random.choice(alphabet) for _ in range(n)]
        for i in range(p):
            pos = random.randint(0, len(test)-2)
            if test[pos] in ['(', ')']:
                continue
            test[pos] = '('
            start = random.randint(pos, len(test)-1)
            for pos2 in range(start, len(test)):
                if test[pos2] in ['(', ')']:
                    continue
                test[pos2] = ')'
                break
            else:
                test[pos] = '*'
        tests.append('"' + "".join(test) + '"')

    return '''
'''.join(tests)
