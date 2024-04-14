class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        N = len(words)
        dp = [1] * N

        def isPredecessor(s , t):
            if len(s) + 1 != len(t) :return False
            for i in range(len(t)):
                if t[:i] + t[i+1:] == s:
                    return True
            return False
        
        for i in range(N):
            word = words[i]
            for j in range(i):
                if isPredecessor(words[j], word) and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
        
        return max(dp)
