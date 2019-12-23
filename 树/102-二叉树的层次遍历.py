"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归法"""
    def levelOrder(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # 第0层（root），创建一个空列表
            if len(levels) == level:
                levels.append([])
            # 每一层加上每层的节点值
            levels[level].append(node.val)
            # 当左节点存在时，加上左节点的值
            if node.left:
                helper(node.left, level + 1)
            # 当右节点存在时，加上右节点的值
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


class Solution2:
    """迭代法"""
    def levelOrder(self, root):

        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                # 双端队列，从左边弹出
                node = queue.popleft()
                # 从队列弹出后，加入levels中
                levels[level].append(node.val)
                # 当左节点存在时，将左节点加入队列中
                if node.left:
                    queue.append(node.left)
                # 当右节点存在时，将右节点加入队列中
                if node.right:
                    queue.append(node.right)
            # 层次加一
            level += 1
        return levels
