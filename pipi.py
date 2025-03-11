
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from os import urandom

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

message1 = "Встреча Боба и Алисы 10 марта в кафе"
encrypted1 = encrypt_message(aes_key, message1)
print(f"Зашифрованное сообщение 1: {encrypted1.hex()}")

message2 = "Встреча Боба и Алисы 31 марта в кино"
encrypted2 = encrypt_message(aes_key, message2)
print(f"Зашифрованное сообщение 2: {encrypted2.hex()}")

modified_encrypted2 = encrypted2[:-16] + encrypted1[-16:]

modified_message2 = decrypt_message(aes_key, modified_encrypted2)
print(f"Расшифрованное изменённое сообщение 2: {modified_message2}") 

#print(aesDecryptor.update(encrypter_message))