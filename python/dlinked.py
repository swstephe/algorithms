# -*- coding: utf8 -*-


class Node(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class List(object):
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.extend(args)

    def __bool__(self):
        return self.head is not None

    def __getitem__(self, item):
        if not self:
            raise ValueError("list is empty")
        if item == 0:
            return self.head.value
        if item < 0:
            for i, value in enumerate(reversed(self)):
                if i == -item - 1:
                    return value
        else:
            for i, value in enumerate(self):
                if i == item:
                    return value
        raise IndexError("slist index out of range")

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __len__(self):
        return sum(1 for _ in self)

    def __reversed__(self):
        node = self.tail
        while node is not None:
            yield node.value
            node = node.prev

    def __str__(self):
        return '[{}]'.format(', '.join(repr(value) for value in self))

    def append(self, value):
        print(self)
        node = Node(value, prev=self.tail)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def clear(self):
        node = self.head
        while node:
            del node
            node = node.next
        self.head = None
        self.tail = None

    def copy(self):
        return self.__class__(self)

    def count(self, x):
        return sum(1 for value in self if value == x)

    def extend(self, iterable):
        prev = self.tail
        for value in iterable:
            node = Node(value)
            if prev is None:
                self.head = node
            else:
                prev.next, node.prev = node, prev
            prev = self.tail = node

    def index(self, value, start=None, end=None):
        i = start or 0
        for val in self:
            if val == value:
                return i
            i += 1
            if end and i > end:
                break
        raise ValueError('%r is not in slist' % value)

    def insert(self, i, value):
        node = self.head
        while node.next and i > 0:
            node = node.next
            i -= 1
        self.tail = node.next = Node(value, node.next)

    def pop(self, i=-1):
        if not self:
            raise IndexError('pop from empty list')
        node = self.tail if i < 0 else self.head
        while node is not None:
            if i == (-1 if i < 0 else 0):
                try:
                    if node.prev:
                        node.prev.next = node.next
                    else:
                        self.head = node.next
                    if node.next:
                        node.next.prev = node.prev
                    else:
                        self.tail = node.prev
                    return node.value
                finally:
                    del node
            node = node.prev if i < 0 else node.next
            i += 1 if i < 0 else -1
        raise IndexError('pop index out of range')

    def prepend(self, value):
        node = Node(value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def remove(self, value):
        prev, node = None, self.head
        while node is not None:
            if node.value == value:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                del node
                return
            prev, node = node, node.next
        raise ValueError('slist.remove(x): x not in list')

    def reverse(self):
        node = self.head
        while node is not None:
            node.next, node.prev, node = node.prev, node.next, node.next
        self.head, self.tail = self.tail, self.head
