from crypto import ciphers

class Rail(ciphers.Cipher):
    def __init__(self):
        self.one = []
        self.two = []
        self.three = []
        pass

    def encrypt(self, text):
        one = text[::4]
        two = text[1::2]
        three = text[2::4]
        return one + two + three

    def decrypt(self, text):
        one = text[::4]
        two = text[1::2]
        three = text[2::4]
        return

