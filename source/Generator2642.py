import random
from .helpers import helpers

'''
2642 - Design Graph With Shortest Path Calculator
'''
def generate() -> str:
    tests = []
    min_nodes = 1
    max_nodes = 100

    min_cost = 1
    max_cost = 200

    # Test case 1
    num_nodes = min_nodes
    actions = ["Graph"]
    dag = []
    inputs = [[num_nodes, dag]]
    actions.append('shortestPath')
    inputs.append([0, 0])
    actions.append('shortestPath')
    inputs.append([0, 0])
    test = f"{actions}\n{inputs}".replace(' ', '').replace("'", '"')
    tests.append(test)

    # More test cases
    for num_nodes in [3,20,max_nodes]:
        for num_edges in [num_nodes, num_nodes*5]:
            dag = helpers.generate_random_dag(num_nodes, num_edges, min_cost, max_cost)
            edge_exists = {}
            for orig, dest, _ in dag:
                edge_exists[(orig, dest,)] = True
            inputs = [[num_nodes, dag]]
            actions = ["Graph"]
            number_of_actions = min(99, num_nodes**2)
            for _ in range(number_of_actions):
                add_edge = (random.randint(0,1) == 0)
                if add_edge:
                    new_orig = random.randint(0, num_nodes-2)
                    new_dest = random.randint(new_orig+1, num_nodes-1)
                    new_cost = random.randint(min_cost, max_cost)
                    if (new_orig, new_dest,) in edge_exists:
                        #print(f"Edge {new_orig} {new_dest} already exists")
                        # Edge already exists. Don't add this edge
                        continue
                    #print(f"Add edge {new_orig} {new_dest}")
                    edge_exists[(new_orig, new_dest,)] = True
                    # Edge doesn't exist. Add action.
                    action = 'addEdge'
                    actions.append(action)
                    inputs.append([[new_orig, new_dest, new_cost]])
                else:
                    new_orig = random.randint(0, num_nodes-2)
                    new_dest = random.randint(new_orig, num_nodes-1)
                    action = 'shortestPath'
                    actions.append(action)
                    inputs.append([new_orig, new_dest])
            test = f"{actions}\n{inputs}".replace(' ', '').replace("'", '"')
            tests.append(test)

    return '''
'''.join(tests)
