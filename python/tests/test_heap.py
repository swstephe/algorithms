# -*- coding: utf-8 -*-
from heap import MinHeap, MaxHeap


def test_0():
    # 0
    # 1 2 3
    # 4 5 6   7 8 9   10 11 12
    heap = MinHeap(*range(13), n=3)
    assert heap.height == 3
    assert heap.parent(0) is None
    assert heap.child(0, 0) == 1
    assert heap.child(0, 1) == 2
    assert heap.child(0, 2) == 3
    assert heap.first(0) == 1
    assert heap.last(0) == 3
    assert heap.parent(1) == 0
    assert heap.child(1, 0) == 4
    assert heap.child(1, 1) == 5
    assert heap.child(1, 2) == 6
    assert heap.first(1) == 4
    assert heap.last(1) == 6
    assert heap.parent(2) == 0
    assert heap.child(2, 0) == 7
    assert heap.child(2, 1) == 8
    assert heap.child(2, 2) == 9
    assert heap.first(2) == 7
    assert heap.last(2) == 9
    assert heap.parent(3) == 0
    assert heap.child(3, 0) == 10
    assert heap.child(3, 1) == 11
    assert heap.child(3, 2) == 12
    assert heap.first(3) == 10
    assert heap.last(3) == 12
    assert heap.parent(4) == 1
    assert heap.parent(5) == 1
    assert heap.parent(6) == 1
    assert heap.parent(7) == 2
    assert heap.parent(8) == 2
    assert heap.parent(9) == 2
    assert heap.parent(10) == 3
    assert heap.parent(11) == 3
    assert heap.parent(12) == 3
    assert heap.is_valid()
    assert tuple(heap.walk_up(4)) == ((1, 4), (0, 1))
    assert tuple(heap.walk_up(5)) == ((1, 5), (0, 1))
    assert tuple(heap.walk_up(6)) == ((1, 6), (0, 1))
    assert tuple(heap.walk_up(7)) == ((2, 7), (0, 2))
    assert tuple(heap.walk_up(12)) == ((3, 12), (0, 3))
    assert tuple(heap.walk_down()) == ((0, 1), (1, 4))
    heap.push(14)
    assert heap.is_valid()
    heap.push(6)
    assert heap.is_valid()
    assert heap.pop() == 0
    assert heap.is_valid()
    assert heap.pop() == 1
    assert heap.is_valid()
    assert heap.pop() == 2
    assert heap.is_valid()


def test_1():
    heap = MaxHeap(*'abcdef', n=3)
    assert heap.height == 3

#     def extreme(self, parent):
#         children = self.data[self.child(parent, 0):self.child(parent, N)]
#         if not children:
#             return None
#         a = None
#         for x in children:
#             if ((a < x) - (a > x)) != self.direction:
#                 a = x
#         return children.index(a)
#
#     def walk_up(self, child):
#         parent = self.parent(child)
#         while parent >= 0:
#             yield parent, child
#             parent, child = self.parent(parent), parent
#
#     def walk_down(self, parent=0):
#         n = len(self.data)
#         while parent < n:
#             child = self.extreme(parent)
#             if child is None:
#                 break
#             child = Heap.child(parent, child)
#             yield parent, child
#             parent = child
#
#     def swap(self, i, j):
#         self.data[i], self.data[j] = self.data[j], self.data[i]
#
#     def is_valid(self, parent=0):
#         n = len(self.data)
#         if parent >= n:
#             return True
#         child = Heap.child(parent, 0)
#         for child in range(child, min(n, child + N)):
#             if cmp(self.data[parent], self.data[child]) not in (0, self.direction):
#                 print 'cmp({}={}, {}={}) != {}'.format(
#                     parent, self.data[parent],
#                     child, self.data[child],
#                     self.direction
#                 )
#                 return False
#             if not self.is_valid(child):
#                 return False
#         return True
#
#     def push(self, value):
#         self.data.append(value)
#         for parent, child in self.walk_up(len(self.data) - 1):
#             if cmp(self.data[parent], self.data[child]) in (0, self.direction):
#                 break
#             self.swap(parent, child)
#
#     def pop(self):
#         n = len(self.data)
#         if n == 0:
#             return None
#         if n == 1:
#             return self.data.pop()
#         self.swap(0, n - 1)
#         value = self.data.pop()
#         for parent, child in self.walk_down():
#             if cmp(self.data[parent], self.data[child]) in (0, self.direction):
#                 break
#             self.swap(parent, child)
#         return value
#
#     def __str__(self):
#         h = self.height
#         if h == 0:
#             return '<empty>'
#         s = []
#         o = 0
#         for i in range(h):
#             w = N**i
#             s.append(' '.join(str(d) for d in self.data[o:o + w]))
#             o += w
#         return '\n'.join(s)
#
#
# class MinHeap(Heap):
#     direction = -1
#
#
# class MaxHeap(Heap):
#     direction = 1
#
#
