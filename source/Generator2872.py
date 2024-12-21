import random
import math
'''
2872 - Maximum Number of K-Divisible Components
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 3*10**4
    minval = 0
    maxval = 10**9

    probability = 5
    for n in [min_num, 
              min_num+1,
              100,
                1000,
                max_num//4*3,
                max_num-2,
                max_num-1,
                max_num]:
        if n == max_num - 1:
            probability = 1
        if n == max_num:
            probability = 0
        values = [random.randint(minval, maxval) for _ in range(n)]
        k = random.randint(1,maxval)
        nodes = list(range(n))
        random.shuffle(nodes)
        root = nodes.pop()
        leafs = [root]
        edges = []
        neighbors = [[] for _ in range(n)]
        while nodes:
            localroot = leafs.pop(random.randint(0,len(leafs)-1))
            edges.append([localroot, nodes[-1]])
            neighbors[localroot].append(nodes[-1])
            leafs.append(nodes.pop())
            if len(nodes) > 1 and random.randint(0,1):
                edges.append([localroot, nodes[-1]])
                neighbors[localroot].append(nodes[-1])
                leafs.append(nodes.pop())

        
        loose = [root]
        connected = []
        while loose:
            node = loose.pop()
            connected.append(node)
            connectedsum = 0
            while connected:
                node = connected.pop()
                connectedsum += values[node]
                while neighbors[node]:
                    neighbor = neighbors[node].pop()
                    if random.randint(0,probability) == 0:
                        # don't connect
                        loose.append(neighbor)
                    else:
                        # connect
                        connected.append(neighbor)
            values[node] = k - ((connectedsum-values[node])%k)


            #random.shuffle(leafs)
        test = "\n".join([str(x) for x in [n, edges,values, k]])
        tests.append(test.__str__().replace(' ', ''))
        
    return '''
'''.join(tests)
