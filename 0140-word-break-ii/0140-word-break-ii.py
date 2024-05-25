class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        ans = []
        words = set(wordDict)

        def go(index, current):
            if index == N:
                ans.append(" ".join(current))
                return

            for i in range(index, N+1):
                if s[index:i] in words:
                    current.append(s[index:i])
                    go(i, current)
                    current.pop()

        go(0, [])
        return ans