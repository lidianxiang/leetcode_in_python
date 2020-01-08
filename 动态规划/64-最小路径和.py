"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 当左边和上边都是矩阵边界时，也就是初始位置
                if i == j == 0:
                    continue
                # 当只有左边时矩阵边界
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                # 当只有上边时矩阵边界
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                # 当左边和上边都不是矩阵边界
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
