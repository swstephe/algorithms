# -*- coding: utf-8 -*-
import math


class Heap(object):
    @staticmethod
    def left(parent):
        return 2*parent + 1

    @staticmethod
    def right(parent):
        return 2*parent + 2

    @staticmethod
    def parent(child):
        return (child - 1) // 2

    @staticmethod
    def walk_up(child):
        parent = Heap.parent(child)
        while parent >= 0:
            yield parent, child
            parent, child = Heap.parent(parent), parent

    def __init__(self, *args):
        self.data = [value for value in args]

    def order(self, parent, child):
        raise NotImplementedError("Heap.order")

    def walk_down(self, parent=0):
        n = len(self.data)
        child = Heap.left(parent)
        while child < n:
            right = child + 1
            if right < n and not self.order(child, right):
                child = right
            yield parent, child
            parent, child = child, Heap.left(child)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_valid(self, parent=0):
        n = len(self.data)
        if parent >= n:
            return True
        left, right = Heap.left(parent), Heap.right(parent)
        if left < n and not self.order(parent, left):
            print('left({}={}) > i({}={})'.format(left, self.data[left], parent, self.data[parent]))
            return False
        if right < n and not self.order(parent, right):
            print('right({}) > i({})'.format(right, parent))
            return False
        return self.is_valid(left) and self.is_valid(right)

    def push(self, value):
        self.data.append(value)
        for parent, child in self.walk_up(len(self.data) - 1):
            if not self.order(parent, child):
                self.swap(parent, child)
            else:
                break

    def pop(self):
        n = len(self.data)
        if n == 0:
            return None
        if n == 1:
            return self.data.pop()
        self.swap(0, n - 1)
        value = self.data.pop()
        for parent, child in self.walk_down(0):
            if not self.order(parent, child):
                self.swap(parent, child)
            else:
                break
        return value

    # 0
    # 1 2
    # 3 4 5 6
    # 7 8 9 10 11 12
    def __str__(self):
        n = len(self.data)
        if n == 0:
            return '<empty>'
        h = int(math.log(n, 2)) + 1
        s = ''
        for i in range(h):
            s += ' '.join(str(d) for d in self.data[2**i - 1:2**(i + 1) - 1]) + '\n'
        return s


class MinHeap(Heap):
    def order(self, parent, child):
        return self.data[parent] < self.data[child]


class MaxHeap(Heap):
    def order(self, parent, child):
        return self.data[parent] > self.data[child]


def main(n):
    heap = MinHeap()
    for i in reversed(range(n)):
        print('-', 'insert', i)
        heap.push(i)
        print(heap)
        heap.is_valid()
    print('-'*20)
    for parent, child in heap.walk_up(n - 1):
        print('*', parent, child)
    print('-'*20)
    for parent, child in heap.walk_down(0):
        print('*', parent, child)
    print('-'*20)
    while heap.data:
        print('-', 'pop', heap.pop())
        print(heap)
        heap.is_valid()


if __name__ == '__main__':
    main(20)
