# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(x)
        is_negative = False
        if x < 0:
            is_negative = True

        x = abs(x)
        result = 0

        while x > 0:
            digit = x % 10
            x = x // 10
            if x != 0:
                result += digit * (10 ** len(str(x)))
            else:
                result += digit * (10 ** (len(str(x)) - 1))
        if is_negative:
            if result > pow(2, 31) - 1 or result < -1 * pow(2, 31):
                return 0
            else:
                return str(-1 * result)
        else:
            if result > pow(2, 31) - 1 or result < -1 * pow(2, 31):
                return 0
            else:
                return str(result)
