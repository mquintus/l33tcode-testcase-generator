import random
def generate():
    tests = []
    letters = "abc"
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    letters = "zyqwertyuiopasdfghjklzxcvbnmabc"
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    test = [random.choice(letters) for i in range(10 ** 4)]
    tests.append('"' + "".join(test) + '"')
    tests = "\n".join(tests)
    return tests
