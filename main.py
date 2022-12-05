import os

from inputter import Inputter
from checker import Checker
from generator import Generator
from outputter import Outputter

INPUT_PATH = "input"
OUTPUT_PATH = "output"


def main():
    eq_pairs = []
    neq_pairs = []
    for folder in os.listdir(INPUT_PATH):
        folder_path = os.path.join(INPUT_PATH, folder)
        inputter = Inputter(folder_path)
        gene_format = inputter.get_format()
        generator = Generator(gene_format)
        p_list = inputter.get_programs()
        new_eq_pairs, new_neq_pairs = Checker.check_list(p_list, generator)
        eq_pairs.extend(new_eq_pairs)
        neq_pairs.extend(new_neq_pairs)
    outputter = Outputter(eq_pairs, neq_pairs, OUTPUT_PATH)
    outputter.write_csv()
    print("Success!")


if __name__ == "__main__":
    main()
