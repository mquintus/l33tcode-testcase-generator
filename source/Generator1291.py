import random

'''
1291 - Sequential Digits
'''
def generate() -> str:
    tests = []
    minval = 10
    maxval = 10**9

    # Testcase 1: Max range
    low = random.randint(minval,12)
    high = random.randint(123456789,maxval)
    tests.append(f'{low}\n{high}')

    # Testcase 2: Random range
    low = random.randint(minval, maxval)
    high = random.randint(low, maxval)
    tests.append(f'{low}\n{high}')

    # Testcase 3: Empty range
    low = random.randint(minval, maxval)
    high = low + 1
    tests.append(f'{low}\n{high}')

    # Testcase 4: Single match range
    matches = [12,23,34,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
    low_index = random.randint(1, len(matches)-3)
    high_index = low_index+2
    low = matches[low_index] + 10
    high = matches[high_index] - 10
    tests.append(f'{low}\n{high}')

    # Testcase 5: +1
    low_index = random.randint(0, len(matches)-2)
    high_index = random.randint(low_index, len(matches)-1)
    low = matches[low_index] + 1
    high = matches[high_index] + 1
    tests.append(f'{low}\n{high}')

    # Testcase 6: -1
    low_index = random.randint(0, len(matches)-2)
    high_index = random.randint(low_index, len(matches)-1)
    low = matches[low_index] -1
    high = matches[high_index] - 1
    tests.append(f'{low}\n{high}')

    # Testcase 7: Including both ends
    low_index = random.randint(0, len(matches)-2)
    high_index = random.randint(low_index+1, len(matches)-1)
    low = matches[low_index]
    high = matches[high_index]
    tests.append(f'{low}\n{high}')

    # Testcase 8: Excluding both ends
    low_index = random.randint(0, len(matches)-2)
    high_index = random.randint(low_index, len(matches)-1)
    low = matches[low_index] + 1
    high = matches[high_index] - 1
    tests.append(f'{low}\n{high}')

    return '''
'''.join(tests)
