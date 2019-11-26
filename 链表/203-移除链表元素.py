"""

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


# definition a singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归的方式
class Solution:
    def removeElements(self, head, val):
        if head:
            head.next = self.removeElements(head.next ,val)
        return head.next if head and head.val == val else head


class Solution2(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        # 因为要删除的可能是链表的第一个元素，所以用一个h节点来做处理
        # 最后只要返回h的下一个节点即可
        p.next, h = head, p
        # 注意遍历的条件是p.next不为空
        while p.next:
            # 如果p的下一个节点的值==val
            # P就指向下下一个，这就删掉了指定的节点
            if p.next.val == val:
                p.next = p.next.next
                # 注意这里的continue
                # 因为循环最后还有一个P=p.next，所以要跳过
                continue
            # 不用continue用else的方式也是可以的
            p = p.next

        return h.next

