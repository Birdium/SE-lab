import os.path
import csv


class Outputter:

    def __init__(self, eq_pairs, neq_pairs, output_dir):
        self.__output_dir__ = output_dir
        self.__eq_pairs__ = eq_pairs
        self.__neq_pairs__ = neq_pairs

    def write_csv(self):
        eq_csv_path = os.path.join(self.__output_dir__, "output", "equal.csv")
        neq_csv_path = os.path.join(self.__output_dir__, "output", "inequal.csv")
        with open(eq_csv_path, "w", encoding='utf-8', newline='') as eq_csv:
            writer = csv.writer(eq_csv)
            writer.writerows(self.__eq_pairs__)
        with open(neq_csv_path, "w", encoding='utf-8', newline='') as neq_csv:
            writer = csv.writer(neq_csv)
            writer.writerows(self.__neq_pairs__)
