class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # We start processing from the least significant bit (rightmost end of the string)
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '0':
                # If bit is '0', it remains '0' unless there's a carry
                if carry:
                    steps += 2  # 0 with carry becomes 10, which means add 1 and then divide by 2
                else:
                    steps += 1  # just divide by 2
            else:
                # If bit is '1', it turns to '0' with a carry, unless there's already a carry
                if carry:
                    steps += 1  # already carrying, so just division step
                else:
                    steps += 2  # add 1 to make it even, then divide by 2
                    carry = 1  # setting carry because adding 1 will affect the next significant bit
                
        # After processing all bits except the most significant bit
        return steps + carry
        