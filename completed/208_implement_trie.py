class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = []
        self._trie_element = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        for i in range(len(word) + 1):
            self._trie_element.append(word[:i])

        self._trie.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self._trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self._trie_element


trie = Trie()
trie.insert("apple")
assert trie.search("apple")   # return True
assert not trie.search("app")     # return False
assert trie.startsWith("app")   # return True
trie.insert("app")
assert trie.search("app")     # return True


trie = Trie()
trie.insert("a")
assert trie.search("a")
assert trie.startsWith("a")