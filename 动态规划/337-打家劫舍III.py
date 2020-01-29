"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    动态规划:对于每个节点，都只有选和不选两种情况，考虑一颗子树，那么根只有两种情况：dp[0](不选)、dp[1](选)
    1、对于选了根节点的，那么就不能选择它的儿子
    2、对于没有选择根节点，那么可以选择任意的儿子
    """
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))

    def dp(self, cur):
        if not cur:
            return [0, 0]
        l = self.dp(cur.left)
        r = self.dp(cur.right)
        return [max(l) + max(r), cur.val+l[0]+r[0]]
