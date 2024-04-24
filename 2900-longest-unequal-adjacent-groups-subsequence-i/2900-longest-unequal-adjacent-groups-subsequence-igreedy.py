class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        mappings = defaultdict(list)
        N= len(words)
        for idx, letter in enumerate(words):
            mappings[groups[idx]].append(idx)
        idx = 0
        path = []
        current = 0
        while idx < N:
            find = bisect_left(mappings[current], idx)
            if find >= len(mappings[current]):
                break
            else:
                idx = mappings[current][find]
                path.append(words[idx])
                if current == 0:
                    current = 1
                else:
                    current = 0
        path2 = []
        current = 1
        idx = 0
        while idx < N:
            find = bisect_left(mappings[current], idx)
            if find >= len(mappings[current]):
                break
            else:
                idx = mappings[current][find]
                path2.append(words[idx])
                if current == 0:
                    current = 1
                else:
                    current = 0
        return path if len(path)  > len(path2) else path2