"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    两次遍历的方式很好理解，先遍历一次链表，求出链表的总长度。
    第二次遍历的时候，根据总长度k的值-n，就算出需要再遍历多少个节点，找到要删除的节点的前一个节点x。
    然后将x节点的next指针指向下下一个节点就可以删除节点了。

    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n <= 0:
            return head
        # 增加一个特殊节点，方便边界处理
        p = ListNode(-1)
        p.next, a, b, k = head, p, p, 0
        # 第一次遍历，计算链表总长度
        while a.next:
            a, k = a.next, k + 1
        # 如果链表总长度小于n，那就直接返回
        if k < n:
            return head
        # 计算第二次遍历多少个节点
        num = k - n
        # 第二次遍历，找到要删除节点的前一个节点
        while num > 0:
            b, num = b.next, num - 1
        # 删除节点，并返回
        b.next = b.next.next
        return p.next


class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 增加一个特殊节点方便边界判断
        p = ListNode(-1)
        p.next, a, b = head, p, p
        # 第一个循环，b指针先往前走n步
        while n > 0 and b:
            b, n = b.next, n - 1
        # 假设整个链表长5，n是10，那么第一次遍历完后b就等于空了
        # 于是后面的判断就不用做了，直接返回
        if not b:
            return head
        # 第二次，b指针走到链表最后，a指针也跟着走
        # 当遍历结束时，a指针就指向要删除的节点的前一个位置
        while b.next:
            a, b = a.next, b.next
        # 删除节点并返回
        a.next = a.next.next
        return p.next
