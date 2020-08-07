import os

class Test:
    def __init__(self, name = "", arg_pairs = {}):
        self.name = name
        self.arg_pairs = arg_pairs


class EaaS:
    # TODO: configure with JSON file
    def __init__(self, cmd = ""):
        print("EaaS initialized")

        self.tests = []


    def run(self):
        i = 0
        for test in self.tests:
            i += 1
            print("Test " + str(i) + ": " + test.name)

            # stream = os.popen(cmd + " " + (str(key + "=" val + " ") for key, val in arg_pairs.items()))


    def create_test(self, name = "", arg_pairs = {}):
        test = Test(name, arg_pairs)

        self.tests.append(test)


    def reset_tests(self):
        self.tests = []
