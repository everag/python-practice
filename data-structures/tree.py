class Node:
    value = None
    children = []

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        node_str = str(self.value)
        if len(self.children) > 0:
            node_str += '->('
            for child in self.children:
                node_str += str(child) + ','
            node_str += ')'
        return node_str.replace(',)', ')')

    def add(self, new_child, *args):
        if len(args) is 0:
            self.children.append(Node(new_child))
        else:
            for child in self.children:
                if child.value is args[0]:
                    child.add(new_child, *args[1:])
                    return
            raise ValueError

    def prune(self, *args):
        for child in self.children:
            if child.value is args[0]:
                if len(args) is 1:
                    self.children.remove(child)
                    return
                else:
                    child.prune(*args[1:])
                    return
        raise ValueError


class Tree:
    root = None

    def __init__(self, root):
        self.root = Node(root)

    def __str__(self):
        return self.root.__str__()

    def add(self, child, *args):
        if self.root.value is not args[0]:
            raise ValueError
        self.root.add(child, *args[1:])
        print('add  : {0}'.format(self.__str__()))

    def prune(self, *args):
        if self.root.value is not args[0]:
            raise ValueError
        self.root.prune(*args[1:])
        print('prune: {0}'.format(self.__str__()))


tree = Tree(1)

assert tree.root is not None
assert tree.root.value is 1
assert str(tree) == '1'

tree.add(2, 1)

assert len(tree.root.children) is not 0
assert len(tree.root.children) is 1
assert tree.root.children[0].value is 2
assert str(tree) == '1->(2)'

tree.add(5, 1, 2)
assert str(tree) == '1->(2->(5))'

tree.add(7, 1, 2)
assert str(tree) == '1->(2->(5,7))'

tree.add(9, 1, 2)
assert str(tree) == '1->(2->(5,7,9))'

tree.add(10, 1, 2, 9)
assert str(tree) == '1->(2->(5,7,9->(10)))'

tree.add(11, 1, 2, 9, 10)
assert str(tree) == '1->(2->(5,7,9->(10->(11))))'

tree.prune(1, 2, 9, 10)
assert str(tree) == '1->(2->(5,7,9))'

tree.prune(1, 2)
assert str(tree) == '1'
