class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @cache
        def go(prev,length):
            if length == n:
                return 1
            total = 0
            for vowel in 'aeiou':
                if vowel > prev:
                    continue
                total += go(vowel,length + 1)
            return total

        best = 0
        for vowel in 'aeiou':
            best += go(vowel,1)
        return best