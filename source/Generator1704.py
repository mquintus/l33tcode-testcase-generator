import random

'''
1704 - Determine if String Halves Are Alike
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 1000
    alphabet = ""
    for char in range(ord('a'), ord('z')+1):
        alphabet += chr(char)
        alphabet += chr(char).upper()

    for n in [min_num, 100, 200, 300, 400, 500, 800, max_num]:
        test = "".join([random.choice(alphabet) for _ in range(n)])
        tests.append(f'"{test}"')

    return "\n".join(tests)
