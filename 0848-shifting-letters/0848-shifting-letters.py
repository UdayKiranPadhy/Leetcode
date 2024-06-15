class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = list(accumulate(shifts[::-1]))
        shifts = shifts[::-1]

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        res = ""

        for idx, value in enumerate(s):
            res += alpha[ (alpha.index(value) + shifts[idx]) % 26]
        return res