"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    """双指针 + 排序"""
    def threeSumClosest(self, nums, target):
        n = len(nums)
        if not nums or n < 3:
            return None

        nums.sort()
        res = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]
                if cur_sum == target:
                    return target
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum - target < 0:
                    L += 1
                else:
                    R -= 1
        return res
