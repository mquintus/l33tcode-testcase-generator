import random

'''
392 - Is Subsequence
'''
def generate() -> str:
    tests = []
    min_length_s = 0
    max_length_s = 100
    min_length_t = 0
    max_length_t = 10000

    letters = "abcdefghijklmnopqrstuvxyz"

    def get_random_string(length):
        selection = '"' + "".join([random.choice(letters) for _ in range(length)]) + '"'
        return selection

    m = min_length_s
    n = min_length_t
    test = get_random_string(m) + "\n" + get_random_string(n)
    tests.append(test)

    m = min_length_s
    n = max_length_t
    test = get_random_string(m) + "\n" + get_random_string(n)
    tests.append(test)

    m = max_length_s
    n = min_length_t
    test = get_random_string(m) + "\n" + get_random_string(n)
    tests.append(test)

    m = max_length_s
    n = max_length_t
    test = '"' + "a"*m + '"' +"\n" + '"' + "a"*(m-1) + "b"*(n-m) + '"'
    tests.append(test)

    for _ in range(4):
        m = max_length_s
        n = max_length_t
        test = get_random_string(m) + "\n" + get_random_string(n)
        tests.append(test)

    return '''
'''.join(tests)
