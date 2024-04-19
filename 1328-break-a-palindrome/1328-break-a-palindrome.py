class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        N = len(palindrome)
        palindrome  = list(palindrome)
        broke = False
        for i in range(N//2):
            if palindrome[i] != "a":
                if N % 2 != 0 and i == ceil(N/2):
                    continue
                else:
                    palindrome[i] = "a"
                    broke = True
                    break
        if broke:
            return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)