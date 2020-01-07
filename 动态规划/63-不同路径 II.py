"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""


class Solution:
    """
                1                     (i == 0, j == 0)
                dp[i][j-1]            (i == 0, j != 0)
    dp[i][j] =  dp[i-1][j]            (i != 0, j == 0)
                dp[i-1] + dp[i][j-1]  (i != 0, j != 0)

    在考虑障碍物的情况下

        1、对于第一个式子，仅在该点为障碍物的时候会导致路径为０(也会导致网络中任意一点，路径均为０)
        2、对于第二个式子，仅会在该点为障碍物的时候导致路径为０，否则机器人可以左方到达，所以和其左方一点的路径相同
        3、对于第三个式子，仅会在该点为障碍物的时候导致路径为０，否则机器人可以上方到达，所以和其上方一点的路径相同
        4、对于第四个式子，仅会在该点为障碍物的时候导致路径为０，否则机器人可以从左方或上方到达，因此为这两个方向的路径之和

    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 行数
        m = len(obstacleGrid)
        # 当行不存在时直接返回0
        if m < 1:
            return 0
        # 列数
        n = len(obstacleGrid[0])
        # 当列不存在时直接返回0
        if n < 1:
            return 0
        # 当出发点就是障碍物时，直接返回0
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j - 1]
                elif i != 0 and j == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]



