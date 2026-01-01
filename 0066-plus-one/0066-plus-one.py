class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        gg = ''
        for i in digits:
            gg += str(i)
        gg = str(int(gg) + 1)
        return [int(i) for i in gg]