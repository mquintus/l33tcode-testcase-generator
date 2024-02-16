import random

'''
1481 - Least Number of Unique Integers after K Removals
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100000

    min_k = 0
    # max_k = n

    min_value = 1
    max_value = 10**9

    next_el = 1

    for what_k in ["min", "max"]:
        # Edgecase 1 - The frequency of each integer is 2
        n = max_num // 100
        test = []
        frequencies = {}
        length = 0
        for i in range(n):
            freq = 2
            if length + freq >= n:
                break
            frequencies[next_el] = freq
            next_el += random.randint(1, 5)
            length += freq
        matrix = [[el] * freq for el, freq in frequencies.items()]
        test = [item for row in matrix for item in row]
        k = random.randint(min_k, min_k + 30) if what_k == "min" else max(min_k, len(test) - 10)
        tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    for what_k in ["min", "max"]:
        # Edgecase 2 - The frequency of each integer is increasing linearly
        n = 500
        test = []
        frequencies = {}
        length = 0
        for i in range(n):
            max_freq = max_num - length
            freq = random.randint(min_num, i + 1)
            if length + freq >= n:
                break
            frequencies[next_el] = freq
            next_el += 1
            length += freq
        matrix = [[el] * freq for el, freq in frequencies.items()]
        test = [item for row in matrix for item in row]
        k = random.randint(min_k, min_k + 30) if what_k == "min" else max(min_k, len(test) - 10)
        tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    for what_k in ["min", "max"]:
        # Edgecase 3 - The frequency of each integer is increasing exponentially
        n = 1000
        test = []
        frequencies = {}
        length = 0
        for i in range(n):
            max_freq = max_num - length
            freq = random.randint(min_num, (2 ** i) + 1)
            if length + freq >= n:
                break
            frequencies[next_el] = freq
            next_el += 1
            length += freq
        matrix = [[el] * freq for el, freq in frequencies.items()]
        test = [item for row in matrix for item in row]
        k = random.randint(min_k, min_k + 30) if what_k == "min" else max(min_k, len(test) - 10)
        tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    for what_k in ["min", "max"]:
        # Edgecase 4 - The frequency of each integer is random
        n = 1500
        test = []
        frequencies = {}
        length = 0
        for _ in range(n):
            max_freq = n - length
            freq = random.randint(min_num, max_freq)
            if length + freq >= n:
                break
            frequencies[next_el] = freq
            next_el += 1
            length += freq
        matrix = [[el] * freq for el, freq in frequencies.items()]
        test = [item for row in matrix for item in row]
        k = random.randint(min_k, min_k + 30) if what_k == "min" else max(min_k, len(test) - 10)
        tests.append(test.__str__().replace(' ', '') + "\n" + str(k))

    return '''
'''.join(tests)
