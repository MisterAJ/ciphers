"""Super class for the ciphers"""


class Cipher:
    def encrypt(self, **kwargs):
        raise NotImplementedError()

    def decrypt(self, **kwargs):
        raise NotImplementedError()
