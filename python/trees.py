# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __len__(self):
        return sum(1 for _ in self)

    def __reversed__(self):
        if self.right:
            yield from reversed(self.right)
        yield self.value
        if self.left:
            yield from reversed(self.left)

    @property
    def height(self):
        return max(
            self.left.height if self.left else 0,
            self.right.height if self.right else 0
        ) + 1

    def find_min(self):
        return self.left.find_min() if self.left else self

    def find_max(self):
        return self.right.find_max() if self.right else self

    def find(self, value):
        if value < self.value:
            if self.left:
                return self.left.find(value)
        elif value > self.value:
            if self.right:
                return self.right.find(value)
        else:
            return self

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left and self.right:
                child = self.right.find_min()
                self.value = child.value
                self.right = self.right.delete(child.value)
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
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def leaves(self):
        if self.left or self.right:
            if self.left:
                yield from self.left.leaves()
            if self.right:
                yield from self.right.leaves()
        else:
            yield self.value

    def paths(self):
        def mkpath(path):
            yield self.value
            yield from path
        if self.left or self.right:
            if self.left:
                for path in self.left.paths():
                    yield tuple(mkpath(path))
            if self.right:
                for path in self.right.paths():
                    yield tuple(mkpath(path))
        else:
            yield tuple((self.value,))

    def __str__(self):
        if self.left or self.right:
            return '({} {} {})'.format(
                self.value,
                self.left or 'nil',
                self.right or 'nil'
            )
        return str(self.value)


class Tree(object):
    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root:
            yield from self.root

    def __len__(self):
        return len(self.root) if self.root else 0

    def __reversed__(self):
        if self.root:
            yield from reversed(self.root)

    @property
    def height(self):
        return self.root.height if self.root else 0

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
            self.root = Node(value)
        return self.root

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
