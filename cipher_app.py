"""Program for encoding and decoding messages with basic ciphers"""
from crypto import atbash
from crypto import rail
from crypto import polybius

if __name__ == '__main__':

    atb_cipher = atbash.Atbash()
    rail_cipher = rail.Rail()
    polybius_cipher = polybius.Polybius()

    secure = rail_cipher.encrypt(text='')

    insecure = rail_cipher.decrypt(text=secure)

    app_on = ''

    print('Welcome to the magic Cipho-Matic!')
    while app_on.lower() != 'n':

        select = 0
        selector = input(
                'Select a Cipher\n\n1 - Atbash\n'
                '2 - Transposition Rail\n3 - Polybius\n\n-- '
        )

        enc_or_dec = 'Would you like to 1 - encode or 2 - decipher? : '

        if selector == '1':
            select = input(enc_or_dec)
            if select == '1':
                keyword = input('What is the message? : ')
                print(atb_cipher.encrypt(keyword))
            if select == '2':
                keyword = input('What is the code? : ')
                print(atb_cipher.decrypt(keyword))

        if selector == '2':
            select = input(enc_or_dec)
            if select == '1':
                keyword = input('What is the message? : ')
                print(rail_cipher.encrypt(keyword))
            if select == '2':
                keyword = input('What is the code? : ')
                print(rail_cipher.decrypt(keyword))

        if selector == '3':
            select = input(enc_or_dec)
            if select == '1':
                keyword = input('What is the message? : ')
                print(polybius_cipher.encrypt(keyword))
            if select == '2':
                keyword = input('What is the code? : ')
                print(polybius_cipher.decrypt(keyword))

        input('Press enter to continue\n\n\n')

        app_on = input('Would you like to work on another message?'
                       ' y/n : \n\n -- ')
