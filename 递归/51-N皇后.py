"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    """递归 + DFS"""
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            """xy_dif表示45度对角线， xy_sum表示负45度对角线"""
            # p表示queens的行数
            # 逐行搜索的
            p = len(queens)
            # 递归终止条件，当搜索到最后一行了，返回最后的结果
            if p == n:
                result.append(queens)
                return None
            # 逐行搜索
            for q in range(n):
                # 当q不在先前的queens的列、45度对角线和负45度对角线上时
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    # 这是一个答案，加上它，占据位置
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        # 两层列表推导式，输出答案
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]
