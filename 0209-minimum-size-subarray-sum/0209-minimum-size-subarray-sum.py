class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0 or nums == []:
            return 0
        
        #two pointers
        # i => fast ptr...thinks greedily..moves l to r and increases window size, thereby adding local sum
        # j => slow ptr...pulls back the window size, thereby satisfying the min_size_subarr_len objective (in simple terms it eliminates the elements from start of array)
        
        
        i, j, sum, local_len, min_len, length = 0, 0, 0, 0, float('inf'), len(nums)
        while i < length:
            
            #greedily increase window
            sum += nums[i]
            local_len += 1
            
            #pulling back window size
            while sum >= s:
                if local_len < min_len:
                    min_len = local_len
                local_len -= 1
                sum -= nums[j]
                j += 1
            i += 1
        if min_len == float('inf'): 
            min_len = 0
        return min_len