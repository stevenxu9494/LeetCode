# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        valueIndex = {}
        for index, value in enumerate(nums):
            if value not in valueIndex:
                valueIndex[value] = [index]
            else:
                valueIndex[value].append(index)

        for key in valueIndex:
            remain = target - key
            if remain not in valueIndex:
                continue
            if remain == key and len(valueIndex[key]) == 1:
                continue
            elif remain == key:
                return valueIndex[key]
            return [valueIndex[key][0], valueIndex[remain][0]]

