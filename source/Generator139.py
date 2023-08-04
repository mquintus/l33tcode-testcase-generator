import random
import itertools

def generate() -> str:
    tests = []

    letters = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(8):
        s = "".join([random.choice(letters) for i in range(300)]).__str__()

        worddict = set()

        c = 0
        while len(worddict) < 1000 and c < 20000:
            # perm = next(permutations)
            c += 1
            start = random.randint(0, len(s) - 1)
            end = start + random.randint(5, 20)
            worddict.add("".join(s[start:end]))
        worddict = list(worddict)
        test = f'"{s}"\n{worddict}'.replace("'", '"')
        tests.append(test)

    permutations = itertools.permutations(letters)
    for _ in range(8):
        s = "".join([random.choice(letters) for i in range(300)]).__str__()

        worddict = set()

        c = 0
        while len(worddict) < 1000 and c < 20000:
            perm = next(permutations)
            c += 1
            start = random.randint(0, len(perm) - 1)
            end = start + random.randint(1, 20)
            worddict.add("".join(perm[start:end]))
        worddict = list(worddict)
        test = f'"{s}"\n{worddict}'.replace("'", '"')
        tests.append(test)

    return "\n".join(tests)
