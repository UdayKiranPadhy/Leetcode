class Solution:
    def compressedString(self, word: str) -> str:
        N = len(word)
        ans = ""
        current = 1
        for i in range(N-1):
            if word[i+1] == word[i]:
                current += 1
            else:
                while current > 9:
                    ans = ans + "9" + word[i]
                    current -= 9
                if current:
                    ans = ans + str(current) + word[i]
                current = 1
        else:
            while current > 9:
                ans = ans + "9" + word[-1]
                current -= 9
            if current:
                ans = ans + str(current) + word[-1]
        return ans