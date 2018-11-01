# -*- coding: utf8 -*-
from slinked import List

DATA = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def test_init():
    slist = List(*DATA)
    assert list(slist) == list(DATA)
    assert str(slist) == str(list(DATA))
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == len(DATA)
    assert slist[2] == DATA[2]
    assert slist[-1] == DATA[-1]


def test_append():
    slist = List()
    for value in DATA:
        slist.append(value)
    assert list(slist) == list(DATA)
    assert str(slist) == str(list(DATA))
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == len(DATA)
    assert slist[2] == DATA[2]
    assert slist[-1] == DATA[-1]


def test_pop():
    slist = List(*DATA)
    expect = list(DATA)
    for i in range(len(DATA)):
        assert slist.pop() == expect.pop()
    slist = List(*DATA)
    for i in range(len(DATA)):
        assert slist.pop(0) == DATA[i]
    slist = List(*DATA)
    for i in range(len(DATA) - 1):
        assert slist.pop(1) == DATA[i + 1]
    assert list(slist) == [DATA[0]]

def test_remove():
    slist = List(*DATA)
    slist.remove(DATA[2])
    expect = list(DATA)
    expect.remove(DATA[2])
    assert list(slist) == list(expect)
    assert str(slist) == str(list(expect))
    assert slist.head.value == expect[0]
    assert slist.tail.value == expect[-1]
    assert len(slist) == len(expect)
    assert slist[2] == expect[2]
    assert slist[-2] == expect[-2]


def test_reverse():
    slist = List(*DATA)
    slist.reverse()
    assert list(slist) == list(reversed(DATA))
    assert str(slist) == str(list(reversed(DATA)))
    assert slist.head.value == DATA[-1]
    assert slist.tail.value == DATA[0]
    assert slist[2] == DATA[-3]
    assert slist[-3] == DATA[2]
