import unittest
class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(1, "1")


def average(seq):
    return sum(seq) / len(seq)
class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError,average,[])
    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])
# if __name__ == "__main__":
#     unittest.main()

from collections import defaultdict
class StatsList(list):
    def mean(self):
        return sum(self) / len(self)
    def median(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx-1]) / 2
    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freq:
                modes.append(item)
        return modes


# from stats import StatsList

# class TestValidInputs(unittest.TestCase):
#     def setUp(self):
#         self.stats = StatsList([1,2,2,3,3,4])
#     def test_mean(self):
#             self.assertEqual(self.stats.mean(), 2.5)
#     def test_median(self):
#         self.assertEqual(self.stats.median(), 2.5)
#         self.stats.append(4)
#         self.assertEqual(self.stats.median(), 3)
#     def test_mode(self):
#         self.assertEqual(self.stats.mode(), [2,3])
#         self.stats.remove(2)
#         self.assertEqual(self.stats.mode(), [3])
# if __name__ == "__main__":
#     unittest.main()


import sys
class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)
    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)
    @unittest.skipIf(sys.version_info.minor == 4,"broken on 3.4")
    def test_skipif(self):
        self.assertEqual(False, True)
    @unittest.skipUnless(sys.platform.startswith('linux'),"broken unless on linux")
    def test_skipunless(self):
        self.assertEqual(False, True)
if __name__ == "__main__":
    unittest.main()


def setup_module(module):
    print("setting up MODULE {0}".format(module.__name__))
def teardown_module(module):
    print("tearing down MODULE {0}".format(module.__name__))
def test_a_function():
    print("RUNNING TEST FUNCTION")
class BaseTest:
    def setup_class(cls):
        print("setting up CLASS {0}".format(cls.__name__))
    def teardown_class(cls):
        print("tearing down CLASS {0}\n".format(cls.__name__))
    def setup_method(self, method):
        print("setting up METHOD {0}".format(method.__name__))
    def teardown_method(self, method):
        print("tearing down METHOD {0}".format(method.__name__))
class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")
    def test_method_2(self):
        print("RUNNING METHOD 1-2")
class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")
    def test_method_2(self):
        print("RUNNING METHOD 2-2")