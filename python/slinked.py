# -*- coding: utf8 -*-


class Node(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class List(object):
    def __init__(self, *args):
        self.head = None
        self.extend(args)

    def __bool__(self):
        return self.head is not None

    def __getitem__(self, item):
        if not self:
            raise ValueError("list is empty")
        if item < 0:
            item += len(self)
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

    def __str__(self):
        return '[{}]'.format(', '.join(repr(value) for value in self))

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.tail.next = Node(value)

    def clear(self):
        node = self.head
        while node:
            del node
            node = node.next
        self.head = None

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
                prev.next = node
            prev = node

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
        node.next = Node(value, node.next)

    def pop(self, i=-1):
        if not self:
            raise IndexError('pop from empty list')
        if i < 0:
            i = len(self) + i
        prev, node = None, self.head
        while node is not None:
            if i == 0:
                try:
                    if prev:
                        prev.next = node.next
                    else:
                        self.head = node.next
                    return node.value
                finally:
                    del node
            prev, node = node, node.next
            i -= 1
        raise IndexError('pop index out of range')

    def prepend(self, value):
        self.head = Node(value, self.head)

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
        prev, node = None, self.head
        while node is not None:
            prev, node.next, node = node, prev, node.next
        self.head = prev

    @property
    def tail(self):
        if not self:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node
