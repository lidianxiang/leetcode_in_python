"""
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。


思路：将两个链表想象成前段不同但后段相同的两条路，现在有两个运动速度一样的运动员从两条路的起点开始跑，当跑到路的终点时又跳到另一条路的起点开始跑。则运动员第二次到达两条路的交叉路口时，他们所跑过的距离一样：两条路相交前的距离之和加上后面的重叠部分！因为速度一样，所以必然会在交叉路口相遇，即相遇点就是该题所求的相交节点！
代码化：设置两个分别指向链表头部的指针，同步往后移动，到达末尾便跳向另一个链表的头部，当两个指针到达同一节点时，便是相交的起始节点。

"""


# definition a singly-link list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB

        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
