class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 10**6
        for i in strs:
            min_length = min(min_length , len(i))
        length = 0
        comefrombreak = False
        for i in range(min_length):
            to_find = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == to_find:
                    continue
                else:
                    comefrombreak = True
                    break
            if comefrombreak:
                break
            else:
                length += 1
        return strs[0][:length]