"""

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""


# definition a singly-linked list
class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        pre = head
        while head:
            next = head.next  # 缓存当前节点的向后指针，待下次迭代用
            head.next = pre  # 这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
            pre = head  # 作为下次迭代时的（当前节点的）向前指针
            head = next  # 作为下次迭代时的（当前）节点
        return pre  # 返回头指针，头指针就是迭代到最后一次时的head变量（赋值给了pre）
