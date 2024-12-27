from colorama import Fore
import pprint

class Runner:
    def __init__(self, tests, solution):
        self.tests = tests
        self.solution = solution

    def run(self):
        for test in self.tests:
            args = test['args']
            expected = test['expected']
            result = self.solution(**args)
            assert result == expected, f"\nInput Args: {args}\nExpected: {expected}\nActual: {result}"
        print("All tests passed!")