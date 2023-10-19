import random

'''
844 - Backspace String Compare
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200
    letters = "#abcdefghijklmnopqrstuvwxyz"
    letters_pure = "abcdefghijklmnopqrstuvwxyz"

    s = "".join([random.choice(letters) for i in range(min_num)]).__str__()
    t = s
    test = f'"{s}"\n"{t}"'
    tests.append(test.__str__().replace(' ', ''))

    s = "".join([random.choice(letters) for i in range(max_num)]).__str__()
    t = s
    test = f'"{s}"\n"{t}"'
    tests.append(test.__str__().replace(' ', ''))

    s = "#" * max_num
    t = "".join([random.choice(letters) + '#' for i in range(max_num // 2)]).__str__()
    test = f'"{s}"\n"{t}"'
    tests.append(test.__str__().replace(' ', ''))

    for _ in range(3):
        s = "".join([random.choice(letters) for i in range(33)]).__str__()
        t = "".join([random.choice(letters) for i in range(33)]).__str__() + "#" * 33 + s
        test = f'"{s}"\n"{t}"'
        tests.append(test.__str__().replace(' ', ''))

    s = "".join([random.choice(letters) for i in range(66)]).__str__()
    t = s + "".join([random.choice(letters_pure) for i in range(66)]).__str__() + "#" * 66
    test = f'"{s}"\n"{t}"'
    tests.append(test.__str__().replace(' ', ''))

    s = "".join([random.choice(letters) for i in range(max_num)]).__str__()
    t = "".join([random.choice(letters) for i in range(max_num)]).__str__()
    test = f'"{s}"\n"{t}"'
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
