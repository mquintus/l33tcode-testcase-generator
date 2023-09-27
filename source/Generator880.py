import random

'''
880 - Decoded String at Index
'''
def generate() -> str:
    tests = []
    max_num = 100
    max_k = 1_000_000_000
    max_unfolded = 2**63 - 1
    letters = "abcdefghijklmnopqrstuvwxyz"

    for l in [1,2,3,10,20,50,max_num - 1]:
        unfolded = 1
        unfolded_new = 1
        stack = [random.choice(letters)]
        for _ in range(l):
            number = random.randint(-9,9)
            if number <= 1:
                unfolded_new += 1
                if unfolded_new > max_unfolded:
                    break
                unfolded = unfolded_new
                stack.append(random.choice(letters))
            else:
                unfolded_new *= number
                if unfolded_new > max_unfolded:
                    break
                unfolded = unfolded_new
                stack.append(str(number))
        s = "".join(stack).__str__()
        k = min(max_k, unfolded)
        tests.append('"' + s + '"\n' + str(k))

    return '''
'''.join(tests)