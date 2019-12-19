"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归法

    先序遍历的顺序是 Root -> Left -> Right，这就能方便的从根开始构造一棵树。
    1、首先，preorder 中的第一个元素一定是树的根，这个根又将 inorder 序列分成了左右两棵子树。
    2、现在我们只需要将先序遍历的数组中删除根元素，然后重复上面的过程处理左右两棵子树。

    """
    def buildTree(self, preorder, inorder):
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            # 没有子树的情况
            if in_left == in_right:
                return None
            # 前序遍历的第一个元素即为root节点
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            index = idx_map[root_val]

            pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)
            return root

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()
