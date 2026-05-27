from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapping = defaultdict(list)
        for idx, char in enumerate(word):
            if char.islower():
                mapping[char].append(idx)
        specail = set()
        for idx, letter in enumerate(word):
            if letter.isupper():
                if letter.lower() in mapping:
                    if mapping[letter.lower()][-1] < idx:
                        specail.add(letter)
                    else:
                        del mapping[letter.lower()]
        return len(specail)

