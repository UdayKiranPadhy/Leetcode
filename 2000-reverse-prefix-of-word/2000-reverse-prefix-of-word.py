class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        for idx,value in enumerate(word):
            res += value
            if value ==ch:
                res = res[::-1]
                res += word[idx+1:]
                return res
        return res