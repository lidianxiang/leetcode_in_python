"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

"""


# difinition for singly-linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
        链表中的点已经相连，一次旋转操作意味着：
        先将链表闭合成环
        找到相应的位置断开这个环，确定新的链表头和链表尾
    """

    def rotateRight(self, head, k):
        if not head:
            return None
        if not head.next:
            return head

        old_tail = head
        # 链表长度
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        # 移动链表
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 断开链表
        new_tail.next = None

        return new_head


class Solution2(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        快慢指针法
        """
        # 下面有 if n==0 ...判断了，所以开头的判断可以省略
        # if not head or k<=0:
        #    return head
        # 创建一个特殊节点，快指针，慢指针，统计节点个数的cur
        p = ListNode(-1)
        cur, n, low, fast, p.next = head, 0, p, p, head
        # 统计链表个数
        while cur:
            cur, n = cur.next, n + 1
        # 边界条件不用忘记处理了
        if n == 0 or k % n == 0:
            return head
        # 还有一个边界条件不要忘了，k可能大于n，所以要取模
        k = k % n
        # 快指针先移动n步
        while fast.next and k > 0:
            fast, n = fast.next, k - 1
        # 快指针，慢指针一起移动，找到需要切割的点
        while fast.next:
            low, fast = low.next, fast.next
        # 改变链表的指向关系，注意这里的步骤不要乱了
        # 先让fast节点指向head(也就是p.next)
        # 再是head(也就是p.next)指向low的下一个节点
        # 这两步如果弄反了就会出现节点丢失了
        # 最后不要忘记将low.next置空
        fast.next, p.next, low.next = head, low.next, None
        return p.next
