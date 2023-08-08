import random

def generate() -> str:
    tests = ['[1]\n1', '[1]\n0', '[3,1]\n3']
    max_num = 5000

    # random cases
    for _ in range(5):
        test = [i - 500 for i in range(max_num)]
        pivot = random.randint(0, max_num - 1)
        test = test[pivot:] + test[:pivot]
        target = random.randint(-500, max_num - 501)
        tests.append(test.__str__() + "\n" + target.__str__())

    return "\n".join(tests)
