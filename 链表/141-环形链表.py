"""

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

"""


# definition a singly-linked list
class NodeList:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针法
class Solution:

    def hasCycle(self, head):

        if head is None:
            return False

        # 慢指针
        p = head
        # 快指针
        q = head
        while q:
            if q.next is None:
                return False
            else:
                p = p.next
                q = q.next.next
            if q == p:
                return True
        return False


# hash表的方式
class Solution2:
    def hasCycle(self, head):
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        return False
