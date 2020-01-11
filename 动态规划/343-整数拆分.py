"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""


class Solution:
    """
    贪心算法：
    情况1：如果分解式中含有1：因为 1*(n-1) = n-1< n，明显，越分解乘积越小。
    情况2：如果分解式中含有2：考虑边界条件 2 x (n - 2) > n，得n > 4,所以当n>4的时候，分解2在乘以n-2得到结果超过n
    情况3：如果分解式中含有3：考虑边界条件 3 x (n - 3) > n，得n > 4.5,所以当n>4.5的时候，分解3在乘以n-3得到的结果超过n
    情况4：如果分解式中含有4：等价于分解出两个2，因此情况2就包含了情况4
    情况5：如果分解式中含有5:分解出5与n-5的乘积小于2、3和n-5的乘积

    划重点：要找出到底是多分解出2好还是多分解出3好，我们计算出边界条件，
            3 X (n -3) > 2 X (n - 2)
          得到 n >= 5（重点！！！）

    综上所述，分解出3比分解出2好，我们应该尽可能多分解出3，直到最后剩下4或2
    """

    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res


class Solution2:
    """
    动态规划
    """
    def integerBreak(self, n):
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j], j) * (i - j))
        return dp[-1]


class Solution3:
    """动态规划,这种动态规划比上面那种要好理解一点"""
    def integerBreak(self, n):

        dp = [1 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(3, n + 1):
            dp[i] = max(max(dp[i - 1], i - 1),
                        2 * max(dp[i - 2], i - 2),
                        3 * max(dp[i - 3], i - 3))
        return dp[-1]
