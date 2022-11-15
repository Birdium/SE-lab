import random


class Generator:

    @staticmethod
    def random_int(lower, upper):
        return random.randint(lower, upper + 1)

    def random_char(self):
        return random.choice(self.__alphabet__)

    def random_str(self, lower, upper):
        rand_str = ""
        rand_len = self.random_int(self, lower, upper)
        for i in rand_len:
            rand_str.append(self.random_char())
        return rand_str

    def __init__(self, stdin_format):
        self.__alphabet__ = "qwertyuiopasdfghjklzxcvbnm"
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

