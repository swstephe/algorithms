# -*- coding: utf8 -*-
import pytest
from dlinked import List

DATA = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def test_init():
    dlist = List(DATA)
    assert list(dlist) == list(DATA)
    assert str(dlist) == str(list(DATA))
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == len(DATA)
    assert dlist[2] == DATA[2]
    assert dlist[-1] == DATA[-1]
    assert bool(dlist) is True


def test_add():
    dlist = List(DATA)
    dlist += List(DATA)
    assert list(dlist) == list(DATA) + list(DATA)
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == 2*len(DATA)
    assert dlist[len(DATA) + 2] == DATA[2]
    assert dlist[-len(DATA) - 2] == DATA[-2]
    assert bool(dlist) is True
    dlist = List(DATA) + List(DATA)
    assert list(dlist) == list(DATA) + list(DATA)
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == 2*len(DATA)
    assert dlist[len(DATA) + 2] == DATA[2]
    assert dlist[-len(DATA) - 2] == DATA[-2]
    assert bool(dlist) is True
    dlist = List(DATA) + DATA
    assert list(dlist) == list(DATA) + list(DATA)
    assert dlist.head.value == DATA[0]
    assert dlist.tail.value == DATA[-1]
    assert len(dlist) == 2*len(DATA)
    assert dlist[len(DATA) + 2] == DATA[2]
    assert dlist[-len(DATA) - 2] == DATA[-2]
    assert bool(dlist) is True


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
    assert bool(dlist) is True


def test_clear():
    dlist = List(DATA)
    dlist.clear()
    assert dlist.head is None
    assert dlist.tail is None
    assert len(dlist) == 0
    assert bool(dlist) is False


def test_count():
    dlist = List(DATA)
    assert dlist.count('Mon') == 1
    assert dlist.count('Foo') == 0


def test_cmp():
    assert List((1, 2, 3)) == (1, 2, 3)
    assert List((2, 3, 4)) > List((1, 2, 3))
    assert List((2, 3, 4)) >= List((1, 2, 3))
    assert List((1, 2, 3)) < List((3, 4, 5))
    assert List((1, 2, 3)) <= List((3, 4, 5))
    assert List((1, 2)) < List((1, 2, 3))
    assert List((1, 2, 3)) > List((1, 2))
    assert List() < List((1, 2))
    assert sorted(List((3, 1, 2))) == List((1, 2, 3))


def test_extend():
    n = len(DATA)
    dlist = List(DATA)
    dlist.extend(DATA)
    dlist.extend(DATA)
    assert len(dlist) == 3*n
    assert dlist[0] == DATA[0]
    assert dlist[-1] == DATA[-1]
    for i in range(n):
        assert dlist[i] == DATA[i]
        assert dlist[i + n] == DATA[i]
        assert dlist[i + 2*n] == DATA[i]
    assert dlist.count('Mon') == 3
    assert dlist.count('Foo') == 0


def test_index():
    dlist = List(DATA)
    for i, day in enumerate(DATA):
        assert dlist.index(day) == i
    with pytest.raises(ValueError):
        dlist.index('Foo')


def test_insert():
    data = []
    dlist = List()
    for i, word in enumerate(('one', 'two', 'three')):
        dlist.insert(0, word)
        data.insert(0, word)
        assert len(dlist) == i + 1
        assert dlist[0] == word
        assert dlist[-1] == 'one'
        assert list(dlist) == data
    dlist.insert(1, 'four')
    data.insert(1, 'four')
    assert list(dlist) == data
    assert tuple(dlist) == ('three', 'four', 'two', 'one')
    dlist.insert(12, 'twelve')
    data.insert(12, 'twelve')
    assert list(dlist) == list(data)
    assert tuple(dlist) == ('three', 'four', 'two', 'one', 'twelve')


def test_pop():
    dlist = List(DATA)
    expect = list(DATA)
    for i in range(len(DATA)):
        assert dlist.pop() == expect.pop()
    dlist = List(DATA)
    for i in range(len(DATA)):
        assert dlist.pop(0) == DATA[i]
    dlist = List(DATA)
    for i in range(len(DATA) - 1):
        assert dlist.pop(1) == DATA[i + 1]
    assert list(dlist) == [DATA[0]]


def test_remove():
    dlist = List(DATA)
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
    dlist = List(DATA)
    dlist.reverse()
    assert list(dlist) == list(reversed(DATA))
    assert str(dlist) == str(list(reversed(DATA)))
    assert dlist.head.value == DATA[-1]
    assert dlist.tail.value == DATA[0]
    assert dlist[2] == DATA[-3]
    assert dlist[-3] == DATA[2]

def test_sort():
    dlist = List(DATA)
    dlist.sort()
    assert list(dlist) == list(sorted(DATA))
    dlist.sort(reverse=True)
    assert list(dlist) == list(sorted(DATA, reverse=True))

    def key(v):
        return v[::-1]

    dlist.sort(key=key)
    assert list(dlist) == list(sorted(DATA, key=key))
