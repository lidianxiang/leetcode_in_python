"""
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归求解
    """
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node:
                return 0
            # 递归左子树
            left_length = arrow_length(node.left)
            # 递归右子树
            right_length = arrow_length(node.right)
            # 定义左、右箭头的长度
            left_arrow = right_arrow = 0
            # 当左子树存在且左子树的值等于父节点的值
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            # 当右子树存在且右子树的值等于父节点的值
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            # 返回左右箭头的最长值
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
