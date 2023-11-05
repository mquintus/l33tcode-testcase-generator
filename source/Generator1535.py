from .helpers import helpers

'''
1535 - Find the Winner of an Array Game
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1

    min_k = 1
    max_k = 10**9

    # Test cases
    for k in [min_k, max_k]:
        for n in [min_num, 20, 100, max_num]:
            unique_numbers = helpers.get_unique_numbers(n, minval)
            test = f"{unique_numbers}\n{k}"
            tests.append(test.replace(' ', ''))


    return '''
'''.join(tests)