import random

'''
647 - Palindromic Substrings
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    # Testcase 1 - One letter
    n = min_num
    test = [random.choice(alphabet) for _ in range(n)]
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2 - Random letters
    n = max_num
    test = [random.choice(alphabet) for _ in range(n)]
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 3 - All the same letter
    n = max_num
    test = random.choice(alphabet) * n
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 4 - Two alternating letters
    n = max_num
    test = random.choice(alphabet) * (n // 2) + random.choice(alphabet) * (n // 2)
    random.shuffle(list(test))
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 5 - One big palindrome with a center
    n = max_num
    test = [random.choice(alphabet)]
    for _ in range(int(n // 2.1)):
        char = random.choice(alphabet)
        test.append(char)
        test.insert(0, char)
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 5 - One big palindrome without a center
    n = max_num
    test = []
    for _ in range(n // 2):
        char = random.choice(alphabet)
        test.append(char)
        test.insert(0, char)
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 7 - Concatenation of two palindromes
    n = max_num
    i = random.randint(1, 25)
    p1 = [random.choice(alphabet)]
    for _ in range(n // 5):
        i += 1
        char = alphabet[i % 26]
        p1.append(char)
        p1.insert(0, char)
    i = random.randint(1, 25)
    p2 = []
    for _ in range(n // 5):
        i += 1
        char = alphabet[i % 26]
        p2.append(char)
        p2.insert(0, char)
    test = p1 + p2
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 8 - Concatenation of eight palindromes
    n = max_num
    test = []
    for _ in range(8):
        i = random.randint(1, 25)
        p1 = [alphabet[i % 26]]
        for _ in range(n // 34):
            i += 1
            char = alphabet[i % 26]
            p1.append(char)
            p1.insert(0, char)
        test += p1
    test = '"' + "".join(test) + '"'
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
