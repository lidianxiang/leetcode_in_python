"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""


class Solution:
    """暴力搜索，逐行遍历"""
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row:
                return True
        return False


class Solution2:
    """二分查找"""
    def searchMatrix(self, matrix, target):

        # 当矩阵为空
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        return False

    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        return False


class Solution3:
    """
    因为矩阵的行和列是排序的，所以在查看任何特定值，可以修剪O(m)或O(n)元素

    首先，我们初始化一个指向矩阵左下角的 (row，col)(row，col) 指针。然后，直到找到目标并返回 true
    （或者指针指向矩阵维度之外的 (row，col)(row，col) 为止，
    我们执行以下操作：如果当前指向的值大于目标值，则可以 “向上” 移动一行。
    否则，如果当前指向的值小于目标值，则可以移动一列。
    不难理解为什么这样做永远不会删减正确的答案；因为行是从左到右排序的，
    所以我们知道当前值右侧的每个值都较大。 因此，如果当前值已经大于目标值，
    我们知道它右边的每个值会比较大。也可以对列进行非常类似的论证，
    因此这种搜索方式将始终在矩阵中找到目标（如果存在）。
    """
    def searchMatrix(self, matrix, target):
        # 特判
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix)
        width = len(matrix[0])

        row = height - 1
        col = 0

        while col < width and row >= 0:
            # 当target值小于当前值，row指针向上移动
            if matrix[row][col] > target:
                row -= 1
            # 当target值大于当前值，col指针向右移动
            elif matrix[row][col] < target:
                col += 1
            # 找到了targrt值
            else:
                return True
        return False
