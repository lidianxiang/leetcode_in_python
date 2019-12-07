"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * n for n in range(1, numRows + 1)]
        for i in range(numRows):
            dp[i][0] = dp[i][-1] = 1
        for i in range(0, numRows):
            for j in range(i + 1):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp
