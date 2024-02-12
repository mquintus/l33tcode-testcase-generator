import random

'''
169 - Majority Element
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5 * 10**4
    minval = -10**9
    maxval = 10**9

    for n in [min_num, 20, 20, 21, 100, 100, 101, 5000]:
        # Edgecase 6 - The frequency of each integer is different except for 1 frequency which is there twice
        majority_element_frequency = n//2 + 1
        freq_sum = majority_element_frequency
        freqs = {42: majority_element_frequency}
        while freq_sum < n:
            freq = random.randint(1, n - freq_sum)
            while freq_sum + freq > n:
                freq -= 1
            freq_sum += freq
            el = random.randint(minval, maxval)
            freqs[el] = freq
        matrix = [[el] * freq for el, freq in freqs.items()]
        test = [item for row in matrix for item in row]
        #test.sort()
        random.shuffle(test)
        tests.append(f'{test}'.replace(" ", ""))

    return '''
'''.join(tests)
