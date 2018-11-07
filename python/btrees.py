# -*- coding: utf-8 -*-
M = 4


class Node(object):
    def __init__(self, degree):
        self.degree = degree
        self.pairs = []
        self.children = []

    def __iter__(self):
        for i, pair in enumerate(self.pairs):
            if self.children:
                yield from self.children[i]
            yield pair
        if self.children:
            yield from self.children[-1]

    def __len__(self):
        return len(self.pairs) + sum(len(child) for child in self.children)

    def __reversed__(self):
        if self.children:
            yield from reversed(self.children[-1])
        for i, pair in reversed(enumerate(self.pairs)):
            yield pair
            if self.children:
                yield from self.children[i]

    @property
    def height(self):
        return (0 if self.is_leaf else self.children[0].height) + 1

    @property
    def is_leaf(self):
        return len(self.children) == 0

    def insert(self, key, value):
        if self.is_leaf:
            if len(self.pairs) > self.degree:
                self.split()
            self.pairs.append((key, value))

    def search(self, key):
        for i, pair in enumerate(self.pairs):
            if pair[0] == key:
                return self
            if pair[0] > key:
                return self.children[i].search(key)
        return self.children[-1].search(key)



class BTree(object):
    def __init__(self, degree):
        self.degree = degree
        self.root = None

    def __iter__(self):
        if self.root:
            yield from self.root

    def __len__(self):
        return len(self.root) if self.root else 0

    def __reversed__(self):
        if self.root:
            yield from reversed(self.root)

    @property
    def height(self):
        return self.root.height if self.root else 0

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(self.degree)
        self.root.insert(key, value)

    def search(self, key):
        if self.root:
            return self.root.search(key)

    def split(self, h):
        t = Node(M/2)
        h.m = M/2
        for j in range(M/2):
            t.children[j] = h.children[M/2 + j]
        return t

    def __str__(self):
        if self.root:
            return str(self.root)
        return '<empty>'
