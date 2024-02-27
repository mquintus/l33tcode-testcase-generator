"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import time
import os
import importlib
from typing import Callable
import re

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


def write_testcase(tests):
    """Convert test cases into strings, add line breaks and write out.
    """
    write_file(tests)


def check_exists_testcase(id: int) -> bool:
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, "source", f"Generator{id}.py")
    print(full_path)
    return os.path.exists(full_path)


def get_generator(id: int) -> Callable:
    current_dir = os.getcwd()
    module_path = f"{current_dir}/source/Generator{id}.py"
    # Specify that you want to import from a source file
    spec = importlib.util.spec_from_file_location(f"Generator{id}.py", module_path)
    # Dynamically import the module
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the function from the module
    generator = getattr(module, "generate")
    # Call the function and return the result
    return generator    


def get_existing_testcases() -> list:
    ids = []
    pattern = r"Generator(\d+)\.py"
    for filename in os.listdir("source"):
        match = re.match(pattern, filename)
        if match:
            number = match.group(1)
            ids.append(number)
    return ids


#placeholder
last_implemented = 1658

def main(challenge_id, e):
    tests = []
    if e:
        existing = get_existing_testcases()
        print("\n".join(existing))
        return 0
        
    if int(challenge_id) == -1:
        challenge_id = last_implemented

    if check_exists_testcase(challenge_id):
        generator = get_generator(challenge_id)
        tests = generator()
    else:
        print("Required argument challenge_id: must be a value of already implemented challenges.")
        print("To see already implemented challenges run generate_testcases.py -e")
        return -1

    date = time.time()
    filename = f"testcase_{challenge_id}_{int(date)}.txt"
    write_file(filename, tests)
    print("Testcases written to", filename)
    return 0
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate testcases for a challenge")
    parser.add_argument("challenge_id", nargs='?', help="The challenge id", default=-1, type=int)
    parser.add_argument("-e", "--exists", action="store_true", help="Show already implemented generators", default=False)
    args = parser.parse_args()
    main(args.challenge_id, args.exists)
    
