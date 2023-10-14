import random

'''
2742 - Painting the Walls
'''
def generate() -> str:
    tests = []
    min_time = 1
    max_time = 500
    min_cost = 1
    max_cost = 10**6
    min_length = 1
    max_length = 500

    for n in [min_length, 2, 3, 10, 10, 20, 100, max_length]:
        cost = [random.randint(min_cost, max_cost) for _ in range(n)]
        time = [random.randint(min_time, n) for _ in range(n)]
        tests.append(
            cost.__str__().replace(' ', '')
            + "\n" + time.__str__().replace(' ', '')
            )

    return '''
'''.join(tests)
