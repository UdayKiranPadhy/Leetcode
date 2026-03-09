class Solution:
    def minSteps(self, N: int) -> int:
        
        @cache
        def go(n,clipboard,copied):
            if n == N:
                return 0
            if clipboard == -1:
                return 1 + go(n, n, True)
            else:
                op1 = op2 = float('inf')
                # Paste
                if n + clipboard <= N:
                    op1 = 1 + go(n + clipboard, clipboard, False)
                # Copy
                if not copied:
                    op2 = 1 + go(n, n, True)
                return min(op1, op2)
            return float('inf')

        return go(1,-1,False)