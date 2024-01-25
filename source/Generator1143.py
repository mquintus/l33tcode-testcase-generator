import random

'''
1143 - Longest Common Subsequence
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    letters = "abcdefghijklmnopqrstuvwxyz"

    for i in [min_num, 4, 10, max_num]:
        for j in [min_num, 4, 10, max_num]:
            for let in [letters, [random.choice(letters) for _ in range(3)]]:
                test = '"' + "".join([random.choice(let) for _ in range(i)]) + '"'
                test2 = '"' + "".join([random.choice(let) for _ in range(j)]) + '"'
                tests.append(test + "\n" + test2)

    return '''
'''.join(tests)
