"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
"""


class Solution:
    """滑动窗口"""
    def findMaxAverage(self, nums, k):
        res = sum(nums[:k])
        tmp = res
        for i in range(k,len(nums)):
            tmp = tmp - nums[i-k] + nums[i]
            # res = max(res, tmp)
            # 对于要求速度性能的话，使用if判断比使用max()函数更快点
            if tmp > res:
                res = tmp
        return res / k

