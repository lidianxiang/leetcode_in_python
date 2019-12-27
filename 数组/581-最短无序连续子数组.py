"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
"""


class Solution:
    """
    当前数组与排序后的数组具有不同数值的索引的最大值与最小值得差值，再加上一即为答案
    """
    def findUnsortedSubarray(self, nums):
        sort_nums = sorted(nums)
        res = []
        for i, (x, y) in enumerate(zip(sort_nums, nums)):
            if x != y:
                res.append(i)
        # 这里要加上len(res)的原因是要排除nums本身是有序数组的情况
        return len(res) and max(res) - min(res) + 1
