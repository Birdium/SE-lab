import unittest
import os
from outputter import Outputter
from program import Program

class MyTestCase(unittest.TestCase):
    def test_output(self):
        program_1 = Program('tests/inputter1/134841308.cpp')
        program_2 = Program('tests/inputter1/48762087.cpp')
        program_3 = Program('tests/inputter1/84822638.cpp')
        eq_list1 = [[program_1, program_2]]
        neq_list1 = [[program_1, program_3], [program_2, program_3]]
        out_1 = Outputter(eq_list1, neq_list1, 'tests')
        if os.path.exists('tests/equal.csv'):
            os.remove('tests/equal.csv')
        if os.path.exists('tests/inequal.csv'):
            os.remove('tests/inequal.csv')
        out_1.write_csv()
        self.assertTrue(os.path.exists('tests/equal.csv'))
        self.assertTrue(os.path.exists('tests/inequal.csv'))
        if os.path.exists('tests/equal.csv'):
            os.remove('tests/equal.csv')
        if os.path.exists('tests/inequal.csv'):
            os.remove('tests/inequal.csv')

if __name__ == '__main__':
    unittest.main()
