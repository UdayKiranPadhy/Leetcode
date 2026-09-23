class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        alpha_to_stickers = {}

        for idx , word in enumerate(stickers):
            for char in word:
                if char not in alpha_to_stickers:
                    alpha_to_stickers[char] = []
                alpha_to_stickers[char].append(idx)
        
        n = len(target)
        FULL_MASK = (1 << n) - 1

        @cache
        def go(mask):
            if mask == FULL_MASK:
                return 0
            
            find = -1

            for i in range(n):
                if not (mask & (1 << i)):
                    find = i
                    break
            
            ch = target[find]

            if ch not in alpha_to_stickers:
                return float('inf')
            
            ans = float('inf')
            
            for word_idx in alpha_to_stickers[ch]:
                word = stickers[word_idx]
                new_mask = mask

                for i in range(n):
                    if new_mask & (1<<i):
                        continue
                    if target[i] in word:
                        new_mask = new_mask | (1<<i)
                        word = word.replace(target[i],"",1)
                            # Sticker must make progress
                if new_mask != mask:
                    ans = min(ans, 1 + go(new_mask))
            
            return ans

        ans = go(0)

        return -1 if ans == float("inf") else ans