"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    深度优先搜索

    在深度优先搜索中，我们总是先访问右子树。这样就保证了当我们访问树的某个特定深度时，
    我们正在访问的节点总是该深度的最右侧节点。于是，可以存储在每个深度访问的第一个结点，
    一旦我们知道了树的层数，就可以得到最终的结果数组。

    """
    def rightSideView(self, root):
        rightmost_value_at_depth = dict()
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                max_depth = max(max_depth, depth)

                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


from collections import deque


class Solution2:
    """
    广度优先搜索

    通过执行将左结点排在右结点之前的广度优先搜索，我们对每一层都从左到右访问。
    因此，通过只保留每个深度最后访问的结点，我们就可以在遍历完整棵树后得到每个深度最右的结点。
    除了将栈改成 deque（双向队列），并去除了rightmost_value_at_depth之前的检查外，算法没有别的改动。


    """
    def rightSideView(self, root):
        rightmost_value_at_depth = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                max_depth = max(max_depth, depth)

                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
