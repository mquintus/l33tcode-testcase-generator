import random

'''
1347 - Minimum Number of Steps to Make Two Strings Anagram
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5*(10**4)
    alphabet = ""
    for char in range(ord('a'), ord('z')+1):
        alphabet += chr(char)

    # To make sure that non-anagram strings are tested
    # We have to use different alphabets for the two strings
    somechars = alphabet[:13]
    otherchars = alphabet[13:]

    n = min_num
    # Two different chars
    string1 = random.choice(alphabet)
    string2 = random.choice(alphabet)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    n = min_num
    # Two identical chars
    string1 = random.choice(alphabet)
    test = f'"{string1}"\n"{string1}"'
    tests.append(f'{test}')

    # Testcases 3 - 8
    for n in [5000, max_num]:
        for equals in [0, n // 2, n]:
            diff = n - equals
            string1 = "".join([random.choice(somechars) for _ in range(n)])
            string2 = string1[:equals] + "".join([random.choice(otherchars) for _ in range(diff)])
            test = f'"{string1}"\n"{string2}"'
            tests.append(f'{test}')

    return "\n".join(tests)
