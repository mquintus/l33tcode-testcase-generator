import random

'''
451 - Sort Characters By Frequency
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5 * 10**5
    somechars = ""

    # To make sure that non-anagram strings are tested
    # We have to use different alphabets for the two strings
    for char in range(ord('a'), ord('z')+1):
        somechars += chr(char)
    for char in range(ord('A'), ord('Z')+1):
        somechars += chr(char)
    for char in range(ord('1'), ord('9')+1):
        somechars += chr(char)
    somechars += '0'

    for n in [min_num, 10, 20, 50, 100, 1000, max_num]:
        string1 = "".join([random.choice(somechars) for _ in range(n)])
        tests.append(f'"{string1}"')

    return "\n".join(tests)
