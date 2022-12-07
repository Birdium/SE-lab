import unittest
from inputter import Inputter
from checker import Checker
from generator import Generator


class MyTestCase(unittest.TestCase):
    def test_input_checker(self):
        inputter_1 = Inputter(r"tests/inputter3")
        format_1 = inputter_1.get_format()
        programs_1 = inputter_1.get_programs()
        generator_1 = Generator(format_1)
        eq_1, neq_1 = Checker.check_list(programs_1, generator_1)
        self.assertEqual(len(eq_1) + len(neq_1), len(programs_1) * (len(programs_1) - 1) / 2)


if __name__ == '__main__':
    unittest.main()
