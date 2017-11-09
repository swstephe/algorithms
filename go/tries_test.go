package algorithms

import (
    "testing"
	"os"
	"strings"
)

var trie *TrieNode

func TestTrie01(t *testing.T) {
	word := "aardvark"
	keys := Word2Keys(word)
	words := trie.Find(keys)
	for _, word2 := range words {
		if strings.EqualFold(word, word2) {
			return
		}
	}
	t.Error(word, keys, words)
}

func TestTrie02(t *testing.T) {
	word := "waggs"
	keys := Word2Keys(word)
	words := trie.Find(keys)
	for _, word2 := range words {
		if strings.EqualFold(word, word2) {
			return
		}
	}
}

func TestMain(m *testing.M) {
	trie = NewNode()
	readWords(trie,"wordlist.txt")
	retCode := m.Run()
	os.Exit(retCode)
}