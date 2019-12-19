"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return

            helper(root.left)
            helper(root.right)

            if not root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right

                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        helper(root)


class Solution2:
    """
    1、右子树 -> 左子树的叶子上
    2、左子树替代右子树
    3、左子树 = None
    """
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if not root.left:
            return None

        node = root.left
        while node.right:
            node = node.right

        node.right = root.right
        root.right = root.left
        root.left = None
