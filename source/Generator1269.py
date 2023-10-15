import random

'''
1269 - Number of Ways to Stay in the Same Place After Some Steps
'''
def generate() -> str:
    tests = []
    min_steps = 1
    max_steps = 500
    min_arrl = 1
    max_arrl = 1_000_000

    test = [min_steps, min_arrl]
    tests.append("\n".join([t.__str__() for t in test]))

    test = [min_steps, max_arrl]
    tests.append("\n".join([t.__str__() for t in test]))

    test = [max_steps, random.randint(2, 10)]
    tests.append("\n".join([t.__str__() for t in test]))

    test = [random.randint(min_steps, max_steps), random.randint(min_arrl, max_arrl)]
    tests.append("\n".join([t.__str__() for t in test]))

    for steps in [3, max_steps]:
        for arrl in [3, max_arrl]:
            test = [steps, arrl]
            tests.append("\n".join([t.__str__() for t in test]))

    return '''
'''.join(tests)
