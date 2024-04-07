import random

'''
678 - Valid Parenthesis String
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100

    alphabet = '()*'

    for n in [min_num, 20, 30, 40, 50, 60, 70, max_num]:
      test = [random.choice(alphabet) for _ in range(n)]
      tests.append('"' + "".join(test) + '"')
    
    
    return '''
'''.join(tests)
