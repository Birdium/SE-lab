import random


class Generator:

    @staticmethod
    def random_int(self, lower, upper):
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
                if elem.type == "char":
                    test_str.append(self.random_char())
                if elem.type == "int":
                    test_str.append(str(self.random_int(elem.getlower(), elem.getupper())))
                if elem.type == "string":
                    test_str.append(self.random_str(elem.getlower(), elem.getupper()))
                test_str.append(' ')
            test_str.append('\n')
        return test_str

