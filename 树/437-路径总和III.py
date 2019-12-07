"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        # sums为node的父节点已能构成的和，返回最长可延伸到node结束的所有路径所能构成的和列表
        def dfs(node, sums):
            left = right = 0
            # 之前的和加当前结点值能构成的新和，以及从当前结点开始算的新和
            temp = [num + node.val for num in sums] + [node.val]
            if node.left:
                left = dfs(node.left, temp)
            if node.right:
                right = dfs(node.right, temp)
            return temp.count(sum) + left + right

        return dfs(root, [])


class Solution2:
    """使用两个递归来求解"""

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        def dfs(root, sum):
            # 记录路径的个数
            count = 0
            if not root:
                return 0
            if root.val == sum:
                count += 1
            # 递归调用
            count += dfs(root.left, sum - root.val)
            count += dfs(root.right, sum - root.val)
            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
