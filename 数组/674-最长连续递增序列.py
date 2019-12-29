"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
"""


class Solution:
    """
    1、每个（连续）增加的子序列是不相交的，并且每当 nums[i-1]>=nums[i] 时，每个此类子序列的边界都会出现。
       当它这样做时，它标志着在 nums[i] 处开始一个新的递增子序列，我们将这样的 i 存储在变量 anchor 中。
    2、例如，如果 nums=[7，8，9，1，2，3]，那么 anchor 从 0 开始（nums[anchor]=7），
       并再次设置为 anchor=3（nums[anchor]=1）。无论 anchor 的值如何，
       我们都会记录 i-anchor+1 的候选答案、子数组 nums[anchor]、nums[anchor+1]、…、nums[i] 的长度，
       并且我们的答案会得到适当的更新。

    """
    def findLengthOfLCIS(self, nums):
        ans = index = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                index = i
            ans = max(ans, i - index + 1)
        return ans
