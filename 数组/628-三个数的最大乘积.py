"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
"""


class Solution:
    def maximumProduct(self, nums):
        nums = sorted(nums)
        # 三个数都是正数的情况
        result1 = nums[-1] * nums[-2] * nums[-3]
        # 存在负数的情况，例如[-4,-3,-2,-1,4]
        result2 = nums[-1] * nums[0] * nums[1]
        return max(result1, result2)
