"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

"""


class Solution:
    def maximalSquare(self, matrix):
        # 特判
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 若当前位置为1
                if matrix[i-1][j-1] == '1':
                    # 构成最大正方形的边长是其正上方，左侧和左上界中的最小值
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    res = max(dp[i][j], res)
        return res * res


class Solution2:
    """
    由公式：dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，可知，
        当前位置的最大边长仅取决于上一行和左侧最大边长，可以将空间优化到O(n),借助pre来保存当前位置的左侧
    """
    def maximalSquare(self, matrix):
        # 特判
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        res, pre = 0, 0
        dp = [0] * (n + 1)
        for i in range(0, m):
            for j in range(1, n + 1):
                tmp = dp[j]
                if matrix[i][j - 1] == "1":
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                # 不换行时，将tmp值赋给pre指针
                pre = tmp
            # 换行，将pre指针置0
            pre = 0
        return res * res
