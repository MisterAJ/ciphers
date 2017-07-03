from crypto import atbash
from crypto import rail
from crypto import polybius

atb_cipher = atbash.Atbash()
rail_cipher = rail.Rail()
polybius_cipher = polybius.Polybius()

secure = rail_cipher.encrypt(text='If you do claim a ')

insecure = rail_cipher.decrypt(text=secure)


