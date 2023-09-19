import random

'''
287 - Find the Duplicate Number
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1

    def make_test(n, how_many=1):
        regular_numbers = [i + minval for i in range(n)]
        duplicates = [random.randint(1,n)] * how_many
        if n + how_many > max_num:
            regular_numbers = regular_numbers[:max_num - how_many]
        all_numbers = [*regular_numbers, *duplicates]
        random.shuffle(all_numbers)
        return all_numbers.__str__().replace(" ", "")

    for n in [min_num, 2, 10, 100, 1000, 10000, 10000, 10000]:
        test = make_test(n, how_many=random.randint(1,2))
        tests.append(test)

    return '''
'''.join(tests)