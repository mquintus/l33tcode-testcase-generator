import itertools, random
def generate():
    letters = """qwertyuiopsdfghjklzxcvbnm,.1234567890-=+_"""
    tests = [" ", "", "0", "1", "4", "10", "*", "-"]
    x = ["1", "2", "3"]
    tests.append("".join(["A" for i in range(5 * 10 ** 4)]))
    tests.append("".join(["A" for i in range(5 * 10 ** 4 - 1)]) + "B")
    tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]) + "B")
    tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]))
    tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=3)])
    tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=4)])
    for i in range(8):
        test = "".join(
            [
                letters[random.randint(0, len(letters) - 1)]
                for i in range(5 * 10 ** 4)
            ]
        )
        tests.append(test)
    tests = "\n".join(['"' + test + '"' for test in tests])
    return tests
