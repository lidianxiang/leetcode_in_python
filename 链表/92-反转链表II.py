"""反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseBetween(self, head, m, n):

        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head


class Solution2:

    def reverseBetween(self, head, m, n):
        if not head:
            return None
        # 初始化cur和prev指针用于m到n之间的链表的反转
        cur, prev = head, None
        # 循环m次，使得prev和cur到达指定地点
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1
        # tail指针指向第m个节点，因为反转后它是反转部分的结尾，所以起名tail
        # con指针指向第m-1节点，即第m个节点的前一个节点
        tail, con = cur, prev
        # 开始反转指定部分的链表
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        # 将con指针指向prev
        if con:
            con.next = prev
        else:
            head = prev
        # tail指向cur，完成最后的反转
        tail.next = cur
        return head


class Solution3:
    def reverseBetween(self, head, m, n):
        # 特判
        if head is None or head.next is None:
            return head
        # 哑节点
        dummy = ListNode(-1)
        dummy.next = head
        head1 = dummy
        # 前m-1个节点不用反转，
        for i in range(m - 1):
            head1 = head1.next
        # 开始反转的开始节点
        p = head1.next
        # 在n - m节点中进行反转
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next

