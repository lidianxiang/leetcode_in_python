"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

"""


# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    思想：迭代
    从根节点开始依次迭代，弹出栈顶元素输出到输出列表中，
    然后依次压入它的所有孩子节点，按照从上到下、从左至右的顺序依次压入栈中。
    """
    def postOrder(self, root):
        if not root:
            return []

        stack, output = [root, ], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return output[::-1]
