"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

"""


class Solution:
    """
    用一个计数器count记录1的数量，另一个计数器maxCount记录当前最大的1的个数
    """
    def findMaxConsecutiveOnes(self, nums):
        count = max_count = 0
        for num in nums:
            # 当数字为1时，count加一
            if num == 1:
                count += 1
            # 当数字不为1时， 判断count和max_count的最大值，更新max_count的值
            else:
                max_count = max(max_count, count)
                # count清零
                count = 0

        return max(max_count, count)
