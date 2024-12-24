# first iteration
# O(n * m) time | O(c) space
# where n is the number of words.
# where m is the length of the longest word.
# where c is the number of unique letters in all the words in the list "words"
def minimumCharactersForWords(words):
    # Write your code here.
    overallMinimumCharacters = {}
    for word in words:
        currentMinimumCharacters = {}
        for char in word:
            currentMinimumCharacters[char] = currentMinimumCharacters.get(char, 0) + 1
        for key in currentMinimumCharacters.keys():
            overallMinimumCharacters[key] = max(overallMinimumCharacters.get(key, 0), currentMinimumCharacters[key])

    minCharacters = [[key] * value for key, value in overallMinimumCharacters.items()]
    return [elem for lst in minCharacters for elem in lst]


words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))
