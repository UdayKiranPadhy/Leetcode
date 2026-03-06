class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        N = len(s)

        @cache
        def go(index):
            if index >= N:
                return 1
            if s[index] == '0':
                return 0
            
            total = 0
            for i in range(index+1,N+1):
                if int(s[index:i]) > k:
                    break
                total += go(i)
            return total % (10**9 + 7)
        
        return go(0) % (10**9 + 7)