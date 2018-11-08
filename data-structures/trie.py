class Node:
    def find_definitions(self, word, defs):
        if self.meaning is not None:
            defs[word] = self.meaning

        for letter, child in self.children.items():
            child.find_definitions(word + letter, defs)

        return defs

    def __init__(self):
        self.meaning = None
        self.children = {}

    def __str__(self):
        return '{{meaning: {0}, children: {1}}}'.format(self.meaning, {k: v.__str__() for k, v in self.children.items()}.__str__().replace('\'', ''))


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

    def get_definitions(self):
        return self.root.find_definitions('', {})

    def __str__(self):
        return self.root.__str__()


trie = Trie()
trie.add('carpa', 'um peixe')
trie.add('capivara', 'melhor animal')
trie.add('chão', 'o que te impede de cair infinitamente')
trie.add('chato', 'minions')
trie.add('paçoca', 'não começa com c')

print(trie)
print()
print({k: v for k, v in trie.get_definitions().items()})
