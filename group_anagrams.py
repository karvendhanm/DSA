# first iteration
# O(n * m log(m)) time | O(n * m) space
# where n is the number of strings in the array
# where m is the length of the longest string
# def groupAnagrams(words):
#     # Write your code here.
#     anagrams = {}
#     for word in words:
#         sortedWord = "".join(sorted(word))
#         if sortedWord in anagrams:
#             anagrams[sortedWord].append(word)
#         else:
#             anagrams[sortedWord] = [word]
#     return list(anagrams.values())


# first iteration
# O(n * m log(m) + m * n log(n)) time | O(n * m) space
# where n is the number of strings in the array
# where m is the length of the longest string
def groupAnagrams(words):
    # Write your code here.
    if not words:
        return []

    # O(n * m log(m)) time
    sortedWords = ["".join(sorted(word)) for word in words]
    indices = [i for i in range(len(words))]
    # O(m * n log(n)) time
    indices.sort(key=lambda x: sortedWords[x])

    results = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for i in indices:
        if sortedWords[i] == currentAnagram:
            currentAnagramGroup.append(words[i])
            continue

        currentAnagram = sortedWords[i]
        results.append(currentAnagramGroup)
        currentAnagramGroup = [words[i]]

    results.append(currentAnagramGroup)
    return results


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
