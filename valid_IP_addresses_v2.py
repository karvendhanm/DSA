# O(1) time and O(1) space
def validIPAddresses(string):
    validIPAddresses = []
    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ["", "", "", ""]
        currentIPAddressParts[0] = string[:i]
        if not isValidPart( currentIPAddressParts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i:j]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    validIPAddresses.append(".".join(currentIPAddressParts))
    return validIPAddresses


def isValidPart(string):
    strAsInt = int(string)
    if strAsInt > 255:
        return False
    return len(string) == len(str(strAsInt))


string = '1921680'
print(validIPAddresses(string))
