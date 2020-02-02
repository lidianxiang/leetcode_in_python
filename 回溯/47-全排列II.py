"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    """回溯 + 剪枝"""
    def permuteUnique(self, nums):
        nums.sort()
        self.res = []
        check = [0 for _ in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        # 当前结果的长度 == 列表的长度时， 返回结果
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        for i in range(len(nums)):
            # 用过的元素不在能使用
            if check[i] == 1:
                continue
            # 重复元素需要剪枝
            if i > 0 and nums[i] == nums[i - 1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            # 重置check
            check[i] = 0
