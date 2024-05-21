class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        N, ans = len(s), []

        def solve(index, subset):
            if index == N:
                ans.append(subset)
                return
            if s[index].isdigit():
                solve(index+1, subset + s[index])
            else:
                solve(index+1, subset + s[index].lower())
                solve(index+1, subset + s[index].upper())
        
        solve(0,"")
        return ans