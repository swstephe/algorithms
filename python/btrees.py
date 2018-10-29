# -*- coding: utf-8 -*-
M = 4


class Node(object):
    def __init__(self, degree):
        self.degree = degree
        self.keys = []
        self.children = []

    @property
    def count(self):
        return len(self.keys) + sum(child.count for child in self.children)

    @property
    def height(self):
        return (0 if self.leaf else self.children[0].height) + 1

    @property
    def leaf(self):
        return len(self.children) == 0

    def in_order(self):
        for i, key in enumerate(self.keys):
            if self.children:
                for k in self.children[i].in_order():
                    yield k
            yield key
        if self.children:
            for k in self.children[-1].in_order():
                yield k

    def insert(self, key):
        if self.leaf:
            if len(self.keys) < self.degree:
                self.keys.append(key)


    def search(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self
            if k > key:
                return self.children[i].search(key)



class BTree(object):
    def __init__(self, degree):
        self.degree = degree
        self.root = None

    @property
    def count(self):
        return self.root.count if self.root else 0

    @property
    def height(self):
        return self.root.height if self.root else 0

    @property
    def is_empty(self):
        return self.root == None or self.root.count == 0

    def in_order(self):
        return list(self.root.in_order()) if self.root else []

    def get(self, key):
        if self.root:
            return self.root.search(key)

    def put(self, key, value):
        u = self.insert(self.root, key, value, self.height)
        self.n += 1
        if u is None:
            return

        # need to split root
        t = Node(2)
        t.children[0] = Entry(self.root.children[0].key, None, self.root)
        t.children[1] = Entry(u.children[0].key, None, u)
        self.root = t
        self.height += 1

    def insert(self, key):
        if self.root is None:
            self.root = Node(self.degree)
        self.root.insert(key)

    def split(self, h):
        t = Node(M/2)
        h.m = M/2
        for j in range(M/2):
            t.children[j] = h.children[M/2 + j]
        return t

    def __str__(self):
        return str(self.root)
