"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

"""


# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    1、从根节点开始遍历树
    2、如果节点 pp 和节点 qq 都在右子树上，那么以右孩子为根节点继续 1 的操作
    3、如果节点 pp 和节点 qq 都在左子树上，那么以左孩子为根节点继续 1 的操作
    4、如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 pp 和节点 qq 的 LCA 了

    """
    def lowerCommenAncestor(self, root, p, q):
        parent_val = root.val

        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowerCommenAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowerCommenAncestor(root.left, p, q)
        else:
            return root


class Solution2:
    """迭代方式
    这个方法跟方法一很接近。唯一的不同是，我们用迭代的方式替代了递归来遍历整棵树。
    由于我们不需要回溯来找到 LCA 节点，所以我们是完全可以不利用栈或者是递归的。
    实际上这个问题本身就是可以迭代的，我们只需要找到分割点就可以了。
    这个分割点就是能让节点 pp 和节点 qq 不能在同一颗子树上的那个节点，或者是节点 pp 和节点 qq 中的一个，
    这种情况下其中一个节点是另一个节点的父亲节点。

    """
    def lowestCommonAncestor(self, root, p, q):

        p_val = p.val
        q_val = q.val

        node = root

        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
