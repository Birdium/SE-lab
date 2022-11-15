import os
import subprocess


class Program:

    @staticmethod
    def get_bin_dir(src_dir):
        portion = os.path.splitext(src_dir)
        return portion[0] + ".out"

    def get_dir(self):
        return self.__src_name__

    def __init__(self, src_dir):
        self.__src_name__ = src_dir
        self.__src_dir__ = os.path.abspath(src_dir)
        self.__bin_dir__ = self.get_bin_dir(src_dir)
        args = ["g++", self.__src_dir__, "-w", "-o", self.__bin_dir__]
        proc = subprocess.run(args)

    def __del__(self):
        os.remove(self.__bin_dir__)

    def run(self, str_in):
        args = [self.__bin_dir__]
        return subprocess.run(args, input=str_in.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)


