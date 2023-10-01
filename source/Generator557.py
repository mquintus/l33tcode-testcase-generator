import random

'''
557 - Reverse Words in a String III
'''
def generate() -> str:
    tests = []
    min_letters = 1
    max_letters = 50000
    letters = [chr(x) for x in range(ord("A"), ord("z") + 1)]

    for length in [min_letters, 2, 3, 3, 3, 20, 24, max_letters - 1]:
        s = ''
        remaining_length = length
        while remaining_length > 0:
            wordlength = random.randint(1, remaining_length)
            if len(s) > 0:
                s += " "
            s += "".join([random.choice(letters) for _ in range(wordlength)])
            remaining_length = length - len(s)
        test = '"' + s + '"'
        tests.append(test.__str__().replace('\\', ''))

    return '''
'''.join(tests)
