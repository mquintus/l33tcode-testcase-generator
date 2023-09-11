import random

# 1282. Group the People Given the Group Size They Belong To
def generate() -> str:
    tests = []
    max_length = 500

    for max_num in [1,3,5,10,20,100,200,500]:
        sizes = []
        while len(sizes) < max_length:
            remaining = min(max_num, max_length - len(sizes))
            l = random.randint(1, remaining)
            sizes.extend([l] * l)
        random.shuffle(sizes)
        test = sizes.__str__().replace(" ", "")
        tests.append(test)

    return "\n".join(tests)
