class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n ^ 2) time | O(n^2) space
    # where n is the length of the string
    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for idx in range(len(string)):
            self.createSuffixTrieFromIndex(idx, string)

    def createSuffixTrieFromIndex(self, idx, string):
        currentNode = self.root
        for i in range(idx, len(string)):
            letter = string[i]
            if letter not in currentNode:
                currentNode[letter] = {}
            currentNode = currentNode[letter]
        currentNode[self.endSymbol] = True

    # O(m) time | O(1) space
    # where m is length of the string that we are searching for
    def contains(self, string):
        # Write your code here.
        currentNode = self.root
        for letter in string:
            if letter not in currentNode:
                return False
            currentNode = currentNode[letter]
        return self.endSymbol in currentNode


string = 'babc'
trie = SuffixTrie(string)
