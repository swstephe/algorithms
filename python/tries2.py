# -*- coding: utf8 -*-


class Node(object):
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.children = [None] * len(self.alphabet)
        self.value = None

    def __iter__(self):
        for char, child in zip(self.alphabet, self.children):
            if child is None:
                continue
            if child.value is not None:
                yield char, child.value
            for suffix, value in child:
                yield char + suffix, value

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        return '{{{}}}/{}'.format(', '.join(
            '{}: {}'.format(char, node)
            for char, node in zip(self.alphabet, self.children)
            if node is not None
        ), self.value)

    def find_node(self, key):
        if key == '':
            return self
        try:
            i = self.alphabet.index(key[0])
        except ValueError:
            return
        if self.children[i] is not None:
            return self.children[i].find_node(key[1:])

    def insert(self, key, value):
        if key == '':
            self.value = value
        else:
            i = self.alphabet.index(key[0])
            if self.children[i] is None:
                self.children[i] = Node(self.alphabet)
            self.children[i].insert(key[1:], value)


class Trie(object):
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.root = Node(self.alphabet)

    def __contains__(self, item):
        return self.root.find_node(item) is not None

    def __iter__(self):
        yield from self.root

    def __len__(self):
        return len(self.root)

    def __str__(self):
        return str(self.root)

    def find(self, key):
        node = self.root.find_node(key)
        if node is not None:
            return node.value

    def find_prefix(self, key):
        node = self.root.find_node(key)
        if node is not None:
            result = set()
            for k, v in node:
                if isinstance(v, set):
                    result |= v
                else:
                    result.add(v)
            return result

    def insert(self, key, value):
        self.root.insert(key, value)

