class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)

        @cache
        def go(index):
            if index >= N:
                return 0
            
            op1 = op2 = op3 = -float('inf')

            op1 = stoneValue[index] - go(index+1)

            if index + 1 < N:
                op2 = stoneValue[index] + stoneValue[index+1] - go(index+2)
            
            if index + 2 < N:
                op3 = stoneValue[index] + stoneValue[index+1] + stoneValue[index+2] - go(index+3)
            
            return max(op1,op2,op3)
        
        result = go(0)
        if result > 0:
            return "Alice"
        if result < 0:
            return "Bob"
        return "Tie"