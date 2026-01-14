class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        @cache
        def go(number):
            if number == 0: return 0
            if number == 1: return 1

            if number%2==0: return go(number//2)
            else: return 1 + go(number//2)
        
        for i in range(0,n+1):
            ans.append(go(i))
        
        return ans
