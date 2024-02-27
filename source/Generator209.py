import random
def generate():
    tests = ["10000, \n[1337]", "10, \n[1337]"]

    for i in range(6):
        target = random.randint(1, 10 ** 9)
        nums = [random.randint(1, 10 ** 4) for i in range(10 ** 5)]
        tests.append(target.__str__() + "\n" + nums.__str__())
    tests = "\n".join(tests)
    return tests
