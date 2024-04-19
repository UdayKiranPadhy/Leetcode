class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        q = deque(sorted(tokens))
        
        while q and (q[0] <= power or score):
            if power>= q[0]:
                power -= q[0]
                q.popleft()
                score += 1
            else:
                score -= 1
                power += q[-1]
                q.pop()
            
            res = max(res,score)
        return res