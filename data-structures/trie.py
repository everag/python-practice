class Node:
    def __init__(self):
        self.meaning = None
        self.children = {}

    def __str__(self):
        return '{{meaning:{0}, children:{1}}}'.format(self.meaning, {k: v.__str__() for k, v in self.children.items()})


class Trie:
    root = Node()

    def add(self, word, meaning):
        i = 0
        node = self.root
        while i < len(word):
            letter = word[i]
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
            i += 1
        node.meaning = meaning

    def __str__(self):
        return self.root.__str__()


trie = Trie()
trie.add('xunda', 'bunda')
print(trie)
