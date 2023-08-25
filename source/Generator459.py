import random


def generate() -> str:
    tests = []
    max_length = 10**4
    letters = 'abcdefghijklmnopqrstuvwxyz' * (1 + max_length // 26)
    lengths = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,5000]

    tests.append('"x"')
    for l in lengths:
        sequence = "".join(random.sample(letters, max_length // l))
        my_word = '"' + sequence*l + '"'
        tests.append(my_word)

    sequence = "a" * 9998 + "u"
    my_word = '"' + sequence + '"'
    tests.append(my_word)

    sequence = "u" + "a" * 9998
    my_word = '"' + sequence + '"'
    tests.append(my_word)

    sequence = ("a" * 4998 + "u") * 2
    my_word = '"' + sequence + '"'
    tests.append(my_word)

    return "\n".join(tests)
