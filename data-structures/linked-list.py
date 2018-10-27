class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        node_str = str(self.value)
        if self.next is not None:
            node_str += ' ' + self.next.__str__()
        return node_str

    def nth(self, index):
        if index is 0:
            return self
        elif self.next is not None:
            index -= 1
            return self.next.nth(index)
        else:
            raise IndexError


class LinkedList:
    head = None
    tail = None
    size = 0

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size += 1

    def __str__(self):
        return self.head.__str__()

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
        elif (index + 1) < self.size:
            if index > 0:
                prev = self.head.nth(index - 1)
                curr_nth = prev.next
            else:
                curr_nth = self.head.nth(index)

            new_nth = Node(value)
            new_nth.next = curr_nth

            if index > 0:
                prev.next = new_nth
            else:
                self.head = new_nth

            self.size += 1
        else:
            raise IndexError

    def delete(self, index):
        if (index + 1) <= self.size:
            if index is 0:
                if self.size is 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.nth(index).next
            else:
                prev_nth = self.head.nth(index - 1)
                if (index + 1) < self.size:
                    prev_nth.next = prev_nth.next.next
                else:
                    prev_nth.next = None
                    self.tail = prev_nth

            self.size -= 1
        else:
            raise IndexError


lst = LinkedList(1)
assert lst.__str__() == '1'

lst.add(2)
assert lst.__str__() == '1 2'

lst.add(3)
assert lst.__str__() == '1 2 3'

lst.prepend(0)
assert lst.__str__() == '0 1 2 3'

lst.insert(5, 1)
assert lst.__str__() == '0 5 1 2 3'

lst.insert(6, 1)
assert lst.__str__() == '0 6 5 1 2 3'

lst.insert(6, 0)
assert lst.__str__() == '6 0 6 5 1 2 3'

lst.insert(7, 0)
assert lst.__str__() == '7 6 0 6 5 1 2 3'

lst.insert(9, 7)
assert lst.__str__() == '7 6 0 6 5 1 2 3 9'

print(lst)

lst.delete(0)
assert lst.__str__() == '6 0 6 5 1 2 3 9'

lst.delete(0)
assert lst.__str__() == '0 6 5 1 2 3 9'

lst.delete(1)
assert lst.__str__() == '0 5 1 2 3 9'

lst.delete(1)
assert lst.__str__() == '0 1 2 3 9'

lst.delete(4)
assert lst.__str__() == '0 1 2 3'

print(lst)
