import os
import re
from program import Program
from element import Element


class Inputter:

    @staticmethod
    def parse_format(self, path: str):
        result = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line_result = []
                for item in line.split(" "):
                    line_result.append(re.findall(r"(int)\((\d+):(\d+)\)", item))
                    line_result.append(re.findall(r"(string)\((\d+):(\d+)\)", item))
                    line_result.append(re.findall(r"(char)", item))
                line_result = map(line_result, Element)
                result.append(line_result)
        return result

    def get_format(self):
        return self.__stdin_format__

    def get_programs(self):
        return self.__programs__

    def __init__(self, path: str):
        self.__folder_path__ = path
        self.__programs__ = []
        for file in os.listdir(path):
            if file == "stdin_format.txt":
                self.__stdin_format__ = self.parse_format(file)
            else:
                self.__programs__.append(Program(file))
