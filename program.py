import os
import subprocess


class Program:

    @staticmethod
    def get_bin_dir(src_dir):
        portion = os.path.splitext(src_dir)
        if portion[1] == ".c++" or portion[1] == ".c":
            return portion[0] + ".out"

    def __init__(self, src_dir):
        self.__src_dir__ = src_dir
        self.__bin_dir__ = self.get_bin_dir(src_dir)
        args = ["g++", src_dir, "-o", self.__bin_dir__]
        proc = subprocess.run(args)

    def __del__(self):
        os.remove(self.__bin_dir__)

    @staticmethod
    def run(self, str_in):
        args = ["./" + str_in]
        return subprocess.run(args, input=str_in.encode())





