import unittest
from generator import Generator
from element import Element


class MyTestCase(unittest.TestCase):
    def test_int(self):
        self.assertTrue(1 <= int(Generator.random_int(1, 4)) <= 4)
        self.assertTrue(11 <= int(Generator.random_int(11, 45)) <= 45)
        self.assertTrue(114 <= int(Generator.random_int(114, 514)) <= 514)

    def test_char(self):
        char_1 = Generator.random_char()
        self.assertTrue(ord('a') <= ord(char_1) <= ord('z') or ord('A') <= ord(char_1) <= ord('Z'))

    def test_str(self):
        str_1 = Generator.random_str(114, 514)
        self.assertIsInstance(str_1, str)
        for ch in str_1:
            self.assertTrue('a' <= ch <= 'z' or 'A' <= ch <= 'Z')

    def test_gen(self):
        test_format = [[('int', 1, 1), ('int', 4, 5), ('int', 1, 4)],
                       ['char', 'char', 'char'],
                       [('string', 19, 19), ('int', 8, 10)]]
        test_format = [[Element(elem) for elem in line] for line in test_format]
        test_generator = Generator(test_format)
        test_str = test_generator.gen_test()
        for lineno, line in enumerate(test_str.strip(' \n').split('\n')):
            for elemno, elem in enumerate(line.strip(' ').split(' ')):
                if lineno == 0:
                    if elemno == 0:
                        self.assertEqual(int(elem), 1)
                    elif elemno == 1:
                        self.assertTrue(4 <= int(elem) <= 5)
                    elif elemno == 2:
                        self.assertTrue(1 <= int(elem) <= 4)
                    else:
                        self.assertTrue(False)
                elif lineno == 1:
                    if 0 <= elemno <= 2:
                        self.assertTrue(ord('a') <= ord(elem) <= ord('z') or ord('A') <= ord(elem) <= ord('Z'))
                    else:
                        self.assertTrue(False)
                elif lineno == 2:
                    if elemno == 0:
                        self.assertIsInstance(elem, str)
                        self.assertTrue(len(elem) == 19)
                        for ch in elem:
                            self.assertTrue('a' <= ch <= 'z' or 'A' <= ch <= 'Z')
                    elif elemno == 1:
                        self.assertTrue(8 <= int(elem) <= 10)
                    else:
                        self.assertTrue(False)
                else:
                    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
