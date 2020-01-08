"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
"""


class Solution:
    """动态规划"""
    def minimumTotal(self, triangle):
        # 特判
        if not triangle:
            return 0
        n = len(triangle)
        # 当只有一行的情况
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                # 第一行
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                # 最后一行
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                # 既不是第一行也不是最后一行的情况
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
