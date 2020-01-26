"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    暴力法
        1、遍历所有链表，将所有节点的值放到一个数组中。
        2、将这个数组排序，然后遍历所有元素得到正确顺序的值。
        3、用遍历得到的值，创建一个新的有序链表。
    """
    def mergeKLists(self, lists):

        self.nodes = []
        head = point = ListNode(-1)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


class Solution2:
    """用队列来模拟分治算法"""
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(self.mergeTwoLists(l1, l2))

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # 迭代
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        p = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next

        p.next = l1 if l1 is not None else l2
        return head.next
