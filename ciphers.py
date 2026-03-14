import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

def caesar_cipher(plaintext, key):
    result = ""
    for char in plaintext:
        if char in lower:
            cipherIndex = (lower.index(char) + key) % 26
            char = lower[cipherIndex]
            result += char
        elif char in upper:
            cipherIndex = (upper.index(char) + key) % 26
            char = upper[cipherIndex]
            result += char
        else:
            result += char
    return result

def vigenere_cipher(plaintext, key):
    shiftKeys = []
    for char in key:
        if char in lower:
            cipherIndex = lower.index(char)
            shiftKeys.append(cipherIndex)
        elif char in upper:
            cipherIndex = upper.index(char)
            shiftKeys.append(cipherIndex)
    completionCounter = 0
    shiftCycleCounter = 0
    keyLength = len(shiftKeys)
    result = ""

    while completionCounter != len(plaintext):
        if plaintext[completionCounter] in lower:
            cipherIndex = (lower.index(plaintext[completionCounter]) + shiftKeys[shiftCycleCounter]) % 26
            char = lower[cipherIndex]
            result += char
            completionCounter += 1
            shiftCycleCounter = (shiftCycleCounter + 1) % keyLength

        elif plaintext[completionCounter] in upper:
            cipherIndex = (upper.index(plaintext[completionCounter]) + shiftKeys[shiftCycleCounter]) % 26
            char = upper[cipherIndex]
            result += char
            completionCounter += 1
            shiftCycleCounter = (shiftCycleCounter + 1) % keyLength
        
        else:
            result += plaintext[completionCounter]
            completionCounter += 1
    return result

# print(caesar_cipher("secret Message from Above! Stay safe everyONE.", 7))
print(vigenere_cipher("secret Message from Above! Stay safe everyONE.", "key"))
