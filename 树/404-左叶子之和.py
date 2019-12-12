"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归"""
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 递归终止的条件是：当前节点为左叶子节点或是空节点
        if root and root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class Solution2:
    """迭代"""
    def sumOfLeftLeaves(self, root):

        Sum = 0
        if not root:
            return 0

        ans = [root]
        while ans:
            node = ans.pop()
            if node.left and not node.left.left and not node.left.right:
                Sum += node.left.val
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
        return Sum
