"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

"""


# definition a binary tree node
class TreeNode:
    def __init(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归"""
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            # 边界条件
            if not node:
                return 0
            # 对node节点的左右子树递归调用max_gain()函数
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # 判断是维护旧路径还是创建新路径(price_newpath)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(price_newpath, max_sum)

            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum
