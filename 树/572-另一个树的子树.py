"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    方式是：递归法。并且创建一个辅助函数判断两棵树是否相同
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        return self.isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSame(p.left,q.left) and self.isSame(p.right, q.right)


class Solution2:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = self.inorder(s)
        tt = self.inorder(t)
        return tt in ss

    def inorder(self, root):
        if not root:
            return '#'
        return '*' + str(root.val) + self.inorder(root.left) + self.inorder(root.right)
