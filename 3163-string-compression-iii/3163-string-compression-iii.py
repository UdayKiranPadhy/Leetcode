class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        res = ""
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
                if count == 9:
                    res += f"{count}{word[i-1]}"
                    count = 0
            else:
                if count > 0:
                    res += f"{count}{word[i-1]}"
                count = 1
        
        # Handle the last sequence
        if count > 0:
            res += f"{count}{word[-1]}"

        return res
