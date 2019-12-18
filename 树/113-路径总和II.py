"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归法"""

    def pathSum(self, root: TreeNode, sum):
        paths = []

        def traverse(root, sum, path=[]):
            if not root:
                return

            if not root.left and not root.right:
                if sum == root.val:
                    paths.append(path + [root.val])
            elif not root.left:
                traverse(root.right, sum - root.val, path + [root.val])
            elif not root.right:
                traverse(root.left, sum - root.val, path + [root.val])
            else:
                traverse(root.left, sum - root.val, path + [root.val])
                traverse(root.right, sum - root.val, path + [root.val])

        traverse(root, sum)
        return paths


class Solution2:
    """递归法"""
    """注意此处函数参数是sum_而不是sum，为了和sum（）区分开"""
    def pathSum(self, root, sum_):
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res
