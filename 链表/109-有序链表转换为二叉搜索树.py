"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 利用快慢指针来确定链表的中间节点
    def findMiddle(self, head):
        # pre指针指向前半部分的最后一个节点
        pre = None
        # 慢指针
        slow = head
        # 快指针
        fast = head

        while fast and fast.next:
            pre = slow
            # 慢指针每次走一步
            slow = slow.next
            # 快指针每次走两步
            fast = fast.next.next
        # 当上述循环结束后，fast指针走到了最后，慢指针走到了中间
        if pre:
            # pre指针的下一个节点是slow，将pre的next指针指向None，从而断开链表
            pre.next = None
        # slow指针现在指向的就是链表的中间节点
        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 判断head是否存在
        if not head:
            return None
        # 调用findMiddle函数，返回中间节点，命名为mid
        mid = self.findMiddle(head)
        # 创建一个树节点，值为mid
        node = TreeNode(mid.val)
        # 判断head是否等于mid。即链表的长度是否为一的特殊情况
        if head == mid:
            return node
        # 递归调用函数，左子树的根节点是head
        node.left = self.sortedListToBST(head)
        # 递归调用函数，右子树的根节点是mid.next
        node.right = self.sortedListToBST(mid.next)

        return node


class Solution2:
    def mapListToValues(self, head):
        """将链表转换为list形式，快速得到中间节点"""
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST(self, head):

        values = self.mapListToValues(head)

        def convertListToBST(l, r):
            # l（left）大于r（right）的情况
            if l > r:
                return None
            # 否则，得到中间节点的位置
            mid = (l + r) // 2
            # 初始化根节点，节点的值为mid的值
            node = TreeNode(values[mid])
            # 当 l== r 的情况
            if l == r:
                return node
            # 递归调用
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node

        return convertListToBST(0, len(values) - 1)
