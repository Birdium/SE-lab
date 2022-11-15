class Checker:
    TIMES = 10

    @staticmethod
    def equiv(ret1, ret2):
        if ret1.returncode == ret2.returncode:
            return ret1.returncode != 0 or ret1.stdout == ret2.stdout

    @staticmethod
    def check_pair(p1, p2, generator):
        for _ in range(Checker.TIMES):
            str_in = generator.gen_test()
            ret1 = p1.run(str_in)
            ret2 = p2.run(str_in)
            if not Checker.equiv(ret1, ret2):
                return False
        return True

    @staticmethod
    def check_list(p_list, generator):
        eq_pairs = []
        neq_pairs = []
        for i1 in range(len(p_list)):
            for i2 in range(i1):
                p1 = p_list[i1]
                p2 = p_list[i2]
                if Checker.check_pair(p1, p2, generator):
                    eq_pairs.append([p1, p2])
                else:
                    neq_pairs.append([p1, p2])
        return eq_pairs, neq_pairs
