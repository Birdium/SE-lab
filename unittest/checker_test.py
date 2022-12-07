import unittest
from program import Program
from generator import Generator
from checker import Checker


class MyTestCase(unittest.TestCase):
    def test_checker(self):
        generator_1 = Generator([])
        progs_1 = [Program('tests/inputter1/48762087.cpp'),
                   Program('tests/inputter1/127473352.cpp'),
                   Program('tests/inputter1/134841308.cpp')]
        eq_1, neq_1 = Checker.check_list(progs_1, generator_1)
        print(eq_1, neq_1)
        for pair in eq_1:
            self.assertTrue(set(pair) == set(progs_1[1:3]))
        for pair in neq_1:
            self.assertTrue(set(pair) == set(progs_1[0:2]) or
                            set(pair) == set(progs_1[0:3:2]))



if __name__ == '__main__':
    unittest.main()
