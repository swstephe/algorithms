# -*- coding: utf-8 -*-
import trees
import random

MAX_INT = 10
COUNT = 10
REPEAT = 40


def test_binary():
    data = set()
    tree = trees.BinaryTree()
    for c in range(1, COUNT + 1):
        for i in range(c):
            value = random.randint(-MAX_INT, MAX_INT)
            tree.insert(value)
            # print '+', value, tree.in_order()
            data.add(value)
            assert tree.in_order() == sorted(list(data))
        print('-'*20)
        print('tree', tree)
        print('in_order', tree.in_order())
        print('height', tree.height)
        print('count', tree.count)
        print('paths', tree.paths())
        print('leaves', tree.leaves())
        for value in list(data):
            tree.delete(value)
            # print '-', value, tree.in_order()
            data.remove(value)
            assert tree.in_order() == sorted(list(data))
        assert tree.in_order() == []


def test_binary1():
    tree = trees.BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    assert tree.in_order() == [20, 30, 40, 50, 60, 70, 80]
    tree.delete(20)
    assert tree.in_order() == [30, 40, 50, 60, 70, 80]
    tree.delete(30)
    assert tree.in_order() == [40, 50, 60, 70, 80]
    tree.delete(50)
    assert tree.in_order() == [40, 60, 70, 80]
