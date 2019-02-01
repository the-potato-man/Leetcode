'''
    Signed Binary has range from -(2^31 + 1) to 2^31
    -2147483648 to 2147483647

    https://www.reddit.com/r/learnprogramming/comments/1tncvz/if_a_32_bit_ints_max_value_is_2147483647_why_is/

    49 = b110001
    -9 = b1001

    i = 2
    temp = b100100 (36)
    quotient = b100 (4)

    i = 1
    temp = b100100 (36)  
    (b10010 (18) is invalid)
    quotient = b100 (4)
    (b10 (2) is invalid)

    i = 0
    temp = b100100 (36) + b1001 (9)
    quotient = b100 (4) + b1 (1)

    remainder = 49 - temp
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == 0: return 0
        if divisor == 0: return None
        finalSign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            finalSign = -1
                      
        dividend = abs(dividend)
        divisor = abs(divisor)
  
        curr = 0
        quotient = 0
        
        for i in range(32, -1, -1):
            if curr + (divisor << i) <= dividend:
                curr += (divisor << i)
                quotient += (1 << i)
        
        quotient *= finalSign

        return min(max(-2**31, quotient), 2**31 - 1)
