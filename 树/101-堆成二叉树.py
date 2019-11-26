"""

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

"""


# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 考虑使用递归的方式
class Solution:
    def isSymmetric(self, root):
        def help(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return help(left.left, right.right) and help(left.right, right.left)

        return help(root.left, root.right) if root else True


from collections import deque


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        deq = deque([root, root])
        while deq:
            t1, t2 = deq.pop(), deq.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            deq.append(t1.left)
            deq.append(t2.right)
            deq.append(t1.right)
            deq.append(t2.left)
        return True
