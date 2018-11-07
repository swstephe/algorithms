# -*- coding: utf-8 -*-
from heap2 import MinHeap


def test_0():
    #           0
    #     1             2
    #  3    4         5   6
    # 7 8  9 10    11 12
    heap = MinHeap(*range(13))
    print(heap)
    assert heap.height == 4
    heap.push(14)
    heap.push(6)
    assert heap.pop() == 0
    assert heap.pop() == 1
    assert heap.pop() == 2


