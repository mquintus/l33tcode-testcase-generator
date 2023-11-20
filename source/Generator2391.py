import random

'''
2391 - Minimum Amount of Time to Collect Garbage
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    min_garbage = 1
    max_garbage = 10
    garbage_type = 'GPM'
    min_travel = 1
    max_travel = 100

    for n in [min_num, 3, 4, 10, 10, 10, 100, max_num]:
        garbage = []
        for stop in range(n):
            number_of_garbage_at_stop = random.randint(min_garbage, max_garbage)
            garbage_at_stop = "".join([random.choice(garbage_type) for i in range(number_of_garbage_at_stop)])
            garbage.append(f'"{garbage_at_stop}"')
        travel = [random.randint(min_travel, max_travel) for i in range(n-1)]
        tests.append(garbage.__str__().replace(' ', '').replace("'", '') + "\n" + travel.__str__().replace(' ', ''))

    return '''
'''.join(tests)
