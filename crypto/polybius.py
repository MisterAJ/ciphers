from crypto import ciphers

'''In cryptography, the Polybius square, also known as the Polybius 
checkerboard, is a device invented by the Ancient Greek historian and 
scholar Polybius,[1] for fractionating plaintext characters so that 
they can be represented by a smaller set of symbols.
'''


class Polybius(ciphers.Cipher):

    def __init__(self):
        super().__init__()
        self.reverse_mapping = {}
        self.mapping = {}
        self.cells = (
            ('A', 'B', 'C', 'D', 'E'),
            ('F', 'G', 'H', 'I', 'K'),
            ('L', 'M', 'N', 'O', 'P'),
            ('Q', 'R', 'S', 'T', 'U'),
            ('V', 'W', 'X', 'Y', 'Z'),
            ('J',)
        )
        for (i, row) in enumerate(self.cells, start=1):
            for (j, letter) in enumerate(row, start=1):
                self.mapping[letter] = str(i)+str(j)

        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

    '''Takes a string and returns an encoded message string'''
    def encrypt(self, text):
        result = ''
        for letter in text.upper():
            code = self.mapping.get(letter)
            if code:
                result += code
            else:
                result += letter
        return result

    '''Takes an encoded message string and returns a decoded string'''
    def decrypt(self, text):
        raw = text
        result = ''
        while raw:
            code = raw[:2]
            de_code = self.reverse_mapping.get(code)
            if de_code:
                result += de_code
                raw = raw[2:]
            else:
                result += raw[:1]
                raw = raw[1:]
        return result
