"""

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3


递归函数返回的不重复子链的头结点，在回溯过程中，比较当前节点和子链头结点的val是否相同，若相同则保留当前节点（删除子链的头结点）。

"""

# definition for singly-linked list


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x


class Solution:

    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        child = self.deleteDuplicates(head.next)
        if child and child.val == head.val:
            head.next = child.next
            child.next = None
        return head
