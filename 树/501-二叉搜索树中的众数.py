# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.count = collections.Counter()
        # 中序遍历得到有序序列
        self.inOrder(root)
        # 找到频数最多的那个数
        freq = max(self.count.values())
        res = []
        # 要考虑存在多个最大值的情况
        for item ,c in self.count.items():
            if c == freq:
                res.append(item)
        return res

    # 中序遍历
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.count[root.val] += 1
        self.inOrder(root.right)
