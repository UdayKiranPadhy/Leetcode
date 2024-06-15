class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        heights = [0] * (N + 1)

        for start , end , direction in shifts:
            if direction:
                heights[start] += 1
                heights[end + 1] -= 1
            else:
                heights[start] -= 1
                heights[end + 1] += 1
        
        heights = list(accumulate(heights))

        alpha = "abcdefghijklmnopqrstuvwxyz"

        res = ""
        for idx , char in enumerate(s):
            res += alpha[(alpha.index(char) + heights[idx] ) % 26]
        return res