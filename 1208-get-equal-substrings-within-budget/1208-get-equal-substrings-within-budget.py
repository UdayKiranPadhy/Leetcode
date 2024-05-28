class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        count, N, max_length, left = 0, len(s), 0, 0
        for right in range(N):
            count += abs( ord(s[right]) - ord(t[right]) )

            while count > maxCost and left < right:
                count -= abs( ord(s[left]) - ord(t[left]) )
                left += 1
            
            max_length = max(right - left + 1, max_length)
        
        return max_length