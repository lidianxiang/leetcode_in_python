"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

"""


# definition for a singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        通过set集合的方式，首先遍历链表，检查节点是否存在在set中，没有则存入set中，当节点出现在
        set中，则证明这个节点是闭环的首个节点
        """
        # 创建一个集合，命名为visited
        visited = set()

        # 将head节点复制给一个新节点node，用于遍历链表
        node = head
        while node is not None:
            # 当node出现在set中，则这个node节点即为环的首个节点，并返回这个node
            if node in visited:
                return node
            else:
                # 否则的话，将节点存入set中
                visited.add(node)
                # 移动node
                node = node.next
        # 遍历完链表，没有则返回None
        return None


class Solution2:
    """
    阶段 1:
        这里我们初始化两个指针 - 快指针和慢指针。我们每次移动慢指针一步、快指针两步，直到快指针无法继续往前移动。如果在某次移动后，
        快慢指针指向了同一个节点，我们就返回它。否则，我们继续，直到 while 循环终止且没有返回任何节点，这种情况说明没有成环，我们返回 null 。

    阶段 2:
        给定阶段1找到的相遇点，阶段2将找到环的入口。首先我们初始化额外的两个指针：ptr1，指向链表的头，ptr2指向相遇点。
        然后，我们每次将它们往前移动一步，直到它们相遇，它们相遇的点就是环的入口，返回这个节点。

    """

    # 找到快慢指针相遇的节点，若是没有相遇的点，则证明链表没有环
    def getIntersect(self, head):
        fast = head
        slow = head
        # 判断快指针是否存在
        while fast is not None and fast.next is not None:
            # 快指针每次走两步
            fast = fast.next.next
            # 慢指针每次走一步
            slow = slow.next
            if fast == slow:
                # 返回快慢指针相遇的节点
                return slow
        # 若快慢指针不相遇，则表示链表不存在环，返回None
        return None

    # 找到环开始的节点
    def detectCycle(self, head: ListNode) -> ListNode:
        # 当head为空的情况
        if not head:
            return None
        # 调用getIntersect函数，并复制给intersect
        intersect = self.getIntersect(head)
        # 判断intersect是否为空
        if intersect is None:
            return None
        # 定义两个新的指针，一个从head开始，一个从快慢指针相遇的节点开始
        p1 = head
        p2 = intersect
        # 循环，两者相遇的节点即为环的开始节点
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        # 返回节点
        return p1
