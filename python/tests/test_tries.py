# -*- coding: utf8 -*-
import os
from tries import Trie

CWD = os.path.dirname(os.path.realpath(__file__))


def test_simple():
    trie = Trie()
    trie.insert('abc', 123)
    print('trie', trie)
    print(list(trie))


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
    trie = Trie()

    # load with 1000 most common words
    with open(os.path.join(CWD, 'wordlist.txt')) as f:
        for i, word in enumerate(f):
            word = word.strip()
            digits = ''.join(keys[ch] for ch in word if ch in keys)
            if not digits:
                continue
            words = trie.find(digits)
            if words:
                words.add(word)
            else:
                words = {word}
            trie.insert(digits, words)

    assert trie.find('2') == {'a'}
    assert trie.find('96864') == {'young'}
    assert trie.find_prefix('968') == {'would', 'young', 'your', 'yourself'}


def test_lines():
    trie = Trie()
    lines = (
        'add s',
        'add ss',
        'add sss',
        'add ssss',
        'add sssss',
        'find s',
        'find ss',
        'find sss',
        'find ssss',
        'find sssss',
        'find ssssss',
    )
    for line in lines:
        line = line.strip().split(None, 1)
        if line[0] == 'add':
            trie.insert(line[1], True)
        elif line[0] == 'find':
            print(trie.find(line[1]))
