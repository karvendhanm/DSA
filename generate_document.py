# first iteration
# O(mn) time | O(m) + O(n) space
# where m - number of characters in "characters" string.
# where n - number of characters in "document" string.
def generateDocument(characters, document):
    # Write your code here.
    if document == "":
        return True

    characters = list(characters)
    document = list(document)

    for _char in document:
        if _char not in characters:
            return False
        characters.remove(_char)
    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


generateDocument(characters, document)