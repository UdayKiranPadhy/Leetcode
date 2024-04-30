class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        seen_sum = {0: 1}
        prefix = 0
        result = 0
        for char in word:
            prefix = prefix ^ (1 << (ord(char) - ord('a')))
            if prefix in seen_sum:
                result += seen_sum[prefix]
            if prefix in seen_sum:
                seen_sum[prefix] += 1
            else:
                seen_sum[prefix] = 1
            for j in range(10):
                if (prefix ^ (1 << j)) in seen_sum:
                    result += seen_sum[prefix ^ (1 << j)]
        return result