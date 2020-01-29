"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    """模拟法"""
    def generateMatrix(self, n):
        left, right, top, bottom = 0, n-1, 0, n-1
        # 初始化全零矩阵
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        # 从外向里
        while num <= tar:
            # 从左到右
            for i in range(left, right+1):
                mat[top][i] = num
                num += 1
            top += 1
            # 从上到下
            for i in range(top, bottom+1):
                mat[i][right] = num
                num += 1
            right -= 1
            # 从右到左
            for i in range(right, left - 1, -1):
                mat[bottom][i] = num
                num += 1
            bottom -= 1
            # 从下到上
            for i in range(bottom, top - 1, -1):
                mat[i][left] = num
                num += 1
            left += 1
        return mat
