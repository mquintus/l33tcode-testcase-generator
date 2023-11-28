import random

'''
2147 - Number of Ways to Divide a Long Corridor
'''
def generate() -> str:
    tests = []
    max_num = 10**5
    alphabet = 'SP'

    test = ["S"]
    tests.append('"' + "".join(test) + '"')

    test = ["P"]
    tests.append('"' + "".join(test) + '"')

    test = ["SS"]
    tests.append('"' + "".join(test) + '"')

    for n in [100, max_num]:
        test = list(alphabet * (n//2))
        random.shuffle(test)
        tests.append('"' + "".join(test) + '"')

        test = ['S'] * n
        tests.append('"' + "".join(test) + '"')

    return '''
'''.join(tests)
