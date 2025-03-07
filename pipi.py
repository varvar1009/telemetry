import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
def generate_key():
    return os.urandom(16)  

def encrypt_message(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_data.decode()

aes_key = generate_key()

message1 = "Встреча Боба и Алисы 10 марта в кино"
encrypted1 = encrypt_message(aes_key, message1)
print(f"Зашифрованное сообщение 1: {encrypted1.hex()}")

message2 = "Встреча Боба и Алисы 15 марта в кафе"
encrypted2 = encrypt_message(aes_key, message2)
print(f"Зашифрованное сообщение 2: {encrypted2.hex()}")

block_size = 16
modified_encrypted2 = encrypted2[:-block_size] + encrypted1[-block_size:]

modified_message2 = decrypt_message(aes_key, modified_encrypted2)
print(f"Расшифрованное изменённое сообщение 2: {modified_message2}")
super_secret_key = varvar
key = super_secret_key.to_bytes(16, 'big')
key=
encrypter_message = aesEncryptor.update(message)
print(encrypter_message)
print(aesDecryptor.update(encrypter_message))
encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'
print(aesDecryptor.update(encrypter_message))
encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'
super_secret_key = 1234654# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), 
backend=default_backend()) 
aesEncryptor = aesCipher.encryptor() 
aesDecryptor = aesCipher.decryptor()

print(aesDecryptor.update(encrypter_message))

kpop=b'love darina                '
polk=aesEncryptor.update(klop) 
print(polk)
k=b'\xdc\x9fw^\xfd\xb8\x83\x11a`\x84\t9\xa0\xef\xa8'
print(aesDecryptor.update(k))
super_secret_key = 12345# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')

#2 шифруем сообщение
encrypter_message = b'love darina'

#3 расшифровываем 
print(encrypter_message)
print(aesDecryptor.update(encrypter_message))


#Пример:
#encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'


#super_secret_key = 1234654

#print(aesDecryptor.update(encrypter_message))