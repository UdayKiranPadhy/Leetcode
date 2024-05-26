cache = {}
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        def go(n,A,L):
            if n == 0:
                return 1
            total = 0
            if (n,A,L) in cache:
                return cache[(n,A,L)]
            for char in ('A','L','P'):
                if A == 1 and char == 'A':
                    continue
                if L == 2 and char == 'L':
                    continue
                if char == 'P':
                    total += go(n-1,A,0)
                elif char == 'A':
                    total += go(n-1,1,0)
                else:
                    total += go(n-1,A,L + 1)
            cache[(n,A,L)] = total % MOD
            return cache[(n,A,L)]

        return go(n,0,0)