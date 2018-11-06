# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/


class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        return '{{val:{0}, prev:{1}, next:{2}, child:{3}}}'.format(self.val, self.prev.val if self.prev is not None else None, self.next, self.child)


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head
        if head.next is not None or head.child is not None:
            self.visit(head, [])
        return head

    def visit(self, node, stack):
        if node.child is not None:
            if node.next is not None:
                nxt = node.next
                nxt.prev = None
                stack.append(nxt)
            node.next = node.child
            node.next.prev = node
            node.child = None
            self.visit(node.next, stack)
        else:
            if node.next is None and len(stack) > 0:
                node.next = stack.pop()
                node.next.prev = node

            if node.next is not None:
                self.visit(node.next, stack)


n1 = Node(1, None, None, None)
n2 = Node(2, n1, None, None)
n1.next = n2
n3 = Node(3, n2, None, None)
n2.next = n3

n4 = Node(4, None, None, None)
n2.child = n4

n5 = Node(5, n4, None, None)
n4.next = n5

n6 = Node(6, n5, None, None)
n5.next = n6

n7 = Node(7, None, None, None)
n5.child = n7

n1 = Solution().flatten(n1)

assert n1.__str__() == '{val:1, prev:None, next:{val:2, prev:1, next:{val:4, prev:2, next:{val:5, prev:4, next:{val:7, prev:5, next:{val:6, prev:7, next:{val:3, prev:6, next:None, child:None}, child:None}, child:None}, child:None}, child:None}, child:None}, child:None}'

# O(n)
# 1176ms - Can be optimized a lot. Beats 20% submissions though
