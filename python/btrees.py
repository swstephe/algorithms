# -*- coding: utf-8 -*-

M = 4


class Node(object):
    def __init__(self):
        self.keys = []
        self.children = []

    def search(self, key):
        if ht == 0:
            for child in self.children:
                if key == child.key:
                    return child.value
        else:
            for j in range(len(self.children)):
                if key < self.children[j + 1].key:
                    return self.children[j].search(key, ht - 1)
        return None



class BTree(object):
    def __init__(self):
        self.root = Node(0)
        self.height = 0
        self.n = 0

    @property
    def is_empty(self):
        return self.n == 0

    def get(self, key):
        return self.search(self.root, key, self.height)

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

    def insert(self, h, key, val, ht):
        j = 0
        t = Entry(key, val, None)

        if ht == 0:
            while j < h.m:
                if key < h.children[j].key:
                    break
                j += 1
        else:
            while j < h.m:
                if j + 1 == h.m or key < h.children[j + 1].key:
                    u = self.insert(h.children[j]._next, key, val, ht - 1)
                    j += 1
                    if u is None:
                        return None
                    t.key = u.children[0].key
                    t._next = u
                    break
                j += 1
        for i in range(h.m, j, -1):
            h.children[i] = h.children[i - 1]
        h.children[j] = t
        h.m += 1
        if h.m < M:
            return None
        return self.split(h)

    def split(self, h):
        t = Node(M/2)
        h.m = M/2
        for j in range(M/2):
            t.children[j] = h.children[M/2 + j]
        return t

    def __str__(self):
        def inner(h, ht, indent):
            s = ''
            children = h.children
            if ht == 0:
                for j in range(h.m):
                    s += indent + children[j].key + ' ' + children[j].value + '\n'
            else:
                for j in range(h.m):
                    if j > 0:
                        s += indent + '(' + children[j].key + ')\n'
                    s += inner(children[j]._next, ht - 1, indent + '    ')
            return s

        return inner(self.root, self.height, '') + '\n'