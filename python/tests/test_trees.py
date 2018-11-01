# -*- coding: utf-8 -*-
import trees
import random

MAX_INT = 10
COUNT = 10
REPEAT = 40


def test_binary():
    data = set()
    tree = trees.Tree()
    for c in range(1, COUNT + 1):
        for i in range(c):
            value = random.randint(-MAX_INT, MAX_INT)
            tree.insert(value)
            data.add(value)
            assert list(tree) == sorted(list(data))
        for value in list(data):
            tree.delete(value)
            data.remove(value)
            assert list(tree) == sorted(list(data))
        assert list(tree) == []


def test_binary1():
    tree = trees.Tree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    assert list(tree) == [20, 30, 40, 50, 60, 70, 80]
    tree.delete(20)
    assert list(tree) == [30, 40, 50, 60, 70, 80]
    tree.delete(30)
    assert list(tree) == [40, 50, 60, 70, 80]
    tree.delete(50)
    assert list(tree) == [40, 60, 70, 80]
