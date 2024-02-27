import random
def generate():
    tests = []
    # min test
    graph = [[0]]
    tests.append(graph.__str__())

    graph = [[0], [1]]
    tests.append(graph.__str__())

    graph = [[0, 1], [0, 1]]
    tests.append(graph.__str__())

    graph = [[], [1], []]
    tests.append(graph.__str__())

    possible_edges = [i for i in range(10 ** 4 - 2)]
    for test in range(4):
        graph = []
        number_of_edges_sum = 0
        for node in range(10 ** 4 - 2):
            number_of_edges = random.randint(0, 6)
            number_of_edges_sum += number_of_edges
            graph.append(sorted(random.sample(possible_edges, number_of_edges)))
        print(number_of_edges_sum)
        tests.append(graph.__str__())

    for test in range(4):
        graph = []
        number_of_edges = 0
        number_of_edges_sum = 0
        for node in range(10 ** 4 - 2):
            number_of_edges = 6 - (node // 1500)
            number_of_edges %= len(possible_edges)
            graph.append(sorted(random.sample(possible_edges, number_of_edges)))
            number_of_edges_sum += number_of_edges
        print(number_of_edges, number_of_edges_sum)
        tests.append(graph.__str__())
    tests = "\n".join(tests)
    return tests
