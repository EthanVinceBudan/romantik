from os import listdir
from importlib import import_module as string_import
from argparse import ArgumentParser
from unittest import TextTestRunner, defaultTestLoader, TestSuite

from . import test_performance

SEARCH_PATTERN = "test_"
SEARCH_BLACKLIST = ["performance"]

def get_functional_testing_modules():
    foundModules = []
    for fileName in listdir(__package__):
        if (SEARCH_PATTERN in fileName) and (fileName not in SEARCH_BLACKLIST):
            # remove ".py" from filename
            foundModules.append(fileName.split(".")[0])
    
    index = 0
    skippedModules = []
    while index < len(foundModules):
        for item in SEARCH_BLACKLIST:
            if item in foundModules[index]:
                skippedModules.append(foundModules.pop(index))
                continue
            index += 1
    return (foundModules, skippedModules)


def create_functional_testing_suite(moduleNames):
    suite = TestSuite()
    for mString in moduleNames:
        # add leading "." to make import relative to module
        mHandle = string_import(f".{mString}", __package__)
        suite.addTest(defaultTestLoader.loadTestsFromModule(mHandle))
    return suite
    
    
if __name__ == "__main__":
    parser = ArgumentParser(
        prog="python -m test"
    )
    parser.add_argument("-v", "--verbose", action='store_const',
            default=1, const=2, help="Display verbose output")
    parser.add_argument("-p", "--performance",
            action='store_true', help="Include performance-related tests")
    args = parser.parse_args()
    
    runner = TextTestRunner(verbosity=args.verbose)
    print("Discovering test modules... ", end="")
    accepted, skipped = get_functional_testing_modules()
    print(f"found {len(accepted)}, skipped {len(skipped)}")
    if args.verbose > 1:
        print(f"Modules to test: {accepted}")
        print(f"Modules skipped: {skipped}")
    print(" Starting Functional Tests ".center(70, '='))
    functionalTestSuite = create_functional_testing_suite(accepted)
    runner.run(functionalTestSuite)
    if args.performance:
        performanceTestSuite = defaultTestLoader.loadTestsFromModule(
                test_performance)
        print("\n\n" + " Starting Performance Tests ".center(70, '='))
        runner.run(performanceTestSuite)
