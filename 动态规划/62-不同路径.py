"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
"""


class Solution:
    """递归，但是超出了时间限制"""
    def uniquePaths(self, m, n):
        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            return helper(i-1, j) + helper(i, j-1)
        return helper(m-1, n-1)


class Solution2:
    """递归，但是加入缓存记录之前的信息"""
    def uniquePaths(self, m, n):
        def helper(i, j):
            if i == 0 or j == 0:
                return 1

            if cache[j][i]:
                return cache[j][i]
            cache[j][i] = helper(i - 1, j) + helper(i, j - 1)
            return cache[j][i]

        cache = [[None for _ in range(m)] for _ in range(n)]
        return helper(m - 1, n - 1)


class Solution3:
    """动态规划"""
    def uniquePaths(self, m, n):
        # 初始状态定义
        cache = [[1 for _ in range(m)] if j == 0 else [1 if i == 0 else None for i in range(m)] for j in range(n)]
        # 每一行是一个阶段，因为第一行已经知道结果了，所以从第二行开始
        for x in range(1, n):
            # 每一个阶段内部，因为第一列已经知道了，所以从第二列开始计算
            for y in range(1, m):
                # 递归方程
                cache[x][y] = cache[x - 1][y] + cache[x][y - 1]
        return cache[n - 1][m - 1]
