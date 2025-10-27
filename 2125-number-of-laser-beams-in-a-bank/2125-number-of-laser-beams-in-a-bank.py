class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count the security devices of each row
        security_count = [row.count("1") for row in bank if row.count("1") > 0]
        
        if len(security_count) < 2:
            return 0 

        ans = 0
        for i in range(1,len(security_count)):
            ans += security_count[i-1] * security_count[i] 
        return ans