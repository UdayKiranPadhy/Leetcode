class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_index = 0
        stack = []
        ops = []
        for i in range(1,n+1):
            if target_index == len(target):
                return ops
            stack.append(i)
            ops.append("Push")
            if stack[-1] == target[target_index]:
                target_index += 1
            else:
                ops.append("Pop")
                stack.pop()
        return ops