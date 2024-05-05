dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        tot = 0
        for i in range(1, len(s)):
            next_value = dictionary[s[i]]
            current_value = dictionary[s[i-1]]
            if current_value < next_value:
                tot -= current_value
            else:
                tot += current_value
        tot += dictionary[s[-1]]
        return tot