class Solution:
    def countAndSay(self, n: int) -> str:
        def create_sequence(seq):
            prev_letter, cur_count = None, 0
            ret = []
            for l in seq:
                if prev_letter and l != prev_letter:
                    ret.extend([str(cur_count), prev_letter])
                    cur_count = 1
                else:
                    cur_count += 1
                prev_letter = l
            ret.extend([str(cur_count), prev_letter])
            return "".join(ret)
        
        seq = "1"
        for i in range(1, n):
            seq = create_sequence(seq)
        return seq