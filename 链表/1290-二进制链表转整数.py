"""
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

 

示例 1：



输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
示例 2：

输入：head = [0]
输出：0
示例 3：

输入：head = [1]
输出：1
示例 4：

输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
输出：18880
示例 5：

输入：head = [0,0]
输出：0
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    由于链表中从高位到低位存放了数字的二进制表示，
    因此我们可以使用二进制转十进制的方法，在遍历一遍链表的同时得到数字的十进制值。
    """
    def getDecimalValue(self, head):
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans


class Solution2:
    """位运算"""
    def getDecimalValue(self, head):
        res = 0
        tmp = head
        while tmp:
            res = (res << 1) | tmp.val
            tmp = tmp.next
        return res
