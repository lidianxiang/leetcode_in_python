"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
"""



# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        # 新建一个字典用来存储数据
        self.visitedHash = {}

    def copyRandomList(self, head):
        # 特判
        if head is None:
            return None
        # 当节点在字典中存储下来
        if head in self.visitedHash:
            return self.visitedHash[head]
        #当当前节点还没有拷贝过，创建一个新的节点
        node = Node(head.val, None, None)
        # 将该节点放入已访问的字典中
        self.visitedHash[head] = node
        # 回溯调用
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution2:
    """迭代"""
    def __init__(self):
        self.visited = {}

    def getCloneNode(self, node):
        """
        拷贝节点
        """
        # 当节点不为空
        if node:
            # 当节点在字典中
            if node in self.visited:
                return self.visited[node]
            else:
                # 当节点不在字典中
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        # 特判
        if not head:
            return None

        old_node = head
        # 新建一个新的节点
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        # 迭代指针链表
        while old_node != None:
            # 复制旧节点的next指针和random指针
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)
            # 移动指针
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]


class Solution3:
    def copyRandomList(self, head):
        # 特判
        if not head:
            return None
        # 第一次遍历，将每个新生成的节点放在对应的旧节点的后面
        # 例如：A -> A'-> B -> B'- C -> C'
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node

            p = new_node.next
        # 第二遍修改每个新节点的next和random指针
        p = head
        while p:
            next_origin = p.next.next
            # 修改新节点的next
            p.next.next = next_origin.next if next_origin else None
            # 修改新节点的random
            p.next.random = p.random.next if p.random else None
            # 更新下一个旧节点
            p = next_origin
        return head.next
