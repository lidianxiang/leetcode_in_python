"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

"""


# definition a binary tree node
class TreeNode:
    def __init(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """中序遍历"""
    def kthSmallest(self, root, k):
        stack, p, s = [], root, 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()
            s += 1
            if s == k:
                return p.val
            p = p.right
