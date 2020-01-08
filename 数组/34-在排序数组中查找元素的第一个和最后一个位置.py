"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    """
        两次二分查找：第一次找到开始位置，第二次找到结束位置
    """
    def searchRange(self, nums, target):
        l, r = 0, len(nums)-1
        # 二分查找
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        # 没找到
        if not nums or nums[l] != target:
            return [-1, -1]
        # 找到结束下标
        a, b = l, len(nums)-1
        while a < b:
            mid = (a+b+1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1
        return [l, a]
