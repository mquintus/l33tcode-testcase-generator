import random

'''
1048 - Longest String Chain
'''
def generate() -> str:
    tests = []
    min_length_word = 1
    max_length_word = 16
    min_length_list = 1
    max_length_list = 1000

    letters = "uvxyz"

    def get_random_string(max_length):
        length = random.randint(min_length_word, max_length)
        selection = "".join([random.choice(letters) for _ in range(length)])
        return selection

    m = min_length_word
    n = min_length_list
    test = [get_random_string(m) for _ in range(n)].__str__().replace("'", '"').replace(' ', '')
    tests.append(test)

    m = min_length_word
    n = 10
    test = [get_random_string(m) for _ in range(n)].__str__().replace("'", '"').replace(' ', '')
    tests.append(test)

    m = max_length_word
    n = min_length_list
    test = [get_random_string(m) for _ in range(n)].__str__().replace("'", '"').replace(' ', '')
    tests.append(test)

    letters = "abcdefuvxyz"
    test = []
    for j in range(max_length_list // max_length_word):
        test.append(["a"])
        for i in range(max_length_word - 1):
            position = random.randint(0, len(test[-1]))
            test.append([*test[-1]])
            test[-1].insert(position, random.choice(letters))
    test = ["".join(t) for t in test].__str__().replace("'", '"').replace(' ', '')
    tests.append(test)

    for _ in range(2):
        m = max_length_word
        n = max_length_list
        test = [get_random_string(m) for _ in range(n)].__str__().replace("'", '"').replace(' ', '')
        tests.append(test)

    return '''
'''.join(tests)

