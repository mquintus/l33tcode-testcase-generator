import random


def generate() -> str:
    tests = []
    maxworth = 10**4
    maxval = 10**5
    for eventslength in [maxval//4, maxval//16, maxval//7, maxval, 1]:
        events = []
        for i in range(0, eventslength):
            start = i + 1
            end = min(eventslength, 1 + i + random.randint(0, 10))
            k = min(eventslength, maxval // eventslength)
            events.append([start,
                           end,
                           random.randint(1, maxworth)])
        tests.append(events.__str__() + '\n' + str(k))
    tests.append("[[21,77,43],[2,74,47],[6,59,22],[47,47,38],[13,74,57],[27,55,27],[8,15,8]]\n4")

    return "\n".join(tests)
