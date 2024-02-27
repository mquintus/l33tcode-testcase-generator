import random
def generate():
    tests = []
    possible_values = [i for i in range(500)]
    for test in range(8):
        tree = []
        number_of_nodes = 488
        # tree = possible_values
        tree.extend(random.sample(possible_values, number_of_nodes))
        target = tree[-1]
        distance = test * 3
        tests.append(
            "\n".join([tree.__str__(), target.__str__(), distance.__str__()])
        )
    tests = "\n".join(tests)
    return tests
