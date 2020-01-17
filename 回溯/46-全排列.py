"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    """
    回溯算法

    1、如果第一个整数有索引 n，意味着当前排列已完成。
    2、遍历索引 first 到索引 n - 1 的所有整数。Iterate over the integers from index first to index n - 1.
        在排列中放置第 i 个整数，即 swap(nums[first], nums[i]).
        继续生成从第 i 个整数开始的所有排列: backtrack(first + 1).
        现在回溯，即通过 swap(nums[first], nums[i]) 还原.
    """
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack()
        return output
