import random

'''
2038 - Remove Colored Pieces if Both Neighbors are the Same Color
'''
def generate() -> str:
    tests = []
    min_letters = 1
    max_letters = int(1e5)
    letters = ["A", "B"]

    for length in [min_letters, 2, 3, 3, 3, 200, 240, max_letters - 1]:
        s = "".join([random.choice(letters) for _ in range(length)])
        test = '"' + s + '"'
        tests.append(test.__str__())

    return '''
'''.join(tests)


    return '''
'''.join(tests)
