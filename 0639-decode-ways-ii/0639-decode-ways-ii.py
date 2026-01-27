class Solution: 
    def numDecodings(self, s):
        """
        if i < 0, we return 1, there is only one way to decode empty string.
if s[i] == *, then there is 9*dp(i-1) ways to decode if we take last number 1-digit. To decode last number 2-digit we need to consider several cases. If we have 1*, then we have 9 ways to replace * with [1, 2, ..., 9]. If we have 2*, then we have 6 ways to replace it with [1, 2, ..., 6]. Finally, if we have **, then we have 15 options: [11, ...., 19, 21, ..., 26].
if s[i] != *, that it it is digit, we have dp(i-1) ways to decode if we have last digit not equal to 0 and 0 ways if it is zero. For last 2 digits we need again consider cases: if previous element is digit, then only case [10, ..., 26] will be good for as, so we add dp(i-2). If we have *., then if . = 0, 1, 2, 3, 4, 5, 6, then we have 2 options for *: 1 and 2, in other case we have only one option.
Complexity
It is O(n) for time and space.

        """
        M = 10**9 + 7 
        
        @lru_cache(None)
        def dp(i):
            if i < 0: return 1
            if s[i] == "*":
                corr = {"1": 9, "2": 6, "*":15}
                ans = 9*dp(i-1)
                if i > 0: ans += corr.get(s[i-1], 0)*dp(i-2)
                return ans % M
            
            ans = dp(i-1) if s[i] != "0" else 0
            if i > 0 and "10" <= s[i-1:i+1] <= "26":
                ans += dp(i-2)
            elif i > 0 and s[i-1] == "*":
                ans += (2 if s[i] <= "6" else 1)*dp(i-2)
           
            return ans % M
        
        return dp(len(s)-1) % M