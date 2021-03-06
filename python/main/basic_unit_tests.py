from colorama import Fore, Back, Style, init
init()


def printHeader(what):
    print()
    print(Fore.BLUE + what + Style.RESET_ALL)


def printGood(what):
    #print(Back.GREEN + 'and with a green background')
    #print(Style.DIM + 'and in dim text')
    print(Fore.GREEN + what + Style.RESET_ALL)


def printBad(what):
    print(Fore.RED + what + Style.RESET_ALL)


class basic_unit_tests:
    def __init__(self):
        self.testAt = 0
        self.kataName = "CodeWar unit tests"

    def describe(self, kataName):
        # Some have a describe method call before the tests, some don't.
        self.kataName = kataName

    def assert_equals(self, returned, expected, testName=''):
        expected_str = str(expected)
        returned_str = str(returned)
        if (self.testAt == 0):
            printHeader(" -- Running tests on " + self.kataName + " -- ")
        if (expected == returned):
            printGood("Test " + str(self.testAt) +
                      " passed with '" + str(returned) + "'")
        else:
            error = "Test " + str(self.testAt) + " failed."
            error += "\n" + "  Expected: " + expected_str
            error += "\n" + "  Returned: " + returned_str
            if (type(expected) != type(returned)):
                error += "\n" + "  !Different types!"
            printBad(error)
        self.testAt += 1
