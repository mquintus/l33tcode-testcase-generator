import random

'''
455 - Assign Cookies
'''
def generate() -> str:
    tests = []

    len_s_min = 0
    len_s_max = 3* 10**4
    len_g_min = 0
    len_g_max = 3 * 10**4

    minval = 1
    maxval = 100000

    # Test case 1 - Kids are greedier than cookies are big
    len_s = 10
    len_g = 10
    offset = random.randint(1, 100)
    factor = random.randint(1, 10)
    test_s = [factor*i+offset for i in range(len_s)].__str__().replace(' ', '')
    test_g = [factor*i+offset+1 for i in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 2 - No cookies
    len_s = 0
    len_g = 10
    test_s = [i+1 for i in range(len_s)].__str__().replace(' ', '')
    test_g = [i+2 for i in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 3 - No matching cookies // max out the greed
    len_s = 10
    len_g = 10
    offset = random.randint(1, 100)
    test_s = [i+1+offset for i in range(len_s)].__str__().replace(' ', '')
    test_g = [2**31 - i - 1 - offset for i in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 4 - Max out the greed and cookie size
    len_s = 10
    len_g = 10
    offset = random.randint(1, 100)
    test_s = [2**31 - i - offset for i in range(len_s)].__str__().replace(' ', '')
    test_g = [2**31 - i - offset - 1 for i in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 5 - Go up with the length
    len_s = 1000
    len_g = 1500
    test_s = [random.randint(minval, 9) for _ in range(len_s)].__str__().replace(' ', '')
    test_g = [random.randint(minval, 9) for _ in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 6 - Max out the length
    len_s = len_s_max
    len_g = len_g_max
    test_s = [random.randint(minval, 9) for _ in range(len_s)].__str__().replace(' ', '')
    test_g = [random.randint(minval, 9) for _ in range(len_g)].__str__().replace(' ', '')
    test = test_g + '\n' + test_s
    tests.append(test)

    # Test case 7 - Random values
    for _ in range(2):
        len_s = random.randint(len_s_min, len_s_max)
        len_g = random.randint(len_g_min, len_g_max)
        test_s = [random.randint(minval, maxval) for _ in range(len_s)].__str__().replace(' ', '')
        test_g = [random.randint(minval, maxval) for _ in range(len_g)].__str__().replace(' ', '')
        test = test_g + '\n' + test_s
        tests.append(test)

    return '''
'''.join(tests)


if __name__ == '__main__':
    print(generate())