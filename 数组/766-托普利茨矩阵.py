"""
如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

示例 1:

输入:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。
示例 2:

输入:
matrix = [
  [1,2],
  [2,2]
]
输出: False
解释:
对角线"[1, 2]"上的元素不同。
"""


class Solution:
    """
    对角线：满足条件r1 -c1 == r2 - c2
    所以可以让groups[r-c]来存储每条对角线上遇到的第一个元素，如果后来遇到的
    任何一个值不等于之前的值，则返回False，否则返回True。
    """
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
