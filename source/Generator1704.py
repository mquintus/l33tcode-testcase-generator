import random

'''
1704 - Determine if String Halves Are Alike
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 1000
    alphabet = ""
    for char in range(ord('a'), ord('z')+1):
        alphabet += chr(char)
        alphabet += chr(char).upper()

    vowels = 'aeiou'
    vowels += vowels.upper()

    non_vowels = list(set(alphabet) - set(vowels))

    n = min_num
    test = "".join([random.choice(alphabet) for _ in range(n)])
    tests.append(f'"{test}"')

    test = "".join([random.choice(vowels) for _ in range(n)])
    tests.append(f'"{test}"')

    n = max_num
    for vowel_count_1, vowel_count_2 in [
        (n // 2, n // 2 - 1),
        (n // 2, n // 2),
        (n // 2 - 1, n // 2),
        (n // 3, n // 3),
        (n // 3, n // 3 - 1),
        (int(n // 2.5), int(n // 2.5)),
    ]:
        non_vowel_count_1 = n//2 - vowel_count_1
        non_vowel_count_2 = n//2 - vowel_count_2

        part1 = []
        part1.extend([random.choice(non_vowels) for _ in range(non_vowel_count_1)])
        part1.extend([random.choice(vowels) for _ in range(vowel_count_1)])
        random.shuffle(part1)

        part2 = []
        part2.extend([random.choice(non_vowels) for _ in range(non_vowel_count_2)])
        part2.extend([random.choice(vowels) for _ in range(vowel_count_2)])
        random.shuffle(part2)

        parts_together = part1
        parts_together.extend(part2)

        test = "".join(parts_together)
        tests.append(f'"{test}"')

    return "\n".join(tests)
