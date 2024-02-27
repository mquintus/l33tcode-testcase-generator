import random
def generate():
    tests = []
    # min test
    number_of_nodes = 1
    graph = [[0, 0]]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    number_of_nodes = 2
    graph = [[0, 0], [1, 1]]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    number_of_nodes = 2
    graph = [[0, 1], [1, 0], [0, 0], [1, 1]]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    number_of_nodes = 5
    graph = []
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    number_of_nodes = 3
    graph = [[1, 1]]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    # giant loop
    number_of_nodes = 2000
    graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes)]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    # giant line
    number_of_nodes = 2000
    graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes - 1)]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    # giant reverse line
    number_of_nodes = 2000
    graph = [[i - 1, i] for i in range(1, number_of_nodes)]
    tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    number_of_nodes = 2000
    possible_edges = [i for i in range(number_of_nodes)]
    for test in range(4):
        graph = []
        number_of_edges_sum = 0
        for node in range(number_of_nodes):
            number_of_edges = random.randint(0, 4)
            number_of_edges_sum += number_of_edges
            edges = random.sample(possible_edges, number_of_edges)
            for e in edges:
                graph.append([node, e])
        print(number_of_edges_sum)
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

    for test in range(4):
        graph = []
        number_of_edges = 0
        number_of_edges_sum = 0
        for node in range(number_of_nodes):
            number_of_edges = random.randint(0, 10)
            number_of_edges_sum += number_of_edges
            if number_of_edges_sum >= 5000:
                number_of_edges_sum -= number_of_edges
                break
            edges = random.sample(possible_edges, number_of_edges)
            for e in edges:
                graph.append([node, e])
        print(number_of_edges, number_of_edges_sum)
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())
    tests = "\n".join(tests)
    return tests
