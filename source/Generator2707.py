import random
import itertools

def generate() -> str:
    tests = []

    dictionary = [
        "a"*10 + "b"*10 + "c"*10,
        "b"*10 + "c"*10 + "d"*10,
        "c"*10 + "d"*10 + "e"*10,
    ]
    s = "a"*10 + "b"*10 + "c"*10 + "d"*10 +"e"*10
    test = f'"{s}"\n{dictionary}'.replace("'", '"')
    tests.append(test)

    dictionary = [
        "a"*7 + "b"*10 + "c"*10 + "d"*10 + "e"*8,
        "b"*10 + "c"*10 + "d"*10 + "e"*8,
    ]
    s = "a"*10 + "b"*10 + "c"*10 + "d"*10 +"e"*10
    test = f'"{s}"\n{dictionary}'.replace("'", '"')
    tests.append(test)


    letters = [l for l in "abcdefghijklmnopqrstuvwxyz"]
    s = ""
    for l in letters[::-1]:
        s += l * 2
    s = s[:50]
    dictionary = []
    for i in range(0, 45, 4):
        dictionary.append(s[i:i+3])
        dictionary.append(s[i+1:i+4])
        dictionary.append(s[i+2:i+5])
    dictionary.append(s[0:5])
    dictionary.append(s[10:15])
    dictionary.append(s[20:25])
    dictionary.append(s[30:35])
    dictionary.append(s[40:45])
    dictionary.reverse()
    test = f'"{s}"\n{dictionary}'.replace("'", '"')
    tests.append(test)


    letters = [l for l in "abcdefghijklmnopqrstuvwxyz"]
    for _ in range(4):
        dictionary = list(set(["".join([random.choice(letters) for i in range(random.randint(1,10))]) for _ in range(50)]))
        s = "".join([random.choice(letters) for i in range(50)]).__str__()
        test = f'"{s}"\n{dictionary}'.replace("'", '"')
        tests.append(test)

    return "\n".join(tests)
