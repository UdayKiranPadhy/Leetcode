class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ind = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[ind]:
                stack.pop()
                ind += 1
        return len(stack) == 0