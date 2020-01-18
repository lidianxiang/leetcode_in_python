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


class Solution2:
    def solveNQueens(self, n):
        # 特判
        if n < 1:
            return []
        self.result = []
        # 表示列方向
        self.cols = set()
        # pie表示负45度方向
        self.pie = set()
        # na表示45度方向
        self.na = set()
        # n表示queens的行数
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # 终止条件
        if row >= n:
            self.result.append(cur_state)
            return
        # 逐行遍历
        for col in range(n):
            # 当列在原来的列上或者负45度方向原来有位置或者45度方向原来有位置
            if col in self.cols or row + col in self.pie or row - col in self.na:
                # 表示不是解，继续搜索
                continue
            # 否则这个是解，将列、pie和na的信息加入cols、pie、na中
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            # 递归搜索下一行，将答案放入cur_state中
            self.DFS(n, row + 1, cur_state + [col])
            # 取出刚才列、pie和na的信息，恢复成原始状态
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    # 输出至特定格式的答案
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + "Q" + '.' * (n - i - 1))
        return [board[i:i + n] for i in range(0, len(board), n)]
