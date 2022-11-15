from inputter import Inputter
from checker import Checker
from generator import Generator

input_path = "input"
output_path = "output"


def main():
    inputter = Inputter(input_path)
    gene_format = inputter.get_format()
    generator = Generator(gene_format)
    p_list = inputter.get_programs()
    eq_pairs, neq_pairs = Checker.check_list(p_list, generator)


if __name__ == "__main__":
    main()
