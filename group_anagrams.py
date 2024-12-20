# first iteration
# O(n * m log(m)) time | O(n * m) space
# where n is the number of strings in the array
# where m is the maximum number of characters in a string
def groupAnagrams(words):
    # Write your code here.
    _dict = {}
    sortedWords = {word: "".join(sorted(word)) for word in words}
    for key, value in sortedWords.items():
        if value in _dict:
            _dict[value].append(key)
        else:
            _dict[value] = [key]
    return [value for value in _dict.values()]


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
