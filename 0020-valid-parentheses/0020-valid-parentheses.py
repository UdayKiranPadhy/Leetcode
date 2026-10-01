class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        string=s
        closing={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in string:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    if closing[i]==stack[-1]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False