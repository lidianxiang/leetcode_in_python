"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

思路：
平衡二叉搜索树需要保证俩点：
根节点大于左子树任意节点，小于右子树任意节点
左右子数高度相差不超过 1
由以上性质，一个可行的递归条件可以得出：
每次返回的根节点处于数组中间，以其左右半数组分别递归构造左右子树
那么就意味着左子小于根，右子大于根，且所有节点左右子树节点数相差不超过 1 （由于递归的构树方式相同，所有节点都满足高度平衡）

"""


# defination for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sortedArrayToBST, [nums[:m], nums[m+1:]])
            return r
