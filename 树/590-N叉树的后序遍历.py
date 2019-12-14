"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :

            1
          / |  \
        3   2   4
       / \
      5   6


返回其后序遍历: [5,6,3,2,1,4]。
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """迭代法"""
    def postorder(self, root):
        if root is None:
            return []

        stack, output = [root], []
        while stack:
            node = stack.pop()
            if node is not None:
                output.append(node.val)
            for c in node.children:
                stack.append(c)
        return output[::-1]


class Solution2:
    """递归法"""
    def postorder(self, root):
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)

        return res

