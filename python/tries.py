# -*- coding: utf8 -*-

KEYS = dict((ch, str(i + 2)) for i, k in enumerate((
    'abc',      # 2
    'def',      # 3
    'ghi',      # 4
    'jkl',      # 5
    'mno',      # 6
    'pqrs',     # 7
    'tuv',      # 8
    'wxyz',     # 9
)) for ch in k)

print('KEYS', KEYS)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.words = set()

    def add(self, word):
        keys_word = ''.join(ch for ch in word if ch in KEYS)
        if not keys_word:
            return
        self.add_child(word, keys_word)

    def add_child(self, word, suffix):
        ch = KEYS[suffix[0]]
        if ch not in self.children:
            self.children[ch] = TrieNode()
        if suffix[1:]:
            self.children[ch].add_child(word, suffix[1:])
        if len(self.words) < 5:
            self.words.add(word)

    def dump(self):
        for ch, child in sorted(self.children.items()):
            yield ch, self.words
            for suffix, words in child.dump():
                yield ch + suffix, words

    def find(self, keys):
        if keys and keys[0] in self.children:
            return self.children[keys[0]].find(keys[1:])
        return self.words


trie = TrieNode()


with open('wordlist.txt') as f:
    for i, word in enumerate(f):
        # if i >= 100:
        #     break
        word = word.strip()
        print(word)
        trie.add(word)


# for thing in sorted(trie.dump()):
#     print('-', thing)

print(trie.find('22738275'))
print(trie.find('9244'))


# trie = Node()
# LINES = (
#     'add s',
#     'add ss',
#     'add sss',
#     'add ssss',
#     'add sssss',
#     'find s',
#     'find ss',
#     'find sss',
#     'find ssss',
#     'find sssss',
#     'find ssssss',
# )
# n = len(LINES)
# for i in range(n):
#     line = LINES[i].strip().split(None, 1)
#     if line[0] == 'add':
#         node = trie
#         for ch in line[1]:
#             node = node.add(ch)
#         node.end = True
#     elif line[0] == 'find':
#         print('-'*20)
#         print(trie.find(line[1]))
