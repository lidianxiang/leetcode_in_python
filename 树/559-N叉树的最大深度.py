"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :

        1
      / |  \
    3   2   4
   / \
  5  6

我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。


"""


# difinition for a node
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """递归求解"""
    def maxDepth(self, root):
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in self.root]
            return max(height) + 1


class Solution2:
    """迭代求解（利用堆栈）"""
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if node is not None:
                depth = max(depth, current_depth)
                for c in node:
                    stack.append((current_depth+1, c))

        return depth

