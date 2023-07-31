import random


def generate() -> str:
    tests = []

    stringa = 'a'*1000
    stringb = 'b'*1000
    test = '"' + stringa.__str__() + '"\n"' + stringb.__str__() + '"'
    tests.append(test)

    stringa = 'ab'*500
    stringb = 'ba'*500
    test = '"' + stringa.__str__() + '"\n"' + stringb.__str__() + '"'
    tests.append(test)

    stringa = 'abcd'*250
    stringb = 'zaba'*250
    test = '"' + stringa.__str__() + '"\n"' + stringb.__str__() + '"'
    tests.append(test)

    stringa = 'abcd'*250
    stringb = 'z'
    test = '"' + stringa.__str__() + '"\n"' + stringb.__str__() + '"'
    tests.append(test)

    for _ in range(4):
        stringa = "".join(random.choices('abcdedfghijklmnopqrstuvwxyz', k=1000))
        stringb = "".join(random.choices('abcdedfghijklmnopqrstuvwxyz', k=1000))
        test = '"' + stringa.__str__() + '"\n"' + stringb.__str__() + '"'
        tests.append(test)

    return "\n".join(tests)
