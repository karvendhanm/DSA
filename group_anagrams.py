# first iteration
# O(n * m log(m)) time | O(n * m) space
# where n is the number of strings in the array
# where m is the length of the longest string
def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
