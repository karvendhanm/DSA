# O(n^2) time | O(c) space
# where n is the number of characters
# where c is the number of unique characters in the string
def firstNonRepeatingCharacter(string):
    # Write your code here.
    previously_seen = set()
    for _idx, char in enumerate(string):
        if char not in previously_seen:
            scout = _idx + 1
            while True:
                if scout > len(string) - 1:
                    return _idx

                if string[scout] == char:
                    break
                scout += 1
            previously_seen.add(char)
    return -1


string = "abab"
print(firstNonRepeatingCharacter(string))