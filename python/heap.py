# -*- coding: utf-8 -*-
N = 3


class Heap(object):
    def __init__(self, *args, n=N):
        self.n = n
        self.data = [value for value in args]

    def cmp(self, i, j):
        raise NotImplementedError("cmp")

    def first(self, parent):
        raise NotImplementedError("first")

    def last(self, parent):
        raise NotImplementedError("last")

    def children(self, parent):
        n = len(self.data)
        first = self.child(parent, 0)
        if first >= n:
            return range(0)
        last = self.child(parent, self.n - 1)
        if last >= n:
            last = n - 1
        return range(first, last + 1)

    @property
    def height(self):
        n = len(self.data)
        h = 0
        while n > 0:
            n -= self.n**h
            h += 1
        return h

    @property
    def is_empty(self):
        return len(self.data) == 0

    def child(self, parent, i):
        return self.n*parent + i + 1

    def parent(self, child):
        if child > 0:
            return (child - 1) // self.n

    def walk_up(self, child):
        parent = self.parent(child)
        while parent is not None:
            yield parent, child
            parent, child = self.parent(parent), parent

    def walk_down(self, parent=0):
        n = len(self.data)
        while True:
            child = self.first(parent)
            if child >= n:
                break
            yield parent, child
            parent = child

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_valid(self, parent=0):
        for child in self.children(parent):
            if self.cmp(parent, child) == 1:
                return False
            if not self.is_valid(child):
                return False
        return True

    def push(self, value):
        self.data.append(value)
        for parent, child in self.walk_up(len(self.data) - 1):
            if self.cmp(parent, child) == 1:
                self.swap(parent, child)

    def heapify(self, parent=0):
        extreme = parent
        for i, child in enumerate(self.children(parent)):
            if self.cmp(extreme, child) == 1:
                extreme = child
        if extreme != parent:
            self.swap(extreme, parent)
            self.heapify(extreme)

    def pop(self):
        n = len(self.data)
        if n == 0:
            return None
        if n == 1:
            return self.data.pop()
        self.swap(0, n - 1)
        value = self.data.pop()
        self.heapify()
        return value

    def __str__(self):
        h = self.height
        if h == 0:
            return '<empty>'
        s = []
        o = 0
        for i in range(h):
            w = self.n**i
            s.append(' '.join(str(d) for d in self.data[o:o + w]))
            o += w
        return '\n'.join(s)


class MinHeap(Heap):
    def cmp(self, i, j):
        if self.data[i] < self.data[j]:
            return -1
        elif self.data[i] > self.data[j]:
            return 1
        else:
            return 0

    def first(self, parent):
        return self.child(parent, 0)

    def last(self, parent):
        return self.child(parent, self.n - 1)


class MaxHeap(Heap):
    def cmp(self, i, j):
        if self.data[i] > self.data[j]:
            return -1
        elif self.data[i] < self.data[j]:
            return 1
        else:
            return 0

    def first(self, parent):
        return self.child(parent, self.n - 1)

    def last(self, parent):
        return self.child(parent, 0)
