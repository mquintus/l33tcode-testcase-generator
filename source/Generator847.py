import random

'''
847 - Shortest Path Visiting All Nodes
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 12

    '''
    n: number of nodes
    connection_probability x: 1/(x + 1)
    self_connect: add(1)/remove(0) loop?
    '''
    def get_graph_adjacency_matrix(n: int, connection_probability: int, self_connect=0) -> list:
        graph_adjacency = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if random.randint(0, connection_probability) == 0:
                    graph_adjacency[i][j] = 1
                    graph_adjacency[j][i] = 1
        for i in range(n):
            graph_adjacency[i][i] = self_connect
        return graph_adjacency

    def adjencency_to_neighbor_list(matrix) -> list:
        neighbors = []
        for i in range(len(matrix)):
            local_neighbors = []
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    local_neighbors.append(j)
            neighbors.append(local_neighbors)
        return neighbors

    for n in [min_num, max_num, max_num // 2, max_num - 2]:
        graph_adjacency = get_graph_adjacency_matrix(n, 1, self_connect=0)
        test = adjencency_to_neighbor_list(graph_adjacency)
        tests.append(test.__str__().replace(' ', ''))

    # ring, full size
    graph_adjacency = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        j = (i + 1) % n
        graph_adjacency[i][j] = 1
        graph_adjacency[j][i] = 1
    test = adjencency_to_neighbor_list(graph_adjacency)
    tests.append(test.__str__().replace(' ', ''))

    # fully meshed
    n = max_num
    graph_adjacency = get_graph_adjacency_matrix(n, 0, self_connect=0)
    test = adjencency_to_neighbor_list(graph_adjacency)
    tests.append(test.__str__().replace(' ', ''))

    # star topology
    graph_adjacency = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        j = n // 2
        if i != j:
            graph_adjacency[i][j] = 1
            graph_adjacency[j][i] = 1
    test = adjencency_to_neighbor_list(graph_adjacency)
    tests.append(test.__str__().replace(' ', ''))

    # deep star topology
    graph_adjacency = [[0 for i in range(n)] for j in range(n)]
    center = 0
    for j in range(0, 4):
        if j != center:
            graph_adjacency[center][j] = 1
            graph_adjacency[j][center] = 1
        deep1 = j + 4
        graph_adjacency[deep1][j] = 1
        graph_adjacency[j][deep1] = 1
        deep2 = j + 8
        graph_adjacency[deep1][deep2] = 1
        graph_adjacency[deep2][deep1] = 1
    test = adjencency_to_neighbor_list(graph_adjacency)
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
