
class Solution:
    def generateParenthesis(self, n):

        ans = []

        def backtrack(length , brackets,current):
            if length == 2*n and brackets == 0:
                ans.append(current[:])
                return
            if length == 2*n and brackets != 0:
                return
            
            if brackets + 1 <= n:
                backtrack(length + 1,brackets+1,current+"(")
            if brackets - 1 >= 0:
                backtrack(length+1,brackets - 1,current+")")
        
        backtrack(0,0,"")
        return ans