import string

from crypto import ciphers

'''The Caesar cipher, also known as a shift cipher, is 
one of the simplest forms of encryption. It is a substitution 
cipher where each letter in the original message (called the plaintext) is 
replaced with a letter corresponding to a certain number of letters up or 
down in the alphabet.
'''


class Caesar(ciphers.Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = (string.ascii_uppercase +
                        string.ascii_uppercase[:self.offset+1])
        self.BACKWARD = (string.ascii_uppercase[:self.offset+1] +
                         string.ascii_uppercase)

    '''Takes a string and returns an encoded message string'''
    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    '''Takes an encoded message string and returns a decoded string'''
    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)



