from crypto import ciphers


class Atbash(ciphers.Cipher):
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.cipher = self.alphabet[51::-1]
        self.cipher += "@"

    def encrypt(self, text):
        code = []
        for letter in text:
            letter = self.cipher[self.alphabet.index(letter)]
            code.append(letter)
        return ''.join(code)

    def decrypt(self, text):
        code = []
        text = text.upper()
        for letter in text:
            letter = self.alphabet[self.cipher.index(letter)]
            code.append(letter)
        return ''.join(code)
