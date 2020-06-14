# -*- coding: utf8 -*-
import pytest
from slinked import List

DATA = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def test_init():
    slist = List(DATA)
    assert list(slist) == list(DATA)
    assert str(slist) == str(list(DATA))
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == len(DATA)
    assert slist[2] == DATA[2]
    assert slist[-1] == DATA[-1]
    assert bool(slist) is True


def test_add():
    slist = List(DATA)
    slist += List(DATA)
    assert list(slist) == list(DATA) + list(DATA)
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == 2*len(DATA)
    assert slist[len(DATA) + 2] == DATA[2]
    assert slist[-len(DATA) - 2] == DATA[-2]
    assert bool(slist) is True
    slist = List(DATA) + List(DATA)
    assert list(slist) == list(DATA) + list(DATA)
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == 2*len(DATA)
    assert slist[len(DATA) + 2] == DATA[2]
    assert slist[-len(DATA) - 2] == DATA[-2]
    assert bool(slist) is True
    slist = List(DATA) + DATA
    assert list(slist) == list(DATA) + list(DATA)
    assert slist.head.value == DATA[0]
    assert slist.tail.value == DATA[-1]
    assert len(slist) == 2*len(DATA)
    assert slist[len(DATA) + 2] == DATA[2]
    assert slist[-len(DATA) - 2] == DATA[-2]
    assert bool(slist) is True


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
    assert bool(slist) is True


def test_clear():
    slist = List(DATA)
    slist.clear()
    assert slist.head is None
    assert slist.tail is None
    assert len(slist) == 0
    assert bool(slist) is False


def test_count():
    slist = List(DATA)
    assert slist.count('Mon') == 1
    assert slist.count('Foo') == 0


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
    slist = List(DATA)
    slist.extend(DATA)
    slist.extend(DATA)
    assert len(slist) == 3*n
    assert slist[0] == DATA[0]
    assert slist[-1] == DATA[-1]
    for i in range(n):
        assert slist[i] == DATA[i]
        assert slist[i + n] == DATA[i]
        assert slist[i + 2*n] == DATA[i]
    assert slist.count('Mon') == 3
    assert slist.count('Foo') == 0


def test_index():
    slist = List(DATA)
    for i, day in enumerate(DATA):
        assert slist.index(day) == i
    with pytest.raises(ValueError):
        slist.index('Foo')


def test_insert():
    data = []
    slist = List()
    for i, word in enumerate(('one', 'two', 'three')):
        slist.insert(0, word)
        data.insert(0, word)
        assert len(slist) == i + 1
        assert slist[0] == word
        assert slist[-1] == 'one'
        assert list(slist) == data
    slist.insert(1, 'four')
    data.insert(1, 'four')
    assert list(slist) == data
    assert tuple(slist) == ('three', 'four', 'two', 'one')
    slist.insert(12, 'twelve')
    data.insert(12, 'twelve')
    assert list(slist) == list(data)
    assert tuple(slist) == ('three', 'four', 'two', 'one', 'twelve')


def test_pop():
    slist = List(DATA)
    expect = list(DATA)
    for i in range(len(DATA)):
        assert slist.pop() == expect.pop()
    slist = List(DATA)
    for i in range(len(DATA)):
        assert slist.pop(0) == DATA[i]
    slist = List(DATA)
    for i in range(len(DATA) - 1):
        assert slist.pop(1) == DATA[i + 1]
    assert list(slist) == [DATA[0]]


def test_remove():
    slist = List(DATA)
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
    slist = List(DATA)
    slist.reverse()
    assert list(slist) == list(reversed(DATA))
    assert str(slist) == str(list(reversed(DATA)))
    assert slist.head.value == DATA[-1]
    assert slist.tail.value == DATA[0]
    assert slist[2] == DATA[-3]
    assert slist[-3] == DATA[2]


def test_sort():
    slist = List(DATA)
    slist.sort()
    assert list(slist) == list(sorted(DATA))
    slist.sort(reverse=True)
    assert list(slist) == list(sorted(DATA, reverse=True))

    def key(v):
        return v[::-1]

    slist.sort(key=key)
    assert list(slist) == list(sorted(DATA, key=key))
