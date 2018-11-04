# TODO: Reuse LinkedList?


class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        item_str = str(self.value)
        if self.next is not None:
            item_str += ' ' + self.next.__str__()
        return item_str


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        return self.top.__str__() if self.top is not None else ''

    def push(self, value):
        item = Item(value)
        if self.top is not None:
            item.next = self.top
        self.top = item
        self.size += 1

    def peek(self):
        return self.top.value if self.top is not None else None

    def pop(self):
        if self.top is None:
            raise ReferenceError

        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value


stack = Stack()

assert stack.size is 0
assert stack.top is None
assert stack.__str__() == ''
assert stack.peek() is None

stack.push("bottom")

assert stack.size is 1
assert stack.top is not None
assert stack.__str__() == 'bottom'
assert stack.peek() is 'bottom'

stack.push(1)
stack.push(2)
stack.push(3)

assert stack.size is 4
assert stack.top is not None
assert stack.__str__() == '3 2 1 bottom'
assert stack.peek() is 3

popped = stack.pop()
assert stack.size is 3
assert stack.top is not None
assert stack.__str__() == '2 1 bottom'
assert stack.peek() is 2
assert popped is 3

stack.pop()
stack.pop()
assert stack.size is 1
assert stack.__str__() == 'bottom'

stack.push('top')
assert stack.size is 2
assert stack.__str__() == 'top bottom'
assert stack.peek() == 'top'

