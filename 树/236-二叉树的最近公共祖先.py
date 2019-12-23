"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归法

    先深度遍历树，当遇到节点p或q时，返回一些布尔标记，标记有助于确定是否在任何路径中找到所需的节点。最不常见的祖先将是讲
    两个子树递归都返回真标志的节点。它可以是一个节点

    临界条件：最近公共祖先为根节点
                根节点是空节点
                根节点是q节点
                根节点是p节点
    根据临界条件
            此题相当于查找以 root 为根节点的树上是否有p节点或者q节点
                有，返回p节点或q节点
                无，返回null
    求解
        从左右子树分别进行递归，即查找左右子树上是否有p节点或者q节点
            左右子树均无p节点或q节点
            左子树找到，右子树没有找到，返回左子树的查找结果
            右子树找到，左子树没有找到，返回右子树的查找结果
            左、右子树均能找到
                说明此时的p节点和q节点在当前root节点两侧，返回root节点

   """
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            if not current_node:
                return False
            # 左子树递归
            left = recurse_tree(current_node.left)
            # 右子树递归
            right = recurse_tree(current_node.right)
            # 当current_node是p或q中的一个
            mid = current_node == p or current_node == q
            # 当三个标志中的两个或以上都为真的时候
            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans
