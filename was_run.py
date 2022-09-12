import unittest

class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1


if __name__ == "__main__":
    test = WasRun("testMethod")
    assert test.wasRun == None
    test.testMethod()
    assert test.wasRun == 1
