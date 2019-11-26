"""

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false

"""


# definition for a binary tree node
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self,root):
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) \
               and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self,node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
