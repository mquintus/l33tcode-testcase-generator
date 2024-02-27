
def generate():
    trees = ["[]", "[1]"]
    tree = [1]
    tree.extend([1 for i in range(10 ** 5 - 1)])
    trees.append(tree.__str__())

    vals = [1, None]
    tree = [1]
    tree.extend([None for i in range(10 ** 5 - 1)])
    for i in range(150):
        if 2 ** i + 1 < len(tree):
            tree[2 ** i] = 1 
        else:
            break

    trees.append(tree.__str__())
    tests = "\n".join(trees)
    return tests
