# -*- coding: utf8 -*-
import os
import string
from tries2 import Trie

CWD = os.path.dirname(os.path.realpath(__file__))


def test_simple():
    trie = Trie(string.ascii_lowercase)
    assert list(trie) == []
    assert len(trie) == 0
    assert str(trie) == '{}/None'
    trie.insert('abc', 123)
    assert list(trie) == [('abc', 123)]
    assert len(trie) == 1
    assert str(trie) == '{a: {b: {c: {}/123}/None}/None}/None'


def test_lines():
    trie = Trie('s')
    trie.insert('s', True)
    trie.insert('ss', True)
    trie.insert('sss', True)
    trie.insert('ssss', True)
    trie.insert('sssss', True)
    assert trie.find('s') is True
    assert trie.find('a') is None
    assert trie.find('') is None
    assert trie.find('ss') is True
    assert trie.find('sss') is True
    assert trie.find('ssss') is True
    assert trie.find('sssss') is True
    assert trie.find('ssssss') is None
    assert trie.find_prefix('s') == {True}
    assert 'sss' in trie
    assert 'sssssssss' not in trie


def test_words():
    keys = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    keys = dict((ch, k) for k, v in keys.items() for ch in v)
    trie = Trie(string.digits)

    # load with 1000 most common words
    with open(os.path.join(CWD, 'wordlist.txt')) as f:
        for i, line in enumerate(f):
            word = line.strip().lower()
            digits = ''.join(keys[ch] for ch in word if ch in keys)
            if not digits:
                continue
            words = trie.find(digits)
            if words is None:
                words = {word}
            else:
                words.add(word)
            trie.insert(digits, words)

    assert trie.find('2') == {'a'}
    assert trie.find('96864') == {'young'}
    assert trie.find_prefix('968') == {'would', 'young', 'your', 'yourself'}
