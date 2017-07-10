from crypto import ciphers

'''The rail fence cipher (also called a zigzag cipher) is a form of 
transposition cipher. It derives its name from the way in which it is encoded.
'''


class Rail(ciphers.Cipher):
    def __init__(self):
        self.one = []
        self.two = []
        self.three = []
        pass

    '''Takes a string and returns an encoded message string'''
    def encrypt(self, text):
        text = text.replace(' ', '')
        if len(text) != 13 or 25 or 49 or 73 or 97:
            if len(text) < 13:
                while len(text) < 13:
                    text += 'x'

            elif len(text) < 25:
                while len(text) < 25:
                    text += 'x'

            elif len(text) < 49:
                while len(text) < 49:
                    text += 'x'

            elif len(text) < 73:
                while len(text) < 73:
                    text += 'x'

            elif len(text) < 97:
                while len(text) < 97:
                    text += 'x'

        one = text[::4]
        two = text[1::2]
        three = text[2::4]
        return one + two + three

    '''Takes an encoded message string and returns a decoded string'''
    def decrypt(self, text):
        print(len(text))
        chunk = int(len(text) / 4)

        one = text[:chunk + 1]
        first_line = []
        for letter in one:
            first_line.append(letter + '---')

        two = text[chunk + 1: chunk * 3 + 1]
        second_line = []
        for letter in two:
            second_line.append(letter + '-')

        three = text[chunk * 3 + 1:]
        third_line = []
        for letter in three:
            third_line.append(letter + '---')
        return (''.join(first_line) + '\n-' +
                ''.join(second_line) + '\n--' +
                ''.join(third_line))


