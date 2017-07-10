from crypto import ciphers

'''Atbash is a monoalphabetic substitution cipher'''


class Atbash(ciphers.Cipher):
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.cipher = self.alphabet[51::-1]
        self.cipher += "@"

    '''Takes a string and returns an encoded message string'''
    def encrypt(self, text):
        code = []
        for letter in text:
            letter = self.cipher[self.alphabet.index(letter)]
            code.append(letter)
        return ''.join(code)

    '''Takes an encoded message string and returns a decoded string'''
    def decrypt(self, text):
        code = []
        text = text.upper()
        for letter in text:
            letter = self.alphabet[self.cipher.index(letter)]
            code.append(letter)
        return ''.join(code)
