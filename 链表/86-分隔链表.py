"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    1、初始化两个指针 before 和 after。在实现中，我们将两个指针初始化为哑 ListNode。这有助于减少条件判断。
    2、利用head指针遍历原链表。
    3、若head 指针指向的元素值 小于 x，该节点应当是 before 链表的一部分。因此我们将其移到 before 中。
    4、否则，该节点应当是after 链表的一部分。因此我们将其移到 after 中。
    5、遍历完原有链表的全部元素之后，我们得到了两个链表 before 和 after。原有链表的元素或者在before 中或者在 after 中，这取决于它们的值。
    6、现在，可以将 before 和 after 连接，组成所求的链表。
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # before 为指针，before_head为节点（哑节点），当head.val小于x值时候，将before指针指向head节点（存储小于x的节点）
        before = before_head = ListNode(-1)
        # after为指针，after_head为节点（哑节点），当head.val大于等于x值时候，将after指针指向head节点（存储大于等于x的节点）
        after = after_head = ListNode(-1)
        # 遍历head
        while head:
            # 当head节点的值小于x时候
            if head.val < x:
                # 将before指针指向head
                before.next = head
                # before指针向后移动一位
                before = before.next
            else:
                # 否则将head节点由after指针指向
                after.next = head
                # after指针向后移动一位
                after = after.next
            # head 节点循环
            head = head.next
        # 遍历完了后，aftre指针指向null
        after.next = None
        # before指针指向after_head节点，从而将before_head和after_head相连接组成一个链表
        before.next = after_head.next
        # 返回 before_head的下一位（因为before_head是哑节点）
        return before_head.next
