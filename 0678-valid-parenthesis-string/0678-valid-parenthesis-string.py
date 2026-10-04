class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)

        @cache
        def valid(index,level):
            if index == N and level == 0:
                return True
            if index >= N:
                return False
            if level < 0:
                return False
            if s[index] == '(':
                return valid(index+1,level + 1)
            elif s[index] == ')':
                return valid(index+1,level - 1)
            else:
                return valid(index+1, level +1) or valid(index+1, level -1) or valid(index+1,level)
        
        return valid(0,0)