class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        N = len(arr)
        stack = [start]

        while stack:
            index = stack.pop()
            if arr[index] == 0:
                return True
            
            right_idx = index + arr[index]
            if right_idx < N and right_idx not in seen:
                stack.append(right_idx)
                seen.add(right_idx)
            
            left_idx = index - arr[index]
            if left_idx >= 0 and left_idx not in seen:
                stack.append(left_idx)
                seen.add(left_idx)
        
        return False