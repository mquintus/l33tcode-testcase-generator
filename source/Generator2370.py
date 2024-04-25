import random

'''
2370 - Longest Ideal Subsequence
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    min_k = 0
    max_k = 25
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for n in [min_num, 100, 1000, 10000, max_num, max_num, max_num]:
      test = "".join([random.choice(alphabet) for _ in range(n)])
      k = random.randint(min_k, max_k)
      tests.append('"' + test + '"\n' + str(k))

    test = "a"*max_num
    k = 25
    tests.append('"' + test + '"\n' + str(k))
    
    return '''
'''.join(tests)
