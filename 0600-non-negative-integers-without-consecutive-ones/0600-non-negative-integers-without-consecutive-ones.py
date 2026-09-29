class Solution:
    def findIntegers(self, n: int) -> int:
        
        bits = list(map(int,bin(n)[2:]))

        @cache
        def go(pos,prev_one,tight):
            if pos == len(bits):
                return 1
            
            limit = bits[pos] if tight else 1
            
            total = 0

            for new_bit in range(limit + 1):
                if prev_one == 1 and new_bit == 1:
                    continue
                
                new_prev_one = new_bit

                new_tight = (tight and new_bit == bits[pos])

                total += go(pos+1, new_prev_one, new_tight)
            
            return total
        
        return go(0,0,True)