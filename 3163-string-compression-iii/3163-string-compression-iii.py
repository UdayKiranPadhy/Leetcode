class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        comp = []
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
                if count == 9:
                    comp.append(f"{count}{word[i - 1]}")
                    count = 0
            else:
                if count > 0:
                    comp.append(f"{count}{word[i - 1]}")
                count = 1
        
        # Handle the last sequence
        if count > 0:
            comp.append(f"{count}{word[-1]}")

        return ''.join(comp)
