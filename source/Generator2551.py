import random
def generate():
    tests = []
    for n in range(8):
        weights = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
        k = random.randint(1, len(weights))
        test = weights.__str__() + "\n" + k.__str__()
        tests.append(test)
    tests = "\n".join(tests)
    return tests
