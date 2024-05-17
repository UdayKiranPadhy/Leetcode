class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        vacancy = []
        available = []
        for profit , cap in zip(profits,capital):
            heappush(available, [cap,profit])
        
        while k:
            while available and available[0][0] <= w:
                cap , profit = heappop(available)
                heappush(vacancy, [-profit,cap])
            
            if vacancy:
                profit , cap = heappop(vacancy)
                w -= profit
                k -= 1
            else:
                break
        return w