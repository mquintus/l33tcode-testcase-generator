import random

'''
1422 - Maximum Score After Splitting a String
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 500
    minval = 0
    maxval = 1

    for n in [min_num, min_num, max_num//2, max_num//2, max_num, max_num, max_num, max_num]:
        test = [random.randint(minval, maxval).__str__() for _ in range(n)]
        tests.append('"' + ''.join(test) + '"')

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())
