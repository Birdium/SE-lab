import random


class Generator:

    __alphabet__ = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    @staticmethod
    def random_int(lower, upper):
        return random.randint(lower, upper)

    @staticmethod
    def random_char():
        return random.choice(Generator.__alphabet__)

    @staticmethod
    def random_str(lower, upper):
        rand_str = ""
        rand_len = Generator.random_int(lower, upper)
        for _ in range(0, rand_len):
            rand_str = rand_str + Generator.random_char()
        return rand_str

    def __init__(self, stdin_format):
        self.__stdin_format__ = stdin_format

    def gen_test(self):
        test_str = ""
        for line in self.__stdin_format__:
            for elem in line:
                if elem.__type__ == "char":
                    test_str = test_str + self.random_char()
                if elem.__type__ == "int":
                    test_str = test_str + str(self.random_int(elem.get_lower(), elem.get_upper()))
                if elem.__type__ == "string":
                    test_str = test_str + self.random_str(elem.get_lower(), elem.get_upper())
                test_str = test_str + ' '
            test_str = test_str + '\n'
        return test_str
