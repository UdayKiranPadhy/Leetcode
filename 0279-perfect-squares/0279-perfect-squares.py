class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([[n,0]])
        while q:
            poped_element, depth = q.popleft()
            for i in range(1,101):
                if i**2 > poped_element:
                    break
                else:
                    if poped_element - i**2 == 0:
                        return depth + 1
                    q.append([poped_element - i**2 , depth + 1])
