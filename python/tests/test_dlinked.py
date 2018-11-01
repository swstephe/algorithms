# -*- coding: utf8 -*-
from dlinked import List

DATA = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def test_init():
    dlist = List(*DATA)
    assert list(dlist) == list(DATA)
    assert str(dlist) == str(list(DATA))
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == len(DATA)
    assert dlist[2] == DATA[2]
    assert dlist[-1] == DATA[-1]


def test_append():
    dlist = List()
    for value in DATA:
        dlist.append(value)
    assert list(dlist) == list(DATA)
    assert str(dlist) == str(list(DATA))
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == len(DATA)
    assert dlist[2] == DATA[2]
    assert dlist[-1] == DATA[-1]


def test_pop():
    dlist = List(*DATA)
    for i in range(len(DATA)):
        assert dlist.pop() == DATA[-(i + 1)]
    dlist = List(*DATA)
    for i in range(len(DATA)):
        assert dlist.pop(0) == DATA[i]
    dlist = List(*DATA)
    for i in range(len(DATA) - 1):
        assert dlist.pop(1) == DATA[i + 1]
    assert list(dlist) == [DATA[0]]


def test_remove():
    dlist = List(*DATA)
    dlist.remove(DATA[2])
    expect = list(DATA)
    expect.remove(DATA[2])
    assert list(dlist) == list(expect)
    assert str(dlist) == str(list(expect))
    assert dlist.head.value == expect[0]
    assert dlist.tail.value == expect[-1]
    assert len(dlist) == len(expect)
    assert dlist[2] == expect[2]
    assert dlist[-2] == expect[-2]


def test_reverse():
    dlist = List(*DATA)
    dlist.reverse()
    assert list(dlist) == list(reversed(DATA))
    assert str(dlist) == str(list(reversed(DATA)))
    assert dlist.head.value == DATA[-1]
    assert dlist.tail.value == DATA[0]
    assert dlist[2] == DATA[-3]
    assert dlist[-3] == DATA[2]
