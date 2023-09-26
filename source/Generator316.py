import random

'''
316 - Remove Duplicate Letters
'''
def generate() -> str:
    tests = []
    max_num = 1000
    letters = "abcdefghijklmnopqrstuvwxyz"

    for _ in range(2):
        s = "".join([random.choice(letters) for i in range(300)]).__str__()
        tests.append('"' + s + '"')

    for _ in range(1):
        s = "".join([random.choice(letters) for i in range(max_num)]).__str__()
        tests.append('"' + s + '"')

    s = "a"
    c = 0
    for l in letters[::-1]:
        c += 100
        s += l * 100
        if c >= max_num:
            break
    tests.append('"' + s + '"')

    s = letters * (max_num // len(letters))
    tests.append('"' + s + '"')

    s = letters[::-1] * (max_num // len(letters))
    tests.append('"' + s + '"')

    s = "g"
    tests.append('"' + s + '"')

    s = ""
    for l in letters[::-1]:
        s += l
    for l in letters:
        s += l
    tests.append('"' + s + '"')

    return '''
'''.join(tests)
