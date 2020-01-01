"""
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:

输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
示例 2:

输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
"""


class Solution:
    def wiggleSort(self, nums):
        """
        将数组重新排序（按照从大到小），并将数组从中间分开，按照奇偶穿插组成新的数组
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2], nums[::2] = nums[:mid], nums[mid:]
