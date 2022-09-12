import unittest

class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1

    def run(self):
        self.testMethod()


if __name__ == "__main__":
    test = WasRun("testMethod")
    assert test.wasRun == None
    test.run()
    assert test.wasRun == 1
