class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        @cache
        def go(i,deep):
            if deep == N:
                return 0
            
            op1 = op2 = float('inf')

            # op1
            op1 = triangle[deep][i] + go(i, deep + 1)
            
            if i+1 < len(triangle[deep]):
                op2 = triangle[deep][i+1] + go(i+1, deep + 1)

            return min(op1, op2)
        
        return go(0,0)