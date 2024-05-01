class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i , j = 0 ,0
        for x in pushed:
            pushed[i] = x
            while i>= 0 and j<len(popped) and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0