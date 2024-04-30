class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s,w):
            j , N = 0, len(s)
            for i in range(N):
                if j < len(w) and s[i] == w[j]: j+=1
                elif (i > 1 and s[i-2] == s[i-1] == s[i]) or (i+ 1< N and s[i-1] == s[i] == s[i+1]):
                    continue
                else: return False
            return j==len(w)
        return sum(check(s,word) for word in words)