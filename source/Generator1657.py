import random

'''
1657 - Determine if Two Strings Are Close
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000

    min_value = 1
    max_value = 1000

    # Edgecase 1 - The frequency of each integer is identical
    freq_sum = 0
    freqs = {}
    default_freq = random.randint(1, max_num//13)
    available_elements = list(range(min_value, max_value + 1))
    random.shuffle(available_elements)
    while freq_sum < max_num:
        freq = default_freq
        freq_sum += freq
        el = available_elements.pop()
        freqs[el] = freq
    test = [[el] * freq for el, freq in freqs.items()]
    tests.append(f'{test}'.replace(" ", ""))

    return "\n".join(tests)
