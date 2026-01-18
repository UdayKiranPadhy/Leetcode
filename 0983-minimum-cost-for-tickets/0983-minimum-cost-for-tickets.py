class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        N = len(days)

        @cache
        def go(index):
            if index >= N:
                return 0
            # 1 day pass
            op1 = costs[0] + go(index+1)

            # 7 day pass
            j = index
            while j < N and days[j] < days[index] + 7:
                j+=1
            op2 = costs[1] + go(j)

            # 30 day pass

            j = index
            while j < N and days[j] < days[index] + 30:
                j += 1
            op3 = costs[2] + go(j)

            return min(op1,op2,op3)
        return go(0)