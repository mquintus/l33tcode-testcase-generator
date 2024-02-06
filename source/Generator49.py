import random

'''
49 - Group Anagrams
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    minlength = 0
    maxlength = 100

    somechars = ""
    morechars = ""
    otherchars= ""

    # To make sure that non-anagram strings are tested
    # We have to use different alphabets for the two strings
    for char in range(ord('a'), ord('h')+1):
        somechars += chr(char)
    for char in range(ord('i'), ord('t')+1):
        morechars += chr(char)
    for char in range(ord('u'), ord('z')+1):
        otherchars += chr(char)

    alphabet = somechars + otherchars + morechars

    anagrams = set()

    for n in [min_num, 4, 5, 10, 10, 20, max_num, max_num]:
        places_free = n
        test = []
        while places_free > 0:
            how_many_anagrams = random.randint(1, places_free)
            places_free -= how_many_anagrams

            maxlength_local = random.randint(0, min(maxlength, places_free + how_many_anagrams))

            charset = random.choice([somechars, morechars, otherchars])
            anagram = [random.choice(charset) for _ in range(random.randint(minlength, maxlength_local))]
            anagram = sorted(anagram)
            while "".join(anagram) in anagrams:
                maxlength_local = (maxlength_local - 1) % maxlength
                anagram = [random.choice(charset) for _ in range(random.randint(minlength, maxlength_local))]
                anagram = sorted(anagram)
            anagrams.add("".join(anagram))
            test.append("".join(anagram))
            for ana in range(how_many_anagrams - 1):
                test.append("".join(anagram))
                random.shuffle(anagram)
        tests.append(f"{test}".replace("'", '"'))


    return "\n".join(tests)
