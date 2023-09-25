import random

'''
389 - Find the Difference
'''
def generate() -> str:
    tests = []
    min_letters = 0
    max_letters = 1000

    letters = "abcdefghijklmnopqrstuvwxyz"
    for length in range(min_letters, max_letters  + 1, (max_letters - min_letters) // 8):
        if length == (max_letters - min_letters) // 4:
            # Edge case: t begins with a letter that didn't appear in s
            s = ["a", "b", "c"]
            t = ["z", "a", "b", "c"]
        else:
            s = [random.choice(letters) for _ in range(length)]
            t = [*s]
            t.append(random.choice(letters))
            random.shuffle(t)
        test = '"' + ''.join(s) + '"' + '\n' + '"' + ''.join(t) + '"'
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
