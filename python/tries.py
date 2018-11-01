# -*- coding: utf8 -*-
from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.value = None

    def __iter__(self):
        for char, node in sorted(self.children.items()):
            if node.value is not None:
                yield char, node.value
            for suffix, value in node:
                yield char + suffix, value

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        gen = (
            '{}: {}'.format(char, node)
            for char, node in sorted(self.children.items())
        )
        return '{{{}}}/{}'.format(', '.join(gen), self.value)

    def find(self, key):
        if not key:
            return self.value
        child = self.children.get(key[0])
        if child is not None:
            return child.find(key[1:])

    def find_prefix(self, key):
        if not key:
            result = set()
            for k, v in self:
                result |= v
            return result
        child = self.children.get(key[0])
        if child is not None:
            return child.find_prefix(key[1:])

    def insert(self, key, value):
        if key:
            self.children[key[0]].insert(key[1:], value)
        else:
            self.value = value


class Trie(object):
    def __init__(self):
        self.root = Node()

    def __iter__(self):
        yield from self.root

    def __str__(self):
        return str(self.root)

    def find(self, key):
        return self.root.find(key)

    def find_prefix(self, key):
        return self.root.find_prefix(key)

    def insert(self, key, value):
        self.root.insert(key, value)

