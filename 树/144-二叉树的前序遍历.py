"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    思想：迭代
    具体步骤：从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。
    """
    def preorderTraversal(self, root):

        if not root:
            return []

        stack, output = [root, ], []

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return output


class Solution2:
    """
    莫里斯遍历
    思路：从当前节点向下访问先序遍历的前驱节点，每个前驱节点都恰好被访问两次。

         首先从当前节点开始，向左孩子走一步然后沿着右孩子一直向下访问，
         直到到达一个叶子节点（当前节点的中序遍历前驱节点），
         所以我们更新输出并建立一条伪边 predecessor.right = root 更新这个前驱的下一个点。
         如果我们第二次访问到前驱节点，由于已经指向了当前节点，我们移除伪边并移动到下一个顶点。
         如果第一步向左的移动不存在，就直接更新输出并向右移动。

    """
    def preorderTraversal(self, root):

        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right

            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
