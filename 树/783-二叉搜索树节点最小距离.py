"""
给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树结点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

"""


# definition a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """思路：排序
    将树中的所有节点的值写入数组中，之后将数组排序。依次计算相邻数之间的差值。
    """
    def minDiffInBST(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        vals.sort()
        return min(vals[i+1] - vals[i] for i in range(len(vals) - 1))


class Solution2:
    """
    思路：中序遍历
    在二叉搜索树中，中序遍历会将树中的节点按数值大小顺序输出。只要遍历计算相邻数的差值即可求出答案。
    """
    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)
        self.ans = float('inf')
        self.prev = float('-inf')
        dfs(root)
        return self.ans
