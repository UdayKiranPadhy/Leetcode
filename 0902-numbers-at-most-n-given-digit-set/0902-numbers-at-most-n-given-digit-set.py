class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        digits = list(map(int,digits))
        n_digits = list(map(int, str(n)))
        
        N = len(str(n))

        @cache
        def go(pos, tight, started):
            if pos == N:
                return 1 if started else 0

            limit = n_digits[pos] if tight else 9
            
            ans = 0

            if not started:
                ans += go(pos+1,
                    False if tight and 0 < limit else tight,
                    False
                    )
            
            for digit in digits:
                if digit > limit:
                    continue
                
                new_tight = (
                    tight and
                    digit == n_digits[pos]
                )

                ans += go(pos+1, new_tight, True)
            
            return ans
        
        return go(0,True,False)