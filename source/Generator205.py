import random

'''
205 - Isomorphic Strings
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4

    alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789'+ '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~' + ' ' + '\t' + '\n'+ '\r'
    shuffled = list(alphabet)
    #random.shuffle(shuffled)
    shuffled = shuffled[1:] + shuffled[:1]
    translation = {a: b for a, b in zip(alphabet, shuffled)}
    translation['\''] = '\''
    translation['"'] = '"'

    switch_quotes = lambda s: s.translate(str.maketrans('\'"', '"\''))

    # Testcase 1 - Short strings
    a = 'a'
    b = 'b'
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 2 - Same strings
    n = random.randint(10, 20)
    a = ''.join(random.choices(alphabet, k=n))
    a = a + a + a
    b = a
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 3 - Valid translation
    a = ''.join(random.choices(alphabet, k=n))
    a = a + a + a + '\'"'
    b = ''.join(translation[c] for c in a)
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 4 - Random strings
    n = random.randint(min_num, 10)
    a = ''.join(random.choices(alphabet, k=n)) + '\'"'
    b = ''.join(random.choices(alphabet, k=n)) + '\'"'
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 5 - No duplicates in source
    n = random.randint(min_num, 10)
    a = ''.join(random.choices(alphabet, k=n))
    b = a + "aaa"
    a = a + "abc"
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 6 - No duplicates in target
    n = random.randint(min_num, 10)
    a = ''.join(random.choices(alphabet, k=n))
    b = a + "abcd"
    a = a + "aaaa"
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 7 - Valid translation - Long
    n = random.randint(max_num-1000, max_num-1)
    a = ''.join(random.choices(alphabet, k=n))
    b = ''.join(translation[c] for c in a)
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    # Testcase 8 - Invalid translation - Long
    n = random.randint(max_num-1000, max_num-1)
    a = ''.join(random.choices(alphabet, k=n))
    b = ''.join(translation[c] for c in a) + 'z'
    a = a + 'a'
    test = switch_quotes(ascii(a)) + "\n" + switch_quotes(ascii(b))
    tests.append(test)

    return '''
'''.join(tests)
