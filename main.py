import os

from inputter import Inputter
from checker import Checker
from generator import Generator
from outputter import Outputter

input_path = "input"
output_path = "output"


def main():
    eq_pairs = []
    neq_pairs = []
    for folder in os.listdir(input_path):
        folder_path = os.path.join(input_path, folder)
        inputter = Inputter(folder_path)
        gene_format = inputter.get_format()
        generator = Generator(gene_format)
        p_list = inputter.get_programs()
        new_eq_pairs, new_neq_pairs = Checker.check_list(p_list, generator)
        eq_pairs.extend(new_eq_pairs)
        neq_pairs.extend(new_neq_pairs)
    outputter = Outputter(eq_pairs, neq_pairs, output_path)
    outputter.write_csv()


if __name__ == "__main__":
    main()
