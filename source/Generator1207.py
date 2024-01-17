import random

'''
1207 - Unique Number of Occurrences
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000

    min_value = -1000
    max_value = 1000

    # Edgecase 1 - Only one element
    test = [random.randint(min_value, max_value)]
    tests.append(f'{test}'.replace(" ", ""))

    # Edgecase 2 - Only two elements
    test = [random.randint(min_value, max_value), random.randint(min_value, max_value)]
    tests.append(f'{test}'.replace(" ", ""))

    # Edgecase 3 - Two identical elements
    test = [random.randint(min_value, max_value)] * 2
    tests.append(f'{test}'.replace(" ", ""))

    # Edgecase 4 - The frequency of each integer is identical
    freq_sum = 0
    freqs = {}
    default_freq = random.randint(1, max_num//13)
    available_elements = list(range(min_value, max_value + 1))
    random.shuffle(available_elements)
    while freq_sum + default_freq <= max_num:
        freq = default_freq
        freq_sum += freq
        el = available_elements.pop()
        freqs[el] = freq
    matrix = [[el] * freq for el, freq in freqs.items()]
    test = [item for row in matrix for item in row]
    #random.shuffle(test)
    test.sort()
    tests.append(f'{test}'.replace(" ", ""))

    for _ in range(2):
        # Edgecase 5 - The frequency of each integer is different
        freq_sum = 0
        freqs = {}
        available_frequencies = set(range(1, max_value + 1))
        available_elements = list(range(1, max_value + 1))
        random.shuffle(available_elements)
        while freq_sum < max_num and len(available_frequencies) > 0:
            freq = random.choice(list(available_frequencies))
            fail_counter = 5
            while freq_sum + freq >= max_num:
                freq = random.choice(list(available_frequencies))
                fail_counter -= 1
                if fail_counter == 0:
                    break
            if fail_counter == 0:
                break
            #print(freq)
            available_frequencies.remove(freq)
            freq_sum += freq
            el = available_elements.pop()
            freqs[el] = freq
        matrix = [[el] * freq for el, freq in freqs.items()]
        test = [item for row in matrix for item in row]
        #random.shuffle(test)
        test.sort()
        tests.append(f'{test}'.replace(" ", ""))

    for _ in range(2):
        # Edgecase 6 - The frequency of each integer is different except for 1 frequency which is there twice
        freq_sum = 0
        freqs = {}
        available_frequencies = list(range(20))
        available_frequencies.append(random.randint(1, 20))
        available_elements = list(range(1, max_value + 1))
        random.shuffle(available_elements)
        while freq_sum < max_num and len(available_frequencies) > 1:
            freq = random.choice(list(available_frequencies))
            while freq_sum + freq > max_num or freq not in available_frequencies:
                freq -= 1
            available_frequencies.remove(freq)
            freq_sum += freq
            el = available_elements.pop()
            freqs[el] = freq
        matrix = [[el] * freq for el, freq in freqs.items()]
        test = [item for row in matrix for item in row]
        test.sort()
        #random.shuffle(test)
        tests.append(f'{test}'.replace(" ", ""))

    return '''
'''.join(tests)
