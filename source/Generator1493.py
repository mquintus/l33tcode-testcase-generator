import random
def generate():
    tests = []
    nums = [0 for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [1 for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [random.randint(0, 1) for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [random.randint(0, 1) for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [random.randint(0, 1) for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [random.randint(0, 1) for i in range(10 ** 5)]
    tests.append(nums.__str__())
    nums = [1]
    tests.append(nums.__str__())
    nums = [0]
    tests.append(nums.__str__())
    nums = [1, 1]
    tests.append(nums.__str__())
    nums = [0, 0]
    tests.append(nums.__str__())
    nums = [0, 1]
    tests.append(nums.__str__())
    nums = [1, 0]
    tests.append(nums.__str__())

    tests = "\n".join(tests)
    return tests
