class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        for i in range(N):
            if s[i:] + s[:i] == goal:
                return True
        return False
        