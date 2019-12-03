"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 判断特殊情况
        if head is None or head.next is None:
            return head
        # 双指针求出链表的中点
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        # cur代表后半链表的头节点
        cur = slow.next
        # 将前半链表与后半链表断开
        slow.next = None
        # 将后半链表反转
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # head与pre代表前后链表的头节点
        cur1, cur2 = head, pre
        while cur2:
            next1, next2 = cur1.next, cur2.next
            # 前链表的下个节点是后链表的头节点
            cur1.next = cur2
            # 后链表的下个节点是前链表的的下个节点
            cur2.next = next1
            # 更新cur1与cur2节点
            cur1, cur2 = next1, next2

        return head
