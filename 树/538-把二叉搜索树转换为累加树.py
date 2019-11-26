"""

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [(root, 1)]
        sum = 0
        while stack:
            node, cmd = stack.pop()
            if node is None:
                continue
            if cmd == 0:
                sum += node.val
                node.val = sum
            else:
                stack.append((node.left, 1))
                stack.append((node, 0))
                stack.append((node.right, 1))
        return root
