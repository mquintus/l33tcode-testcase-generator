import random

'''
1578 - Minimum Time to Make Rope Colorful
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 1000
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    n = min_num
    colors = [random.choice(alphabet) for _ in range(n)]
    weights = [random.randint(minval, maxval) for _ in range(n)]
    test = '"' + "".join(colors) + '"\n' + weights.__str__().replace(' ', '')
    tests.append(test.__str__().replace(' ', ''))

    n = 1000
    start = random.randint(0, 10)
    end = random.randint(start + 1, 26)
    colors = [random.choice('ho') for _ in range(n)]
    weights = [random.randint(minval, maxval) for _ in range(n)]
    test = '"' + "".join(colors) + '"\n' + weights.__str__().replace(' ', '')
    tests.append(test.__str__().replace(' ', ''))

    n = 2024
    start = random.randint(0, 10)
    end = random.randint(start + 1, 26)
    alphabet_christmas = 'merrychristmashohohoooohappyhanukkahhappyholidayshappyholidaysandahappynewyearmaypeacebeonearth'
    offset = random.randint(0, len(alphabet_christmas)-1)
    colors = [alphabet_christmas[(i+offset) % len(alphabet_christmas)] for i in range(n)]
    weights = [random.randint(minval, maxval) for _ in range(n)]
    test = '"' + "".join(colors) + '"\n' + weights.__str__().replace(' ', '')
    tests.append(test.__str__().replace(' ', ''))


    for n in [100, max_num]:
        start = random.randint(0, 10)
        end = random.randint(start + 1, 26)
        colors = [random.choice(alphabet[start:end]) for _ in range(n)]
        weights = [random.randint(minval, maxval) for _ in range(n)]
        test = '"' + "".join(colors) + '"\n' + weights.__str__().replace(' ', '')
        tests.append(test.__str__().replace(' ', ''))

        colors = [random.choice(alphabet)] * n
        weights = [random.randint(minval, maxval) for _ in range(n)]
        test = '"' + "".join(colors) + '"\n' + weights.__str__().replace(' ', '')
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)


if __name__ == '__main__':
    print(generate())