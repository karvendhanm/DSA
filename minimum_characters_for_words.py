# first iteration
def minimumCharactersForWords(words):
    # Write your code here.
    overallMinimumCharacters = {}
    for word in words:
        currentMinimumCharacters = {}
        for char in word:
            if char in currentMinimumCharacters:
                currentMinimumCharacters[char] += 1
            else:
                currentMinimumCharacters[char] = 1
        for key in currentMinimumCharacters.keys():
            if key in overallMinimumCharacters:
                overallMinimumCharacters[key] = max(overallMinimumCharacters[key], currentMinimumCharacters[key])
            else:
                overallMinimumCharacters[key] = currentMinimumCharacters[key]
    minCharacters = [[key] * value for key, value in overallMinimumCharacters.items()]
    return [elem for lst in minCharacters for elem in lst]


words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))