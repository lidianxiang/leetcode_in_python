"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

"""


# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        可以考虑使用栈的结构（先进后出，后进先出的特点），每两个放入一个栈里面
        :param head:
        :return:
        """
        # 当链表不足两个时
        if not (head and head.next):
            return head
        # 定义一个节点
        p = ListNode(-1)
        # 用stack保存每次迭代的两个节点
        # head指向新的p节点， 函数结束时返回head.next即可
        cur, head, stack = head, p, []
        while cur and cur.next:
            # 将两个节点放入stack中
            _, _ = stack.append(cur), stack.append(cur.next)
            # 当前节点往前走两步
            cur = cur.next.next
            # 从stack中弹出先前的两个节点（先进后出）
            p.next = stack.pop()
            p.next.next = stack.pop()
            # 然后用p节点指向新的节点
            p = p.next.next
        # 注意边界条件， 当链表长度为奇数时，cur就不为空了，此时将p节点的next指向cur
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next


class Solution2:
    """
    迭代实现就比stack方式复杂多了，需要很小心的处理节点的指向。
    这里我们需要三个指针，a，b，tmp。
    假设链表是
    1->2->3->4->5->6
    在迭代的时候，每次处理两个节点，于是第一轮a指向1，b指向2。
    第二轮的时候a指向3，b指向4。第三轮的时候a指向5，b指向6。
    我们通过 a.next = b.next，以及b.next=a就把两个指针的位置反转了，于是1->2就变成2->1。
    但这里有一个细节需要处理，当我们第二轮迭代的时候，a指向3，b指向4。按照题目要求，最终应该是2->1->4->3。
    也就是节点1需要跟节点4串起来，只有两个指针就没法弄了，所以需要第三个指针tmp，用来记录上一轮a的位置，然后下一轮迭代的时候，将原先的a(也就是节点1)指向4。

    """
    def swapPair(self, head):
        # 增加一个特殊节点方便处理
        p = ListNode(-1)
        # 创建a b两个指针， 还有一个tmp指针
        a, b, p.next, tmp = p, p, head, p

        while b.next and b.next.next:
            # a前进一位， b前进两位
            a, b = a.next, b.next.next
            # 这步很关键，tmp指针用来处理边界条件的
            # 假设链表是1->2->3->4，a指向1，b指向2
            # 改变a和b的指向，于是就变成2->1，但是1指向谁呢？
            # 1是不能指向2的next，1应该指向4，而循环迭代的时候一次处理2个节点
            # 1和2的关系弄清楚了，3和4的关系也能弄清楚，但需要一个指针来处理
            # 2->1，4->3的关系，tmp指针就是干这个用的
            tmp.next, a.next, b.next = b, b.next, a
            # 现在链表就变成2->1->3->4
            # tmp和b都指向1节点，等下次迭代的时候
            # a就变成3，b就变成4，然后tmp就指向b，也就是1指向4
            tmp, b = a, a
        return p.next

