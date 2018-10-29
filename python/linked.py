# -*- coding: utf8 -*-


class SLinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SLinkedListIterator(object):
    def __init__(self, llist):
        self.node = llist.head

    def __next__(self):
        if self.node is None:
            raise StopIteration
        node = self.node
        self.node = self.node.next
        return node.value


class SLinkedList(object):
    Node = SLinkedListNode
    Iter = SLinkedListIterator

    def __init__(self, *args):
        self.head = None
        self.extend(args)

    def __getitem__(self, item):
        if self.head is None:
            raise ValueError("list is empty")
        if item < 0:
            item += len(self)
        return self.head.get(item)

    def __iter__(self):
        return self.Iter(self)

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        return '[{}]'.format(', '.join(repr(value) for value in self))

    def append(self, value):
        if self.head is None:
            self.head = self.Node(value)
        else:
            self.tail.next = self.Node(value)

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
        node = self.tail
        for value in iterable:
            if node is None:
                node = self.head = self.Node(value)
            else:
                node = node.next = self.Node(value)

    def index(self, value, start=None, end=None):
        for i, node in enumerate(self):
            if node.value == value:
                return i

    def insert(self, i, value):
        node = self.head
        while node.next and i > 0:
            node = node.next
            i -= 1
        node.next = self.Node(value, node.next)

    def pop(self, i=None):
        if i is None:
            i = len(self) - 1
        prev, node = None, self.head
        while node is not None:
            prev, node = node, node.next
            if i == 0:
                prev.next = node.next
                return node
            i -= 1

    def prepend(self, value):
        self.head = self.Node(value, self.head)

    def remove(self, value):
        prev, node = None, self.head
        while node is not None:
            prev, node = node, node.next
            if node.value == value:
                prev.next = node.next
                del node
                break

    @property
    def tail(self):
        if self.head is None:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node


slist = SLinkedList()
slist.append('Monday')
slist.append('Tuesday')
slist.append('Wednesday')
slist.append('Thursday')
slist.append('Friday')
print('slist', slist)
slist.remove('Wednesday')
print('slist', slist)
print('slist.tail', slist.tail.value)
print('len(slist)', len(slist))
print('slist[2]', slist[2].data)
print('slist[-1]', slist[-1].data)
print('tuple(slist)', tuple(slist))
