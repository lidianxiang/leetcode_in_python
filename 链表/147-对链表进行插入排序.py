"""
对链表进行插入排序。

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 判断特殊情况
        if not head or not head.next:
            return head
        # 创建一个哑节点，指向head
        dummy = ListNode(-1)
        dummy.next = head
        # 循环节点
        while head.next:
            # 当链表的当前节点小于后面一个节点时，直接pass
            if head.val <= head.next.val:
                # 直接跳到下个节点
                head = head.next
            # 当链表的当前节点大于等于后面一个节点时
            else:
                # 创建一个节点，临时保存用于比较的head的下个节点
                temp = head.next
                # 创建新的指针q
                q = dummy
                head.next = head.next.next
                # 将temp（head.next）与排序好的前面节点逐一比较，如果q.next小于temp.val,直接逃过
                while q.next and q.next.val < temp.val:
                    q = q.next
                # 否则调换两者的顺序
                temp.next = q.next
                q.next = temp
        return dummy.next
