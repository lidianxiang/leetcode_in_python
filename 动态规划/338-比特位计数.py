"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
"""


class Solution:
    """
    1、奇数的二进制中1的个数等于它的上一位偶数的二进制中1的个数加一
    2、偶数的二进制中1的个数等于它除以2后的数的二进制中1的个数
    """
    def countBits(self, num):
        dp = [0] * (num+1)
        for i in range(1, num+1):
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]
        return dp
