class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N , bad_index = len(s), -1
        stack = []
        best = 0

        for right in range(N):
            if s[right] == '(':
                stack.append(right)
            else:
                if len(stack):
                    stack.pop()
                    if stack:
                        current = right - stack[-1]
                    else:
                        current = right - bad_index
                    best = max(best , current)
                else:
                    bad_index = right
        return best