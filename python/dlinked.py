# -*- coding: utf8 -*-


class Node(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class List(object):
    def __init__(self, initlist=None):
        self.head = None
        self.tail = None
        self.length = 0
        if initlist is not None:
            self.extend(initlist)

    def _iter(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def _riter(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.prev

    def __add__(self, other):
        copy = self.copy()
        copy.extend(other)
        return copy

    def __bool__(self):
        return self.head is not None

    def __cmp__(self, other):
        node = self.head
        for value in other:
            if node is None or node.value < value:
                return -1
            if node.value > value:
                return 1
            node = node.next
        if node is None:
            return 0
        return 1

    def __contains__(self, value):
        for v in self:
            if v is value or v == value:
                return True
        return False

    def __delitem__(self, item):
        node = self.head
        while node is not None and item > 0:
            node = node.next
            item -= 1
        if node is None:
            raise IndexError("dlist assignment index out of range")
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        del node

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ge__(self, other):
        return self.__cmp__(other) != -1

    def __getitem__(self, item):
        if not self:
            raise ValueError("dlist is empty")
        if not isinstance(item, int):
            raise ValueError("expected integer argument")
        if item < 0:
            item += len(self)
        if item == 0:
            return self.head.value
        if item >= 0:
            for i, value in enumerate(self):
                if i == item:
                    return value
        raise IndexError("dlist index out of range")

    def __gt__(self, other):
        return self.__cmp__(other) == 1

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __imul__(self, n):
        copy = self.copy()
        for _ in range(n - 1):
            self.extend(copy)
        return self

    def __iter__(self):
        return (node.value for node in self._iter())

    def __le__(self, other):
        return self.__cmp__(other) != 1

    def __len__(self):
        return self.length

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __mul__(self, n):
        new_list = self.__class__()
        for i in range(n):
            new_list.extend(self)
        return new_list

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __radd__(self, other):
        copy = self.__class__(other)
        copy.extend(self)
        return copy

    def __repr__(self):
        return '[{}]'.format(', '.join(repr(value) for value in self))

    def __reversed__(self):
        return (node.value for node in self._riter())

    __rmul__ = __mul__

    def __setitem__(self, item, value):
        node = self.head
        while node is not None and item >= 0:
            node = node.next
            item -= 1
        if node is None:
            raise IndexError("dlist assignment index out of range")
        node.value = value

    def append(self, value):
        node = Node(value, prev=self.tail)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def clear(self):
        while self.head is not None:
            node, self.head = self.head, self.head.next
            del node
            self.length -= 1
        self.tail = None

    def copy(self):
        return self.__class__(self)

    def count(self, value):
        return sum(1 for v in self if v is value or v == value)

    def extend(self, values):
        for v in values:
            new_node = Node(v)
            if self.tail is None:
                self.head = self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def index(self, value, start=None, end=None):
        for i, node in enumerate(self._iter()):
            if start is not None and start > i:
                continue
            if end is not None and end < i:
                break
            if node.value is value or node.value == value:
                return i
        raise ValueError('%r is not in dlist' % value)

    def insert(self, i, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        elif i == 0:
            self.head = self.head.prev = Node(value, self.head)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
                i -= 1
                if i == 0:
                    break
            node.prev.next = Node(value, next=node.prev.next)
        self.length += 1

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

    def _bubble_sort(self, reverse=False, key=None):
        if key is None:
            def key(v):
                return v

        def cmp_func(a, b):
            result = key(a) < key(b)
            if reverse:
                result = not result
            return result

        # bubble sort
        while True:
            node, is_sorted = self.head, True
            while node is not None:
                if node.prev is not None and not cmp_func(node.prev.value, node.value):
                    node.prev.value, node.value, is_sorted = node.value, node.prev.value, False
                node = node.next
            if is_sorted:
                break

    def sort(self, reverse=False, key=None):
        self._bubble_sort(reverse=reverse, key=key)
