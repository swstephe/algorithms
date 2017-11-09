# -*- coding: utf-8 -*-
from itertools import izip_longest


class BinaryNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def count(self):
        return (
            (self.left.count if self.left else 0)
            + (self.right.count if self.right else 0)
            + 1
        )

    @property
    def height(self):
        return max(
            self.left.height if self.left else 0,
            self.right.height if self.right else 0
        ) + 1

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self

    def find(self, value):
        if value == self.value:
            return self
        child = self.left if value < self.value else self.right
        return None if child is None else child.find(value)

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left and self.right:
                node = self.right.find_min()
                self.value = node.value
                self.right = self.right.delete(self.value)
            elif self.left:
                return self.left
            elif self.right:
                return self.right
            else:
                return None
        return self

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryNode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinaryNode(value)
        return self

    def in_order(self):
        if self.left:
            for left in self.left.in_order():
                yield left
        yield self.value
        if self.right:
            for right in self.right.in_order():
                yield right

    def leaves(self):
        if self.left or self.right:
            if self.left:
                for leaf in self.left.leaves():
                    yield leaf
            if self.right:
                for leaf in self.right.leaves():
                    yield leaf
        else:
            yield self.value

    def paths(self):
        if self.left or self.right:
            if self.left:
                for path in self.left.paths():
                    yield (self.value,) + path
            if self.right:
                for path in self.right.paths():
                    yield (self.value,) + path
        else:
            yield (self.value,)

    def __str__(self):
        if self.left or self.right:
            return '({} {} {})'.format(
                self.value,
                self.left or 'nil',
                self.right or 'nil'
            )
        return str(self.value)


class BinaryTree(object):
    def __init__(self):
        self.root = None

    @property
    def count(self):
        if self.root:
            return self.root.count
        return 0

    @property
    def height(self):
        if self.root:
            return self.root.height
        return 0

    def find_min(self):
        if self.root:
            return self.root.find_min()

    def find_max(self):
        if self.root:
            return self.root.find_max()

    def find(self, value):
        if self.root:
            return self.root.find(value)

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)
        else:
            self.root = None
        return self.root

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = BinaryNode(value)
        return self.root

    def in_order(self):
        if self.root:
            return list(self.root.in_order())
        return []

    def leaves(self):
        if self.root:
            return tuple(self.root.leaves())
        return tuple()

    def paths(self):
        if self.root:
            return tuple(self.root.paths())
        return tuple()

    def __str__(self):
        if self.root:
            return str(self.root)
        return '<empty>'
