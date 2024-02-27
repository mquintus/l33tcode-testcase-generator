import random

'''
2305 - Fair Distribution of Cookies
'''

def generate() -> str:
    tests = ""
    for k in [7, *range(2, 9)]:
        cookies = [random.randint(1, 100000) for i in range(8)]
        tests += "\n".join([kwa.__str__() for kwa in [cookies, k]]) + "\n"
    return tests
