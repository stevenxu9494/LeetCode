'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

'''
First make sure signs of the result and convert to positive numbers.
Then check all the even number of multiples of divisor. For example, starting
from divisor * 16, then divisor * 8, then divisor * 4 ... until divisor.
For each iteration, check to substract current number from dividend, if possible
to substract, the return value will be added.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # get the result sign from negative or positive
        is_negative = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor >9):
            is_negative = True
        # absolute both dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)

        # see how many times dividend can be divided by divisor
        accumulator, index = divisor, 1
        track = []
        while accumulator <= dividend:
            track.append((accumulator, index))
            accumulator += accumulator
            index += index

        # get Characteristic and Mantiss
        result = 0
        for i in range(len(track) -1, -1, -1):
            val, idx = track[i]
            if dividend >= val:
                dividend -= val
                result += idx
        if (not is_negative and result >= 2147483648) or (is_negative and result > 2147483648):
            return 2147483647
        return result if not is_negative else -result


