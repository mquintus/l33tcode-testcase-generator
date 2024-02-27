from source.helpers.helpers import get_testcase_random, get_testcase_uniform

def generate() -> list:
    tests = []
    tests.extend(
        [
            get_testcase_random(),
            get_testcase_random(),
            get_testcase_random(),
            get_testcase_uniform(),
            get_testcase_uniform(),
        ]
    )
    tests = "\n".join([kwa.__str__() for kwa in tests])
    return tests
