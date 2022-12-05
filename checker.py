class Checker:
    TIMES = 10

    @staticmethod
    def equiv(ret1, ret2):
        if ret1.returncode == ret2.returncode:
            return ret1.returncode != 0 or ret1.stdout == ret2.stdout
        return False

    @staticmethod
    def check_pair(program_1, program_2, generator):
        for _ in range(Checker.TIMES):
            str_in = generator.gen_test()
            ret1 = program_1.run(str_in)
            ret2 = program_2.run(str_in)
            if not Checker.equiv(ret1, ret2):
                return False
        return True

    @staticmethod
    def check_list(p_list, generator):
        eq_pairs = []
        neq_pairs = []
        for i_1, program_1 in enumerate(p_list):
            for i_2 in range(i_1):
                program_2 = p_list[i_2]
                if Checker.check_pair(program_1, program_2, generator):
                    eq_pairs.append([program_1, program_2])
                else:
                    neq_pairs.append([program_1, program_2])
        return eq_pairs, neq_pairs
