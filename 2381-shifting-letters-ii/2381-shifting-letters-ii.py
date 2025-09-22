class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        result = [0] * (N+1)
        for start , end , di in shifts:
            if di == 1:
                result[start] += 1
                result[end+1] -= 1
            else:
                result[start] -= 1
                result[end+1] += 1

        currentShift = 0
        shiftList = list(s)
        for i in range(N):
            currentShift += result[i]
            netShift = (currentShift % 26 + 26) % 26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))
        return ''.join(shiftList)