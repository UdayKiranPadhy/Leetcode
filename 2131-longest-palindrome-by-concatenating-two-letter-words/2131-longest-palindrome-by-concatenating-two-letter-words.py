class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = Counter(words)
        ans = 0
        
        # Handeling non equal elements
        for word, freq in word_dict.items():
            if word == word[::-1]:
                continue
            reverse = word[::-1]
            if reverse not in word_dict:
                continue
            pairs = min(freq,word_dict[reverse])
            word_dict[word] -= pairs
            word_dict[reverse] -= pairs
            ans += 4*pairs
        
        # Handeling equal elements
        odd = 0
        for word , freq in word_dict.items():
            if word != word[::-1]:
                continue
            if freq%2 == 1:
                odd = 1
            ans += 4*(freq//2)
        if odd:
            ans += 2
        return ans