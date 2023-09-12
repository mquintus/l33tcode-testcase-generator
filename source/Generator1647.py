import random
import itertools

# 1647. Minimum Deletions to Make Character Frequencies Unique

def generate() -> str:
    tests = []
    max_length = 100_000

    letters = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(3):
        s = "".join([random.choice(letters) for i in range(max_length)]).__str__()
        test = f'"{s}"'
        tests.append(test)

    test = list("a" * (max_length // 2) + "b" * (max_length // 2))
    random.shuffle(test)
    tests.append('"' + "".join(test) + '"')

    test = list("a" * (max_length // 3) + "b" * (max_length // 3) + "c" * (max_length // 3))
    random.shuffle(test)
    tests.append('"' + "".join(test) + '"')

    s = "a" * int(max_length // 26 - 1)
    for i in range(1, 26):
        s += chr(ord("a") + i) * int(max_length // 26 - i)
    test = s
    tests.append('"' + "".join(test) + '"')

    s = ""
    for i in range(25, -1, -1):
        s += chr(ord("a") + i) * int(max_length // 26 - 1)
    test = s
    tests.append('"' + "".join(test) + '"')

    return "\n".join(tests)
