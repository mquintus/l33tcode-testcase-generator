import random

'''
1657 - Determine if Two Strings Are Close
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 2 * 10**2
    alphabet = ""
    for char in range(ord('a'), ord('z')+1):
        alphabet += chr(char)

    # To make sure that non-anagram strings are tested
    # We have to use different alphabets for the two strings
    somechars = alphabet[:13]
    otherchars = alphabet[13:]

    # Edgecase 1 - Both strings have the same frequency of chars, but different chars
    freq = [random.randint(1, 10) for _ in range(13)]
    string1 = "".join([somechars[i] * f for i, f in enumerate(freq)])
    string2 = "".join([otherchars[i] * f for i, f in enumerate(freq)])
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Edgecase 2 - Both strings have the same chars, but different frequencies
    freq1 = [random.randint(1, 10) for _ in range(13)]
    freq2 = [random.randint(1, 10) for _ in range(13)]
    string1 = "".join([somechars[i] * f for i, f in enumerate(freq1)])
    string2 = "".join([somechars[i] * f for i, f in enumerate(freq2)])
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Edgecase 3 - Both strings have the same chars and frequencies, but in different order
    freq = [random.randint(1, max_num//13) for _ in range(26)]
    string1 = "".join([alphabet[i] * f for i, f in enumerate(freq)])
    string2 = "".join([alphabet[(i + random.randint(1,25))%26] * f for i, f in enumerate(freq)])
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Edgecase 4 - String 1 is a permutation of string 2
    freq = [random.randint(1, max_num//13) for _ in range(26)]
    string1 = "".join([alphabet[i] * f for i, f in enumerate(freq)])
    string2 = list(string1)
    random.shuffle(string2)
    string2 = "".join(string2)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Edgecase 5 - String 1 is a permutation of string 2, but with one extra char from a different alphabet
    freq = [random.randint(1, 10) for _ in range(13)]
    string1 = "".join([somechars[i] * f for i, f in enumerate(freq)])
    string2 = list(string1)
    random.shuffle(string2)
    string2.append(random.choice(otherchars))
    string2 = "".join(string2)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Testcase 6 - String 1 contains only two chars, string 2 contains only two chars, but frequencies swapped
    freq1 = [0 for _ in range(26)]
    freq2 = [0 for _ in range(26)]
    p = random.randint(0,25)
    q = (p + random.randint(1,25)) % 26
    freq1[p] = max_num - 10
    freq1[q] = 10
    freq2[q] = max_num - 10
    freq2[p] = 10
    string1 = "".join([alphabet[i] * f for i, f in enumerate(freq1)])
    string2 = "".join([alphabet[i] * f for i, f in enumerate(freq2)])
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Testcase 7 - String 1 contains only one char, string 2 is identical but 1 short
    freq1 = [0 for _ in range(26)]
    p = random.randint(0,25)
    freq1[p] = max_num
    string1 = "".join([alphabet[i] * f for i, f in enumerate(freq1)])
    string2 = string1[:-1]
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Testcase 8 - String 1 contains only one char, string 2 is identical
    freq1 = [0 for _ in range(26)]
    p = random.randint(0,25)
    freq1[p] = max_num
    string1 = "".join([alphabet[i] * f for i, f in enumerate(freq1)])
    string2 = string1
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    return "\n".join(tests)
