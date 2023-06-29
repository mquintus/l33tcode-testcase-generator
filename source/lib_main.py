"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import random

def write_file(filename: str, string: str):
    """A simple wrapper to write a string to a file.

    Does not allow override of an existing file.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        None
    """
    f = open(filename, "x")
    f.write(string)
    f.close()


def write_testcase(**kwargs):
    """Convert test cases into strings, add line breaks    and write out.
    """
    write_file("\n".join([kwa.__str__() for kwa in kwargs]))


"""Generate testcases for 1514_Path_with_Maximum_Probability.py
"""
def get_testcase_random() -> [int, list, list, int, int]:
    n,edges,succProb,start,end = get_testcase_uniform()
    succProb = [random.random() for i in range(len(succProb))]
    return n,edges,succProb,start,end

def get_testcase_min() -> [int, list, list, int, int]:
    n = 2
    start = 0
    end = 1
    edges = []
    succProb = []
    return n,edges,succProb,start,end

def get_testcase_uniform() -> [int, list, list, int, int]:
    n = 10**4
    start = 0
    end = 10**4 - 1
    edges = []
    succProb = []
    max_edge_count = 2*n
    for i in range(max_edge_count):
        a = random.randint(start,end)
        b = a
        while b == a or [a,b] in edges or [b,a] in edges:
            b = random.randint(start,end)
        edges.append([a, b])
        succProb.append(1)
    return n,edges,succProb,start,end

def run():
    tests = []
    tests.extend([
        get_testcase_random(),
        get_testcase_random(),
        get_testcase_random(),

        get_testcase_uniform(),
        get_testcase_uniform(),

        get_testcase_empty()
    ])

