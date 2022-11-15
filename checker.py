class Checker:

    @staticmethod
    def check_pair(p1, p2, generator):
        str_in = generator.gen()
        result1 = p1.run(str_in)
        result2 = p2.run(str_in)
        return Checker.equiv(result1, result2)

    @staticmethod
    def check_list(p_list):
        eq_pairs = neq_pairs = []
        for i1 in range(len(p_list)):
            for i2 in range(p1):
                p1 = p_list[i1]
                p2 = p_list[i2]
                if (Checker.check_pair(p1, p2, generator)):
                    eq_pairs.append((p1, p2))
                else:
                    neq_pairs.append((p1, p2))
        return eq_pairs, neq_pairs
