"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归方式"""
    def minDepth(self, root: TreeNode) -> int:
        # 判断root是否存在
        if not root:
            return 0

        children = [root.left, root.right]
        # 考虑只有root，没有左右子树的情况
        if not any(children):
            return 1

        min_depth = float('inf')
        # 遍历树的节点
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


class Solution2:
    """
    我们可以利用栈将上述解法中的递归变成迭代。

    想法是对于每个节点，按照深度优先搜索的策略访问，同时在访问到叶子节点时更新最小深度。

    我们从一个包含根节点的栈开始，当前深度为 1 。

    然后开始迭代：弹出当前栈顶元素，将它的孩子节点压入栈中。当遇到叶子节点时更新最小深度。


    """
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth


from collections import deque


class Solution:
    """
    深度优先搜索方法的缺陷是所有节点都必须访问到，以保证能够找到最小深度。因此复杂度是 O(N)。

    一个优化的方法是利用宽度优先搜索，我们按照树的层次去迭代，第一个访问到的叶子就是最小深度的节点，这样就不要遍历所有的节点了。

    """
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])

        while node_deque:
            depth, root = node_deque.popleft()

            children = [root.left, root.right]

            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth+1, c))
