# -*- coding: utf8 -*-


class Node(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class List(object):
    def __init__(self, initlist=None):
        self.head = None
        self.length = 0
        if initlist is not None:
            self.extend(initlist)

    @property
    def tail(self):
        if self.head is None:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node

    def _iter(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

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
        prev, node = None, self.head
        while node is not None and item > 0:
            prev, node = node, node.next
            item -= 1
        if node is None:
            raise IndexError("slist assignment index out of range")
        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next
        del node

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ge__(self, other):
        return self.__cmp__(other) != -1

    def __getitem__(self, item):
        if not self:
            raise ValueError("slist is empty")
        if not isinstance(item, int):
            raise ValueError("expected integer argument")
        if item < 0:
            item += len(self)
        if item >= 0:
            for i, value in enumerate(self):
                if i == item:
                    return value
        raise IndexError("slist index out of range")

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

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __len__(self):
        return self.length

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

    __rmul__ = __mul__

    def __setitem__(self, item, value):
        node = self.head
        while node is not None and item >= 0:
            node = node.next
            item -= 1
        if node is None:
            raise IndexError("list assignment index out of range")
        node.value = value

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.tail.next = Node(value)
        self.length += 1

    def clear(self):
        while self.head is not None:
            node, self.head = self.head, self.head.next
            del node
            self.length -= 1

    def copy(self):
        return self.__class__(self)

    def count(self, value):
        return sum(1 for v in self if v is value or v == value)

    def extend(self, values):
        node = self.tail
        for v in values:
            new_node = Node(v)
            if node is None:
                self.head = new_node
            else:
                node.next = new_node
            node = new_node
            self.length += 1

    def index(self, value, start=None, end=None):
        for i, node in enumerate(self._iter()):
            if start is not None and start > i:
                continue
            if end is not None and end < i:
                break
            if node.value is value or node.value == value:
                return i
        raise ValueError('%r is not in slist' % value)

    def insert(self, i, value):
        if i == 0 or self.head is None:
            self.head = Node(value, self.head)
        else:
            prev, node = None, self.head
            while node is not None:
                prev, node = node, node.next
                i -= 1
                if i == 0:
                    break
            prev.next = Node(value, prev.next)
        self.length += 1

    def pop(self, i=-1):
        if not self:
            raise IndexError('pop from empty list')
        if i < 0:
            i += self.length
        prev, node = None, self.head
        while node is not None:
            if i == 0:
                try:
                    if prev:
                        prev.next = node.next
                    else:
                        self.head = node.next
                    self.length -= 1
                    return node.value
                finally:
                    del node
            prev, node = node, node.next
            i -= 1
        raise IndexError('pop index out of range')

    def remove(self, value):
        prev, node = None, self.head
        while node is not None:
            if node.value == value:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                self.length -= 1
                del node
                return
            prev, node = node, node.next
        raise ValueError('slist.remove(x): x not in list')

    def reverse(self):
        prev, node = None, self.head
        while node is not None:
            prev, node.next, node = node, prev, node.next
        self.head = prev

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
            prev, node, is_sorted = None, self.head, True
            while node is not None:
                if prev is not None and not cmp_func(prev.value, node.value):
                    prev.value, node.value, is_sorted = node.value, prev.value, False
                prev, node = node, node.next
            if is_sorted:
                break

    def sort(self, reverse=False, key=None):
        self._bubble_sort(reverse=reverse, key=key)
