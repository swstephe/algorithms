# -*- coding: utf-8 -*-
import btrees
import random

MAX_INT = 10
COUNT = 10
REPEAT = 40


def test_binary():
    data = set()
    tree = btrees.BTree(3)
    for c in range(1, COUNT + 1):
        for i in range(c):
            value = random.randint(-MAX_INT, MAX_INT)
            tree.insert(value)
            print('+', value, tree.in_order())
            data.add(value)
            assert tree.in_order() == sorted(list(data))
        print('-'*20)
        print('tree', tree)
        print('in_order', tree.in_order())
        print('height', tree.height)
        print('count', tree.count)
        # print('paths', tree.paths())
        # print('leaves', tree.leaves())
        for value in list(data):
            tree.delete(value)
            # print '-', value, tree.in_order()
            data.remove(value)
            assert tree.in_order() == sorted(list(data))
        assert tree.in_order() == []


def test_binary1():
    tree = btrees.BTree()
    for key in (50, 30, 20, 40, 70, 60, 80):
        print('+', key)
        tree.put(key, None)
        print(tree)
    assert tree.in_order() == [20, 30, 40, 50, 60, 70, 80]
    tree.delete(20)
    assert tree.in_order() == [30, 40, 50, 60, 70, 80]
    tree.delete(30)
    assert tree.in_order() == [40, 50, 60, 70, 80]
    tree.delete(50)
    assert tree.in_order() == [40, 60, 70, 80]


BTREE3_DATA = (
    ("www.cs.princeton.edu", "128.112.136.12"),
    ("www.cs.princeton.edu", "128.112.136.11"),
    ("www.princeton.edu",    "128.112.128.15"),
    ("www.yale.edu",         "130.132.143.21"),
    ("www.simpsons.com",     "209.052.165.60"),
    ("www.apple.com",        "17.112.152.32"),
    ("www.amazon.com",       "207.171.182.16"),
    ("www.ebay.com",         "66.135.192.87"),
    ("www.cnn.com",          "64.236.16.20"),
    ("www.google.com",       "216.239.41.99"),
    ("www.nytimes.com",      "199.239.136.200"),
    ("www.microsoft.com",    "207.126.99.140"),
    ("www.dell.com",         "143.166.224.230"),
    ("www.slashdot.org",     "66.35.250.151"),
    ("www.espn.com",         "199.181.135.201"),
    ("www.weather.com",      "63.111.66.11"),
    ("www.yahoo.com",        "216.109.118.65")
)


def test_btree3():
    st = btrees.BTree()
    check = {}
    for key, value in BTREE3_DATA:
        st.put(key, value)
        check[key] = value
        print('-'*20)
        print(st)
    for key, value in check.iteritems():
        assert st.get(key) == value
