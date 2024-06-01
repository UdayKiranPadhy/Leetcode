class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        N = len(s)
        for i in range(1,N):
            score += abs(ord(s[i-1]) - ord(s[i]))
        return  score