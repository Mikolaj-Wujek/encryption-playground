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

print(caesar_cipher("hello I am under the WATER HELLO", 7))