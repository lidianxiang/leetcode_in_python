"""
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  

1 是丑数。
n 不超过1690。
"""


class Solution:
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        num_2, num_3, num_5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2*dp[num_2], 3*dp[num_3], 5*dp[num_5])
            if dp[i] >= 2 * dp[num_2]:
                num_2 += 1
            if dp[i] >= 3 * dp[num_3]:
                num_3 += 1
            if dp[i] >= 5 * dp[num_5]:
                num_5 += 1
        return dp[-1]

