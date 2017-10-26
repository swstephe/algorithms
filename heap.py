# -*- coding: utf-8 -*-
N = 3


class Heap(object):
    direction = None

    def __init__(self, *args):
        self.data = [value for value in args]

    @property
    def height(self):
        n = len(self.data)
        h = 0
        total = 0
        while n > total:
            total += N**h
            h += 1
        return h

    @staticmethod
    def child(parent, i):
        return N*parent + i + 1

    @staticmethod
    def parent(child):
        return (child - 1) // N

    def extreme(self, parent):
        children = self.data[self.child(parent, 0):self.child(parent, N)]
        if not children:
            return None
        return children.index(reduce(lambda a, x: a if cmp(a, x) == self.direction else x, children))

    @staticmethod
    def walk_up(child):
        parent = Heap.parent(child)
        while parent >= 0:
            yield parent, child
            parent, child = Heap.parent(parent), parent

    def walk_down(self, parent=0):
        n = len(self.data)
        while parent < n:
            child = self.extreme(parent)
            if child is None:
                break
            child = Heap.child(parent, child)
            yield parent, child
            parent = child

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_valid(self, parent=0):
        n = len(self.data)
        if parent >= n:
            return True
        child = Heap.child(parent, 0)
        for child in range(child, min(n, child + N)):
            if cmp(self.data[parent], self.data[child]) not in (0, self.direction):
                print 'cmp({}={}, {}={}) != {}'.format(
                    parent, self.data[parent],
                    child, self.data[child],
                    self.direction
                )
                return False
            if not self.is_valid(child):
                return False
        return True

    def push(self, value):
        self.data.append(value)
        for parent, child in self.walk_up(len(self.data) - 1):
            if cmp(self.data[parent], self.data[child]) in (0, self.direction):
                break
            self.swap(parent, child)

    def pop(self):
        n = len(self.data)
        if n == 0:
            return None
        if n == 1:
            return self.data.pop()
        self.swap(0, n - 1)
        value = self.data.pop()
        for parent, child in self.walk_down():
            if cmp(self.data[parent], self.data[child]) in (0, self.direction):
                break
            self.swap(parent, child)
        return value

    def __str__(self):
        h = self.height
        if h == 0:
            return '<empty>'
        s = []
        o = 0
        for i in range(h):
            w = N**i
            s.append(' '.join(str(d) for d in self.data[o:o + w]))
            o += w
        return '\n'.join(s)


class MinHeap(Heap):
    direction = -1


class MaxHeap(Heap):
    direction = 1


