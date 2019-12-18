"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    这道题难点,是找到那两个交换节点,把它交换过来就行了.

    这里我们二叉树搜索树的中序遍历(中序遍历遍历元素是递增的)

    如下图所示, 中序遍历顺序是 4,2,3,1,我们只要找到节点4和节点1交换顺序即可!

    这里我们有个规律发现这两个节点:

    第一个节点,是第一个按照中序遍历时候前一个节点大于后一个节点,我们选取前一个节点,这里指节点4;

    第二个节点,是在第一个节点找到之后, 后面出现前一个节点大于后一个节点,我们选择后一个节点,这里指节点1;


    """
    def recoverTree(self, root):
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float('-inf'))

        def in_order(node):
            """递归法来中序遍历"""
            if not node:
                return
            in_order(node.left)
            if not self.firstNode and self.preNode.val >= node.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= node.val:
                self.secondNode = node
            self.preNode = node
            in_order(node.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val



class Solution2:
    """迭代法中序遍历"""
    def recoverTree(self, root):
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                secondNode = p
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val

