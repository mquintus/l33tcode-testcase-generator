import random

'''
779 - K-th Symbol in Grammar
'''
def generate() -> str:
    tests = []
    i = 8
    n = 30
    for pot in [random.randint(1,3),random.randint(10,15),random.randint(25,28)]:
        for k in range(2**pot-0-pot, 2**pot+3-pot):
            test = f"{n}\n{k}"
            tests.append(test.__str__().replace(' ', ''))
            i -= 1
            if i == 0:
                break
        if i == 0:
            break

    return '''
'''.join(tests)
