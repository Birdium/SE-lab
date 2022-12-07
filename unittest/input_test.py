import unittest
from inputter import Inputter


class MyTestCase(unittest.TestCase):
    def test_format(self):
        inputter_1 = Inputter(r"tests/inputter1")
        format_1 = inputter_1.get_format()
        self.assertTrue(format_1[0][0].get_type() == 'int')
        self.assertTrue(format_1[0][0].get_lower() == 1)
        self.assertTrue(format_1[0][0].get_upper() == 2)
        self.assertTrue(format_1[0][1].get_type() == 'string')
        self.assertTrue(format_1[0][1].get_lower() == 2)
        self.assertTrue(format_1[0][1].get_upper() == 3)

        inputter_2 = Inputter(r"tests/inputter2")
        format_2 = inputter_2.get_format()
        self.assertTrue(format_2[0][0].get_type() == 'int')
        self.assertTrue(format_2[0][0].get_lower() == 114)
        self.assertTrue(format_2[0][0].get_upper() == 514)
        self.assertTrue(format_2[0][1].get_type() == 'int')
        self.assertTrue(format_2[0][1].get_lower() == 191)
        self.assertTrue(format_2[0][1].get_upper() == 9810)

        inputter_3 = Inputter(r"tests/inputter3")
        format_3 = inputter_3.get_format()
        self.assertTrue(format_3[0][0].get_type() == 'int')
        self.assertTrue(format_3[0][0].get_lower() == 114)
        self.assertTrue(format_3[0][0].get_upper() == 514)
        self.assertTrue(format_3[0][1].get_type() == 'int')
        self.assertTrue(format_3[0][1].get_lower() == 191)
        self.assertTrue(format_3[0][1].get_upper() == 9810)
        self.assertTrue(format_3[1][0].get_type() == 'char')
        self.assertTrue(format_3[1][1].get_type() == 'char')
        self.assertTrue(format_3[1][2].get_type() == 'char')
        self.assertTrue(format_3[1][3].get_type() == 'char')
        self.assertTrue(format_3[1][4].get_type() == 'char')
        self.assertTrue(format_3[2][0].get_type() == 'string')
        self.assertTrue(format_3[2][0].get_lower() == 19)
        self.assertTrue(format_3[2][0].get_upper() == 19)

    def test_program(self):
        inputter_1 = Inputter(r"tests/inputter1")
        program_1 = inputter_1.get_programs()
        prog_dir_1 = [prog.get_dir() for prog in program_1]
        std_dir_1 = ['tests/inputter1/48762087.cpp', 'tests/inputter1/84822638.cpp', 'tests/inputter1/84822639.cpp',
                     'tests/inputter1/101036360.cpp', 'tests/inputter1/117364748.cpp', 'tests/inputter1/127473352.cpp',
                     'tests/inputter1/134841308.cpp', 'tests/inputter1/173077807.cpp']
        self.assertEqual(len(prog_dir_1), len(std_dir_1))
        self.assertTrue(len(set(prog_dir_1).difference(set(std_dir_1))) == 0)

        inputter_2 = Inputter(r"tests/inputter2")
        program_2 = inputter_2.get_programs()
        prog_dir_2 = [prog.get_dir() for prog in program_2]
        std_dir_2 = ['tests/inputter2/21508887.cpp', 'tests/inputter2/21508898.cpp', 'tests/inputter2/21715601.cpp',
                     'tests/inputter2/29019948.cpp']
        self.assertEqual(len(prog_dir_2), len(std_dir_2))
        self.assertTrue(len(set(prog_dir_2).difference(set(std_dir_2))) == 0)

        inputter_3 = Inputter(r"tests/inputter3")
        program_3 = inputter_3.get_programs()
        prog_dir_3 = [prog.get_dir() for prog in program_3]
        std_dir_3 = ['tests/inputter3/30534178.cpp', 'tests/inputter3/31034693.cpp', 'tests/inputter3/33794240.cpp',
                     'tests/inputter3/36641065.cpp']
        self.assertEqual(len(prog_dir_3), len(std_dir_3))
        self.assertTrue(len(set(prog_dir_3).difference(set(std_dir_3))) == 0)


if __name__ == '__main__':
    unittest.main()
