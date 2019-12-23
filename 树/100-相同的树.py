"""
给定两个二叉树，请编写一个函数来检验它们是否是相同的。

如果两个树在结构上相同并且节点上具有相同的值，则认为它们是相同的。
"""


# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        # 如果p和q同时为空，则返回True
        if not p and not q:
            return True
        # 若p或q其中一个为空，则返回False
        if not p or not q:
            return False
        # 逐个判断p对应q的值，不想等则为False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
