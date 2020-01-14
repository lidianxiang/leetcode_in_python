"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix):
        # 特判
        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        # 表示之前已经访问过的元素
        seen = [[False] * C for _ in matrix]
        # 存储答案
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        # di表示前进方向
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans


class Solution2:
    """按层模拟"""
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            # 遍历上面
            for c in range(c1, c2 + 1):
                yield r1, c
            # 遍历右边
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                # 遍历下面
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                # 遍历左边
                for r in range(r2, r1, -1):
                    yield r, c1
        # 特判
        if not matrix:
            return []

        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            # 从最外层向里层遍历
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ans
