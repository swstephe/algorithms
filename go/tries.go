package algorithms

import (
	"bufio"
	"fmt"
	"os"
	"io"
	"strings"
)

var KEYS = map[string]string{
	"a": "2", "b": "2", "c": "2",
	"d": "3", "e": "3", "f": "3",
	"g": "4", "h": "4", "i": "4",
	"j": "5", "k": "5", "l": "5",
	"m": "6", "n": "6", "o": "6",
	"p": "7", "q": "7", "r": "7", "s": "7",
	"t": "8", "u": "8", "v": "8",
	"w": "9", "x": "9", "y": "9", "z": "9",
}

func Word2Keys(word string) string {
	var keys []string
	for _, ch := range word {
		key, ok := KEYS[string(ch)]
		if ok {
			keys = append(keys, key)
		}
	}
	return strings.Join(keys, "")
}

type TrieNode struct {
	children map[string]*TrieNode
	words []string
}

func NewNode() *TrieNode {
	node := new(TrieNode)
	node.children = make(map[string]*TrieNode)
	return node
}

func (node *TrieNode) Add(word string) {
	keys := Word2Keys(word)
	if len(keys) > 0 {
		node.AddChild(word, Word2Keys(word))
	}
}

func (node *TrieNode) AddChild(word string, keys string) {
	ch := string(keys[0])
	child, ok := node.children[ch]
	if ! ok {
		child = NewNode()
		node.children[ch] = child
	}
	suffix := keys[1:]
	if len(suffix) > 0 {
		child.AddChild(word, suffix)
	}
	if len(node.words) < 5 {
		node.words = append(node.words, word)
	}
}

//func (node *TrieNode) Dump() {
//	for ch, child := range node.children {
//		c <- Result{ch, node.words }
//		go child.Dump(c)
//		for res := range c {
//			c <- Result{ch + result.keys, result.words}
//		}
//	}
//}

func (node *TrieNode) Find(keys string) []string {
	fmt.Println("Find", keys, node.words)
	if len(keys) <= 1 {
		return node.words
	}
	child, ok := node.children[string(keys[0])]
	if ok {
		return child.Find(keys[1:])
	}
	return nil
}

func readWords(trie *TrieNode, fn string) (err error) {
	file, err := os.Open(fn)
	if err != nil {
		fmt.Println("couldn't open file", err)
		return err
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	var line string
	for {
		line, err = reader.ReadString('\n')
		if err != nil {
			break
		}
		line = strings.TrimSpace(line)
		line = strings.ToLower(line)
		fmt.Println("-", line)
		trie.Add(line)
	}
	if err != io.EOF {
		fmt.Println("read error", err)
		return err
	}
	return
}
