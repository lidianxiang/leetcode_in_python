"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """栈"""
    def reverseKGroup(self, head, k):
        # 哑节点
        dummy = ListNode(-1)
        # 移动指针
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意，目前tmp所在k+1位置
            # 说明剩下的链表不够k个，跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下的链表链接起来
            p.next = tmp
            head = tmp
        return dummy.next


class Solution2:
    """尾插法"""
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break

            head = pre.next
            while pre.next != tail:
                # 获取下一个元素
                cur = pre.next
                # pre与cur.next连接起来，此时的cur孤立地掉了出来
                pre.next = cur.next
                # 和剩余的链表连接起来
                cur.next = tail.next
                # 插在tail后面
                tail.next = cur
            # 改变pre和tail的值
            pre = head
            tail = head
        return dummy.next


class Solution3:
    """递归法"""
    def reverseKGroup(self, head, k):
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head
