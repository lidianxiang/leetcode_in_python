"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    按照常用方法计算一个节点的深度：max(depth of node.left, depth of node.right) + 1。
    在计算的同时，经过这个节点的路径长度为 1 + (depth of node.left) + (depth of node.right) 。
    搜索每个节点并记录这些路径经过的点数最大值，期望长度是结果 - 1。
    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
