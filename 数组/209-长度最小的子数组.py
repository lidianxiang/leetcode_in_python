"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""


class Solution:
    """
    双指针 + 滑动窗口
    """
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        left = 0
        # 保存结果
        res = float('inf')
        tmp = 0
        for right in range(n):
            tmp += nums[right]
            # 当累加结果大于s时遍历数组
            while tmp >= s:
                # 更新res结果
                res = min(res, right - left + 1)
                # 减去左指针指向的值
                tmp -= nums[left]
                # 更新左指针
                left += 1
        return res if res != float('inf') else 0
