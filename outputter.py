import os.path
import csv
from program import Program

class Outputter:

    def __init__(self, eq_pairs, neq_pairs, output_dir):
        self.__output_dir__ = output_dir
        self.__eq_pairs__ = [[p.get_dir() for p in pair] for pair in eq_pairs]
        self.__neq_pairs__ = [[p.get_dir() for p in pair] for pair in neq_pairs]

    def write_csv(self):
        eq_csv_path = os.path.join(self.__output_dir__, "equal.csv")
        neq_csv_path = os.path.join(self.__output_dir__, "inequal.csv")
        header = ['file1', 'file2']
        with open(eq_csv_path, "w", encoding='utf-8', newline='') as eq_csv:
            writer = csv.writer(eq_csv)
            writer.writerow(header)
            writer.writerows(self.__eq_pairs__)
        with open(neq_csv_path, "w", encoding='utf-8', newline='') as neq_csv:
            writer = csv.writer(neq_csv)
            writer.writerow(header)
            writer.writerows(self.__neq_pairs__)
