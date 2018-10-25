class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def nth(self, index):
        if index is 0:
            return self
        elif self.next is not None:
            index -= 1
            return self.next.nth(index)
        else:
            raise IndexError


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    def add(self, value):
        new_tail = Node(value)
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def prepend(self, value):
        head = Node(value)
        head.next = self.head
        self.head = head
        self.size += 1

    def insert(self, value, index):
        if (index + 1) is self.size:
            self.add(value)
        elif (index + 1) > self.size:
            raise IndexError
        else:
            curr_nth = self.head.nth(index)
            new_nth = Node(value)
            new_nth.next = curr_nth
            self.size += 1

            if index > 0:
                prev = self.head.nth(index - 1)
                prev.next = new_nth
            else:
                self.head = new_nth

    def delete(self, index):
        if (index + 1) > self.size:
            raise IndexError
        else:
            if index is 0:
                if self.size is 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.nth(index).next
            else:
                prev_nth = self.head.nth(index - 1)
                if (index + 1) < self.size:
                    prev_nth.next = self.head.nth(index).next
                else:
                    prev_nth.next = None
                    self.tail = prev_nth

            self.size -= 1


def show(arg):
    if isinstance(arg, LinkedList):
        show(arg.head)
    elif isinstance(arg, Node):
        print(arg.value, end=' ')
        if arg.next is not None:
            show(arg.next)
    else:
        raise TypeError("Param 1 must be a LinkedList or a Node")


lst = LinkedList(1)
# 1
lst.add(2)
# 1 2
lst.add(3)
# 1 2 3
lst.prepend(0)
# 0 1 2 3
lst.insert(5, 1)
# 0 5 1 2 3
lst.insert(6, 1)
# 0 6 5 1 2 3
lst.insert(6, 0)
# 6 0 6 5 1 2 3
lst.insert(7, 0)
# 7 6 0 6 5 1 2 3
lst.insert(9, 7)
# 7 6 0 6 5 1 2 3 9

show(lst)
print()

lst.delete(0)
# 6 0 6 5 1 2 3 9
lst.delete(0)
# 0 6 5 1 2 3 9
lst.delete(1)
# 0 5 1 2 3 9
lst.delete(1)
# 0 1 2 3 9
lst.delete(4)
# 0 1 2 3

show(lst)
