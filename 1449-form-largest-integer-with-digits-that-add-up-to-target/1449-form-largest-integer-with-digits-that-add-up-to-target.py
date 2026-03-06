class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        sys.set_int_max_str_digits(10000)
        self.d = {}
        def top_down(t):
            if t == 0: return 0
            if t in self.d: return self.d[t]
            cur = float('-inf')
            for digit in range(1,10):
                if (t-cost[digit-1]) >= 0:
                    cur = max(cur, top_down(t-cost[digit-1])*10+digit)
            self.d[t] = cur
            return cur

        res = top_down(target)
        return str(res) if res != float('-inf') else "0"