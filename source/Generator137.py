import random
def generate():
    def numrandom(i):
        num = random.randint(-10000, 10000)
        num *= 10000
        num += i
        return num

    tests = []
    for test in range(8):
        n = 9999
        nums = []
        num = 0
        for i in range(n):
            num = numrandom(i)
            nums.append(num)
            nums.append(num)
            nums.append(num)
        i += 1
        num = numrandom(i)
        nums.append(num)
        random.shuffle(nums)
        tests.append(nums.__str__())
    tests = "\n".join(tests)
    return tests
