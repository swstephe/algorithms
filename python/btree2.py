# -*- coding: utf8 -*-
M = 4


class Entry(object):
    def __init__(self, key, val, _next):
        self.key = key
        self.val = val
        self._next = _next

    def __iter__(self):
        return self

    def __next__(self):
        if self._next is None:
            raise StopIteration
        return self._next


class Node(object):
    def __init__(self, k):
        self.m = k
        self.children = [None] * M


class BTree(object):
    def __init__(self):
        self.root = Node(0)
        self.height = 0
        self.size = 0

    @property
    def is_empty(self):
        return self.size == 0

    def get(self, key):
        return self.search(self.root, key, self.height)

    def search(self, x, key, ht):
        children = x.children
        if ht == 0:
            for j in range(x.m):
                if key == children[j].key:
                    return children[j].val
        else:
            for j in range(x.m):
                if j + 1 == x.m or key < children[j + 1].key:
                    return self.search(children[j].next, key, ht - 1)

    def put(self, key, val):
        u = self.insert(self.root, key, val, self.height)
        self.size += 1
        if u is None:
            return

        t = Node(2)
        t.children[0] = Entry(self.root.children[0].key, None, self.root)
        t.children[1] = Entry(u.children[0].key, None, u)
        self.root = t
        self.height += 1

    def insert(self, h, key, val, ht):
        j = 0
        t = Entry(key, val, None)
        if ht == 0:
            for j in range(h.m):
                if key < h.children[j].key:
                    break
        else:
            j = 0
            while j < h.m:
                if j + 1 == h.m or key < h.children[j + 1].key:
                    u = self.insert(h.children[j].next, key, val, ht - 1)
                    j += 1
                    if u is None:
                        return None
                    t.key = u.children[0].key
                    t.next = u
                    break
                j += 1
        for i in range(h.m, j, -1):
            h.children[i] = h.children[i - 1]
        h.children[j] = t
        h.m += 1
        if h.m < M:
            return None
        else:
            return self.split(h)

    def split(self, h):
        t = Node(M // 2)
        h.m = M // 2
        for j in range(M // 2):
            t.children[j] = h.children[M // 2 + j]
        return t

    def __str__(self):
        def to_string(h, ht, indent):
            children = h.children
            if ht == 0:
                for j in range(h.m):
                    yield indent + children[j].key + ' ' + children[j].val + '\n'
            else:
                for j in range(h.m):
                    if j > 0:
                        yield indent + '(' + children[j].key + ')\n'
                    for text in to_string(children[j].next, ht - 1, indent + '    '):
                        yield text

        return ''.join(to_string(self.root, self.height, '')) + '\n'


st = BTree()

st.put("www.cs.princeton.edu", "128.112.136.12")
st.put("www.cs.princeton.edu", "128.112.136.11")
st.put("www.princeton.edu", "128.112.128.15")
st.put("www.yale.edu", "130.132.143.21")
st.put("www.simpsons.com", "209.052.165.60")
st.put("www.apple.com", "17.112.152.32")
st.put("www.amazon.com", "207.171.182.16")
st.put("www.ebay.com", "66.135.192.87")
st.put("www.cnn.com", "64.236.16.20")
st.put("www.google.com", "216.239.41.99")
st.put("www.nytimes.com", "199.239.136.200")
st.put("www.microsoft.com", "207.126.99.140")
st.put("www.dell.com", "143.166.224.230")
st.put("www.slashdot.org", "66.35.250.151")
st.put("www.espn.com", "199.181.135.201")
st.put("www.weather.com", "63.111.66.11")
st.put("www.yahoo.com", "216.109.118.65")

print("cs.princeton.edu: ", st.get("www.cs.princeton.edu"))
print("hardvardsucks.com:", st.get("www.harvardsucks.com"))
print("simpsons.com:     ", st.get("www.simpsons.com"))
print("apple.com:        ", st.get("www.apple.com"))
print("ebay.com:         ", st.get("www.ebay.com"))
print("dell.com:         ", st.get("www.dell.com"))
print()

print("size:   ", st.size)
print("height: ", st.height)
print(st)
print()

