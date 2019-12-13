"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """中序遍历+双指针"""

    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 中序遍历
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        # 中序遍历后对二叉树的序列排序
        numbers = sorted(inorder(root))
        # 序列的长度
        n = len(numbers)

        # 双指针i、j
        i = 0
        j = n - 1
        while i < j:
            if numbers[i] + numbers[j] > k:
                j -= 1
            elif numbers[i] + numbers[j] < k:
                i += 1
            else:
                return True
        return False
