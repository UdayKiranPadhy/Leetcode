class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chair , current = 0, 0
        for char in s:
            if char == 'E':
                current += 1
            elif char == 'L':
                current -= 1
            max_chair = max(max_chair, current)
        return max_chair