class Node:
    def __init__(self, c):
        self.c = c
        self.n = {}
        self.n_words = 0
        self.is_leaf = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(c="^")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            return
        cur_node = self.root
        cur_node.n_words += 1
        for c in word:
            if c not in cur_node.n:
                cur_node.n[c] = Node(c=c)
            cur_node = cur_node.n[c]
            cur_node.n_words += 1
        cur_node.is_leaf = True
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return False
        cur_node = self.root
        for c in word:
            if c not in cur_node.n:
                return False
            cur_node = cur_node.n[c]
        return cur_node.is_leaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return False
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.n:
                return False
            cur_node = cur_node.n[c]
        return True

    def num_start_with(self, prefix: str) -> int:
        if len(prefix) == 0:
            return 0
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.n:
                return 0
            cur_node = cur_node.n[c]
        return cur_node.n_words


def print_trie_node(node: Node):
    part1 = "node: c = %c, n_words = %d, children = " % (node.c, node.n_words)
    part2 = ", ".join(node.n.keys())
    print(part1 + part2)


if __name__ == '__main__':
    trie = Trie()
    print(trie.num_start_with("app"))  # returns 0
    print(trie.startsWith("a"))   # returns false
    # print_trie_node(trie.root)
    trie.insert("apple")
    # print_trie_node(trie.root)
    print(trie.num_start_with("app"))  # returns 1
    trie.insert("apex")
    print(trie.num_start_with("app"))  # returns 1
    print(trie.search("apple"))   # returns true
    print(trie.search("app"))     # returns false
    print(trie.startsWith("app")) # returns true
    print(trie.startsWith("c"))  # returns false
    trie.insert("app")
    print(trie.search("app"))     # returns true
    print(trie.num_start_with("b"))  # returns 0
    print(trie.num_start_with("a"))  # returns 3
    print(trie.num_start_with("ap"))  # returns 3
    print(trie.num_start_with("app"))  # returns 2
    print(trie.num_start_with("appy"))  # returns 0
    print_trie_node(trie.root)
    print_trie_node(trie.root.n['a'])
    print_trie_node(trie.root.n['a'].n['p'])
    print_trie_node(trie.root.n['a'].n['p'].n['p'])
    print_trie_node(trie.root.n['a'].n['p'].n['p'].n['l'])
    print_trie_node(trie.root.n['a'].n['p'].n['p'].n['l'].n['e'])
