# -*- coding: utf-8 -*-
import heapq


class MinHeap(object):
    def __init__(self, *args):
        self.heap = list(args)
        heapq.heapify(self.heap)

    @property
    def height(self):
        n = len(self.heap)
        h = 0
        while n > 0:
            n -= 2**h
            h += 1
        return h

    @property
    def is_empty(self):
        return len(self.heap) == 0

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)

    def __str__(self):
        h = self.height
        if h == 0:
            return '<empty>'
        s = []
        o = 0
        for i in range(h):
            w = 2**i
            s.append(' '.join(str(d) for d in self.heap[o:o + w]))
            o += w
        return '\n'.join(s)
