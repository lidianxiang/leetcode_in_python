"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """归并排序（递归版）"""
    def sortList(self, head):
        # 特判
        if not head or not head.next:
            return head
        # 快慢指针，寻找中点
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # mid为链表的中点， 将slow.next设置为None，断开了两个链表
        mid, slow.next = slow.next, None
        # 递归调用了两个链表
        left, right = self.sortList(head), self.sortList(mid)
        # res为最后答案， h为辅助节点
        h = res = ListNode(0)
        while left and right:
            # 当左链表的值小于右链表的值
            if left.val < right.val:
                # h指针的下个元素指向left节点，left节点向后移动一位
                h.next, left = left, left.next
            # 否则（左链表的值大于右链表的值）
            else:
                # h指针的下一个元素指向右链表的节点，右链表节点向后移动一位
                h.next, right = right, right.next
            # h指针向后移动一位
            h = h.next
        # 将两个链表合并
        h.next = left if left else right
        return res.next


class Solution2:
    """归并排序（非递归版）"""
    def sortList(self, head):
        # intv表示每次分割单元长度，第一次为1，后面均乘以2
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # 遍历
        while intv < length:
            # pre为res的辅助节点
            pre, h = res, res.next
            while h:
                # 获得两个合并节点h1和h2
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                # 不在需要合并，因为此时的h2为None
                if i:
                    break
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i
                # 合并两个节点
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next
