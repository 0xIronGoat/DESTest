import binascii
import des


def encrypt_des(cleartext):
    key = des.DesKey(bytes("75849301", 'utf-8'))  # Needs to be hardened here
    encrypted = key.encrypt(bytes(cleartext, 'utf-8'), padding=True)
    hex_encrypted = binascii.hexlify(encrypted)
    decrypted = key.decrypt(encrypted, padding=True)
    print("Your encrypted message is: ", hex_encrypted)
    print("Your original message was: ", decrypted)


message = input("Please enter your secret message:\n")
encrypt_des(message)
