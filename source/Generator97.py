import random


def generate() -> str:
    tests = []
    max_length_a = 100
    max_length_b = 98
    letters = 'df' * (1 + max_length_a)

    test = ['""', '""', '"a"']
    tests.append("\n".join(test))

    test = ['"a"', '""', '""']
    tests.append("\n".join(test))

    test = ['"a"', '""', '"a"']
    tests.append("\n".join(test))

    # positive tests
    for _ in range(2):
        a = "".join(random.sample(letters, max_length_a))
        b = "".join(random.sample(letters, max_length_b))
        c = ""
        test = []
        p_a = 0
        p_b = 0
        while p_a < len(a) or p_b < len(b):
            if random.randint(0, 1) == 0 and p_a < len(a):
                    c += a[p_a]
                    p_a += 1
            elif p_b < len(b):
                    c += b[p_b]
                    p_b += 1
        for string in [a, b, c]:
            test.append('"' + string + '"')
        tests.append("\n".join(test))

    # negative tests
    for _ in range(3):
        a = "".join(random.sample(letters, max_length_a))
        b = "".join(random.sample(letters, max_length_b))
        c = ""
        test = []
        p_a = 0
        p_b = 0
        while p_a < len(a) or p_b < len(b):
            if random.randint(0, 1) == 0 and p_a < len(a):
                    c += a[p_a]
                    p_a += 1
            elif p_b < len(b):
                    c += b[p_b]
                    p_b += 1
        if c[-1] != a[-1]:
            c = c[:-1] + a[-1]
        else:
            c = c[:-3] + b[-3:]
        for string in [a, b, c]:
            test.append('"' + string + '"')
        tests.append("\n".join(test))

    return "\n".join(tests)
