"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution:
    """动态规划"""
    def numSquares(self, n):
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]


from collections import deque


class Solution2:
    """广度优先遍历，BFS"""
    def numSquares(self, n):

        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            for _ in range(len(queue)):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    x = tmp - i ** 2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step
