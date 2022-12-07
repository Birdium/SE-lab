import unittest
from inputter import Inputter
from generator import Generator

class MyTestCase(unittest.TestCase):
    def test_input_gene(self):
        inputter_1 = Inputter(r"tests/inputter4")
        format_1 = inputter_1.get_format()
        generator_1 = Generator(format_1)
        for _ in range(10):
            test_str = generator_1.gen_test()
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
