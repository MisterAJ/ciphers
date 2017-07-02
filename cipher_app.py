from crypto import atbash
from crypto import rail

atb_cipher = atbash.Atbash()
rail_cipher = rail.Rail()

phrase = "Ride on the magic school bus"
secure = rail_cipher.encrypt(text=phrase)
insecure = rail_cipher.decrypt(text=phrase)


print(secure)

print(insecure)

