import random

'''
1624 - Largest Substring Between Two Equal Characters
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 300

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Test case 1: Use only two characters
    n = random.randint(5, 10)
    char1 = random.choice(alphabet)
    char2 = random.choice(alphabet)
    test = '"' + ''.join([random.choice([char1, char2]) for _ in range(n)]) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 2: Use seasonal sentence
    sentence = 'merrychristmasandahappynewyear'
    test = '"' + sentence * random.randint(1,3) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 3: Use minimum number of characters
    n = min_num
    test = '"' + ''.join([random.choice(alphabet) for _ in range(n)]) + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 4: Subset spanning the full string
    char1 = random.choice(alphabet)
    alphabet_without_char1 = alphabet.replace(char1, '')
    test = '"' + char1 + alphabet_without_char1 + char1 + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 5: Subset spanning only one letter towards the end of the string
    char1 = random.choice(alphabet[-10:-2])
    test = '"' + alphabet + char1 + '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 6: Subset starting ore than 30 characters from the start and from end of the string
    # Also use a long string
    # Also use a string with many repeating characters
    # Have the edge character inside the substring
    char1 = random.choice(alphabet)
    alphabet_without_char1 = alphabet.replace(char1, '')
    test = '"'
    for i in range(len(alphabet_without_char1)):
        test += alphabet_without_char1[i] * random.randint(10,12)
        if i == 5 or i == 20:
            test += char1
        elif i == 10:
            test += char1 * random.randint(10,12)
    test += '"'
    tests.append(test.__str__().replace(' ', ''))

    # Test case 7: Do some random repeating stuff
    someint = random.randint(5, 10)
    n = max_num // someint
    test = "".join([random.choice(alphabet) for _ in range(n)]) * someint
    test = '"' + test + '"'
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)




if __name__ == '__main__':
    print(generate())