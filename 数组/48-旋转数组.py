"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        沿对角线先翻转数据 + 每行数据倒序
        """
        n = len(matrix[0])
        for i in range(n):
            # for j in range(i, n):
            for j in range(0, i):
                # print((i,j))
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            matrix[i].reverse()


class Solution2:
    """方法一的简写"""
    def rotate(self, matrix):
        # zip和*一起用，表示解包的意思，返回的是对象，在用map函数转化成list形式
        return map(list, zip(*matrix[::-1]))


class Solution3:
    """
    方法一使用了两次矩阵操作，但是只使用一次操作的方法来完成旋转，
    本方法的思路是将给定矩阵分成4个矩形，将原问题规划为旋转这些矩形的问题。
    """
    def rotate(self, matrix):
        n = len(matrix[0])
        # n // 2 + n % 2 表示 奇数的中间和偶数的中间两个的前一位
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row
