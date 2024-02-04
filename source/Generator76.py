import random

'''
76 - Minimum Window Substring
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    somechars = ""
    otherchars= ""

    # To make sure that non-anagram strings are tested
    # We have to use different alphabets for the two strings
    for char in range(ord('a'), ord('z')+1):
        somechars += chr(char)
    for char in range(ord('A'), ord('Z')+1):
        otherchars += chr(char)


    n = min_num
    # Two different chars
    string1 = random.choice(somechars)
    string2 = random.choice(otherchars)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    n = min_num
    # Two identical chars
    string1 = random.choice(somechars)
    test = f'"{string1}"\n"{string1}"'
    tests.append(f'{test}')


    def interwieve_lists(s1, s2):
        #print(s1)
        #print(s2)
        result = []
        for i in range(min(len(s2), len(s1))):
            result.append(s1[i])
            result.append(s2[i])
        return result

    # Testcases 3 - Exact solution
    n = 100
    search_chars = [random.choice(otherchars) for _ in range(23)]
    string2 = "".join(search_chars)
    string1 = [random.choice(somechars) for _ in range(n)]

    shortest_solution = 42
    start = random.randint(10, n - shortest_solution - 10)
    end = start + shortest_solution
    positions = interwieve_lists(list(range(start, start + shortest_solution//2)), list(range(end - 1, end - 1 - shortest_solution//2, -1)))
    #print(positions)
    while search_chars:
        char = search_chars.pop()
        string1[positions.pop(0)] = char
    string1 = "".join(string1)
    string2 = "".join(string2)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Testcase 4: s is longer than t
    n = 10
    char = random.choice(somechars)
    string1 = char * (n - 1)
    string2 = char * n
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    # Testcases 5, 6, 7
    n = max_num - 200
    for shortest_solution in [10, n//2, n-20]:
        shortest_chars = random.randint(2, shortest_solution)
        search_chars = [random.choice(otherchars[1:]) for _ in range(shortest_chars)]
        string2 = "".join(search_chars)
        string1 = [random.choice(somechars) for _ in range(n)]

        start = random.randint(10, n - shortest_solution - 10)
        end = start + shortest_solution
        positions = interwieve_lists(list(range(start, start + shortest_solution//2)), list(range(end - 1, end - 1 - shortest_solution//2, -1)))
        for p in positions:
            if not search_chars:
                break
            char = search_chars.pop()
            string1[p] = char
        string1.append(otherchars[0])
        string1 = "".join(string1)
        string1 = string2[:100] + string1
        string2 += otherchars[0]
        test = f'"{string1}"\n"{string2}"'
        tests.append(f'{test}')

    n = max_num - 100
    # Testcase 8: Random
    string1 = [random.choice(somechars) for _ in range(n)]
    search_chars = [random.choice(otherchars[1:]) for _ in range(shortest_chars)]
    string2 = "".join(search_chars)
    for i in range(1000):
        if not search_chars:
            break
        if random.randint(0, 1):
            string1[i] = search_chars.pop()
    string1[0] = otherchars[0]
    string2 += otherchars[0]
    string1 = "".join(string1)
    test = f'"{string1}"\n"{string2}"'
    tests.append(f'{test}')

    return "\n".join(tests)
