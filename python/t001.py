# -*- coding: utf8 -*-


class Node(object):
    def __init__(self):
        self.chars = {}
        self.end = False

    def add(self, ch):
        if ch not in self.chars:
            self.chars[ch] = Node()
        return self.chars[ch]

    def find(self, text):
        print('find', text, self.chars, self.end)
        if text:
            if text[0] in self.chars:
                return self.chars[text[0]].find(text[1:])
            return 0
        return int(self.end) + sum(
            node.find(None)
            for ch, node in self.chars.items()
        )


trie = Node()
LINES = (
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
n = len(LINES)
for i in range(n):
    line = LINES[i].strip().split(None, 1)
    if line[0] == 'add':
        node = trie
        for ch in line[1]:
            node = node.add(ch)
        node.end = True
    elif line[0] == 'find':
        print('-'*20)
        print(trie.find(line[1]))
