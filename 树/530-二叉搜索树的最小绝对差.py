"""
给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :

输入:

   1
    \
     3
    /
   2

输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution:
    """
    既然是要找结点值之间最小的差的绝对值，那就是对每个结点值找到与其最相近的结点值，然后求差了。
    设想如果是一个有序数组的话，这样的最小值就是按顺序后一个元素与前一个元素的差的最小值了。
    看到BST第一反应就是BST的中序遍历结果是有序数组，正好对应上了，那就是中序遍历时，
    求当前结点与前一结点的差，差的最小值就是结果了。
    """
    def getMinimumDifference(self, root: TreeNode) -> int:
        result = sys.maxsize
        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if prev is not None:
                    result = min(result, node.val - prev)
                prev = node.val
                root = node.right
        return result
